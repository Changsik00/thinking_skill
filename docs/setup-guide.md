# Setup & Troubleshooting Guide

## 1. Prerequisites
- **OS**: macOS (Recommended), Linux, or Windows (WSL2)
- **Python**: 3.11 or higher
- **Docker**: Docker Desktop must be installed and running.

## 2. Installation

1.  **Clone the repository** (if not already done).
2.  **Environment Setup**:
    ```bash
    cp .env.example .env
    # Edit .env and key in your GEMINI_API_KEY
    ```
3.  **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 3. Running the Infrastructure
MACS uses Docker for its "Body" (Action & Memory) layer.

```bash
docker compose up -d
```

Check if services are running:
```bash
docker ps
# Should see: 'chromadb/chroma' and 'n8n'
```

## 4. Troubleshooting

### Issue: Docker Connection Failed
**Error**: `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`
**Solution**:
- Ensure **Docker Desktop** app is running.
- On macOS, look for the whale icon in the menu bar.

### Issue: Container Name Conflict
**Error**: `Conflict. The container name "/thingking-n8n-1" is already in use...`
**Solution**:
Old containers might be lingering. Remove them and restart:
```bash
docker rm -f thingking-n8n-1 thingking-chroma-1
docker compose up -d
```
