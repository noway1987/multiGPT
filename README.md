# GPT SaaS App

Dieses Projekt demonstriert die Nutzung mehrerer GPT-Instanzen, um verschiedene Rollen in einem Softwareentwicklungsprozess zu übernehmen.

## Einrichtung

1. Klonen Sie das Repository:
    ```bash
    git clone https://github.com/USERNAME/gpt_saas_app.git
    cd gpt_saas_app
    ```

2. Installieren Sie die Abhängigkeiten:
    ```bash
    pip install flask openai
    ```

3. Setzen Sie Ihren OpenAI API-Schlüssel in den GPT-Instanzen:
    ```python
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    ```

4. Starten Sie die Flask-Anwendung:
    ```bash
    python app.py
    ```

## Endpunkt

- `/generate-app` (POST): Generiert die App basierend auf dem gegebenen Prompt.

### Beispielanforderung

```bash
curl -X POST http://127.0.0.1:5000/generate-app -H "Content-Type: application/json" -d '{"prompt": "A task management application"}'
```
