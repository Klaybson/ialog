from flask import Flask, jsonify, render_template, request
import subprocess
import requests
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os
import logging

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configurações
K8S_MASTER_IP = "https://k8shome:6443"
KUBECONFIG_PATH = os.getenv("KUBECONFIG", "/Users/klaybson/.kube/config")
CONTEXT_NAME = "k8s-home"
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")

# Autenticação básica
users = {
    "admin": generate_password_hash("senha123", method="pbkdf2:sha256")
}

# Configuração de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

def get_k8s_events():
    try:
        if not os.path.exists(KUBECONFIG_PATH):
            return "Erro: Arquivo kubeconfig não encontrado."

        cmd = [
            "kubectl",
            "--kubeconfig", KUBECONFIG_PATH,
            "--context", CONTEXT_NAME,
            "--server", K8S_MASTER_IP,
            "get", "events", "--all-namespaces", "-o", "wide"
        ]
        logger.info("Executando comando: %s", " ".join(cmd))

        result = subprocess.run(cmd, capture_output=True, text=True)

        logger.info("Saída do kubectl (stdout): %s...", result.stdout[:200])
        logger.info("Saída do kubectl (stderr): %s", result.stderr)

        if result.returncode == 0:
            return result.stdout
        else:
            return f"Erro ao obter eventos: {result.stderr}"

    except Exception as e:
        logger.error("Exceção ao executar kubectl: %s", str(e))
        return f"Erro ao executar kubectl: {str(e)}"

def analyze_events_with_ollama(events):
    """
    Envia os eventos do Kubernetes para o Ollama e recebe uma análise.
    """
    try:
        data = {
            "model": "deepseek-r1:latest",  # Modelo que você baixou no Ollama
            "prompt": f"Analise os seguintes eventos do Kubernetes e forneça um resumo: {events}",
            "stream": False
        }
        response = requests.post(OLLAMA_API_URL, json=data)

        if response.status_code == 200:
            return response.json().get("response", "Nenhuma resposta do modelo.")
        else:
            return f"Erro ao obter resposta do Ollama: {response.text}"

    except Exception as e:
        return f"Erro ao conectar-se ao Ollama: {str(e)}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/k8s-events")
@auth.login_required
def k8s_events():
    try:
        events = get_k8s_events()
        analysis = analyze_events_with_ollama(events)
        return jsonify({
            "events": events,
            "analysis": analysis
        })
    except Exception as e:
        logger.error("Erro na rota /api/k8s-events: %s", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5041, debug=True)
