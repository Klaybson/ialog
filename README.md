## **Estrutura do Projeto**

```
k8s-deepseek-monitor/
│
├── app.py                  # Backend Flask
├── requirements.txt        # Dependências do Python
├── static/                 # Arquivos estáticos (CSS, JS)
│   └── styles.css

#### 6. **README.md**

```markdown
# Kubernetes Event Monitor with DeepSeek

Este projeto coleta eventos de um cluster Kubernetes e os envia para o DeepSeek para análise.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/k8s-deepseek-monitor.git
   cd k8s-deepseek-monitor
   ```

2. Configure as variáveis no arquivo `app.py`:
   - `K8S_MASTER_IP`: IP do master do Kubernetes.
   - `KUBECONFIG_PATH`: Caminho do arquivo kubeconfig.

3. Instale as dependências e inicie o servidor:
   ```bash
   ./run.sh
   ```

4. Acesse a interface web em:
   ```
   http://localhost:5000
   ```

## Autenticação
- Usuário: `admin`
- Senha: `senha123`
```

---

### **Pronto!**

Agora você tem um projeto completo com backend, frontend, autenticação e documentação. Para executar:

1. Configure as variáveis no `app.py`.
2. Rode o script `run.sh`.
3. Acesse a interface web e clique em "Buscar Eventos" para ver os eventos e a análise.

Se precisar de mais ajustes ou tiver dúvidas, é só perguntar! 🚀