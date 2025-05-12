# 📊 K8s Events Analyzer com Flask + Ollama

Este projeto é uma aplicação Flask que coleta eventos do Kubernetes usando `kubectl` e envia os dados para um modelo de IA local via API do Ollama para análise e resumo.

---

## 🚀 Funcionalidades

- Autenticação básica HTTP para acesso seguro
- Consulta de eventos em todos os namespaces do Kubernetes
- Integração com o modelo `deepseek-r1` via Ollama para gerar análise automática dos eventos
- Interface básica via HTML e API REST (`/api/k8s-events`)

---

## ⚙️ Requisitos

- Python 3.8+
- Kubernetes configurado com acesso por `kubectl`
- Ollama instalado e rodando localmente com o modelo `deepseek-r1`
- Chave `KUBECONFIG` configurada corretamente (ou padrão: `~/.kube/config`)

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone git@gitlab.klaybson.com.br:flask/ialog.git
cd ialog
