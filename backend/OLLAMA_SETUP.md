# Ollama Setup Guide

## Prerequisites

1. **Install Ollama**
   - Download from: https://ollama.ai/download
   - Or use: `curl -fsSL https://ollama.ai/install.sh | sh` (Linux/Mac)

2. **Pull a model**
   ```bash
   ollama pull gemma2:2b
   ```

## Configuration

The backend is configured to use Ollama via environment variables in `.env`:

```bash
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=gemma2:2b
```

### Available Models

You can use any model available in Ollama. Popular options:
- `gemma2:2b` (default, 2B parameters, fast and efficient)
- `llama3.2` (3B parameters)
- `llama3.2:1b` (smaller, faster)
- `mistral` (Mistral AI)
- `phi3` (Microsoft Phi-3)

To change the model, update `OLLAMA_MODEL` in `.env` and restart the backend.

## Running Ollama

1. **Start Ollama server**
   ```bash
   ollama serve
   ```

2. **Verify it's running**
   ```bash
   python test_ollama.py
   ```

3. **Start your backend**
   ```bash
   uvicorn app.main:app --reload
   ```

## Troubleshooting

### "Cannot connect to Ollama"
- Make sure Ollama is running: `ollama serve`
- Check if port 11434 is available
- Verify OLLAMA_URL in `.env` matches your Ollama server

### "Model not found"
- Pull the model: `ollama pull gemma2:2b`
- List available models: `ollama list`
- Update OLLAMA_MODEL in `.env` to match an installed model

### Slow responses
- Use a smaller model like `llama3.2:1b`
- Reduce `num_predict` in `chat_service.py`
- Ensure you have enough RAM (4GB+ recommended)

## Benefits of Ollama

✓ **Privacy**: All data stays on your machine  
✓ **No API costs**: Completely free  
✓ **Offline**: Works without internet  
✓ **Fast**: Local inference, no network latency  
✓ **Flexible**: Easy to switch models
