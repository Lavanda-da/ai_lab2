#!/bin/bash
set -e

# Запуск Ollama сервер и ожидание его готовности
ollama serve &
SERVER_PID=$!

until ollama list > /dev/null 2>&1; do
    sleep 1
done

# Загрузка модели
MODEL=${OLLAMA_MODEL:-qwen2.5-coder:0.5b}
ollama pull $MODEL

echo "Model $MODEL loaded successfully!"
