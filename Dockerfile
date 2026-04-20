FROM ollama/ollama


COPY download_model.sh /download_model.sh
RUN chmod +x /download_model.sh

ENV OLLAMA_MODEL=qwen2.5-coder:0.5b

EXPOSE 11434

ENTRYPOINT ["/download_model.sh"]
