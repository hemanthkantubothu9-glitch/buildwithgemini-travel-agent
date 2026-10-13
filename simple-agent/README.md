# Build with Gemini: Travel Guide Agent 🌍

A personalized, intelligent travel guide AI agent built with **Google Agent Development Kit (ADK)** and powered by **Gemini 3.8 Flash** on Google Cloud Vertex AI.

The agent grounds its recommendations in real-time using **Google Web Search** and remembers user travel styles, dietary preferences, and past destinations across sessions using **Vertex AI Memory Bank**.

---

## 🌟 Key Features

- **Real-Time Google Search Grounding**: Live, factual information for destinations worldwide via Google Search.
- **Cross-Session Long-Term Memory**: Powered by Vertex AI Memory Bank (`PreloadMemoryTool` + auto-memory generation callback) to remember your preferences (e.g., pure vegetarian, budget vs luxury, heritage lover) across conversations.
- **Structured Categories**: Every destination query is automatically structured into:
  - 🏛️ **Historic & Mythological Places**: Ancient temples, monuments, UNESCO world heritage sites.
  - 🏙️ **Famous Sights & Top Attractions**: Iconic city landmarks, viewpoints, nature escapes.
  - 🛍️ **Shopping & Malls**: Traditional local bazaars, artisanal handicraft markets, modern malls.
  - 🍜 **Food & Culinary Delights**: Must-try dishes, iconic street eateries, regional sweets.
  - 💡 **Practical Travel Tips**: Best season to visit, transit advice, cultural etiquette.

---

## 🛠️ Tech Stack & Architecture

- **Model**: `gemini-3.8-flash`
- **Framework**: Google Agent Development Kit (`google-adk`)
- **Memory Service**: Vertex AI Memory Bank (`VertexAiMemoryBankService`)
- **Protocol**: Agent-to-Agent (A2A) protocol + FastAPI REST backend
- **Deployment**: Google Cloud Agent Engine (Agent Runtime)
- **Tooling**: `google_search`, `PreloadMemoryTool`

---

## 🚀 Running Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hemanthkantubothu9-glitch/buildwithgemini-travel-agent.git
   cd buildwithgemini-travel-agent
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

3. **Set up environment variables**:
   Create a `.env` file:
   ```bash
   GOOGLE_GENAI_USE_VERTEXAI=true
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_CLOUD_LOCATION=global
   MEMORY_BANK_ID=your-agent-engine-id
   ```

4. **Run the local interactive server**:
   ```bash
   uv run adk web --port 8080 --reload_agents app
   ```
   Open `http://localhost:8080` in your browser.

---

## ☁️ Deployment

Deploy to Google Cloud Agent Runtime using `agents-cli`:
```bash
agents-cli deploy --project your-project-id
```
| `agents-cli publish gemini-enterprise` | Register deployed agent to Gemini Enterprise                    || [A2A Inspector](https://github.com/a2aproject/a2a-inspector) | Launch A2A Protocol Inspector                                                        |

## 🛠️ Project Management

| Command | What It Does |
|---------|--------------|
| `agents-cli scaffold enhance` | Add CI/CD pipelines and Terraform infrastructure |
| `agents-cli infra cicd` | One-command setup of entire CI/CD pipeline + infrastructure |
| `agents-cli scaffold upgrade` | Auto-upgrade to latest version while preserving customizations |

---

## Development

Edit your agent logic in `app/agent.py` and test with `agents-cli playground` - it auto-reloads on save.

## Deployment

```bash
gcloud config set project <your-project-id>
agents-cli deploy
```

To add CI/CD and Terraform, run `agents-cli scaffold enhance`.
To set up your production infrastructure, run `agents-cli infra cicd`.

## Observability

Built-in telemetry exports to Cloud Trace, BigQuery, and Cloud Logging.

## A2A Inspector

This agent supports the [A2A Protocol](https://a2a-protocol.org/). Use the [A2A Inspector](https://github.com/a2aproject/a2a-inspector) to test interoperability.
See the [A2A Inspector docs](https://github.com/a2aproject/a2a-inspector) for details.
