import os
import httpx
from fastapi import FastAPI
from pydantic import BaseModel


OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "qwen2.5-coder:0.5b")
OLLAMA_API_URL = f"{OLLAMA_HOST}/api/generate"


class TextRequest(BaseModel):
    input_text: str


class TextResponse(BaseModel):
    generated_text: str


app = FastAPI()

'''
Эндпоинт для генерации текста через llm.

На вход подается строка текста, которая потом отправляется как запрос в llm.
Выводится сгенерированный ответ от модели тоже в виде строки.
'''
@app.post("/generate", response_model=TextResponse)
async def generate_text(request: TextRequest):
    if not request.input_text or not request.input_text.strip():
        return TextResponse(
            generated_text="Генерация отсутствует из-за пустой строки."
        )

    payload = {
        "model": MODEL_NAME,
        "prompt": request.input_text,
        "stream": False
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                OLLAMA_API_URL,
                json=payload,
                timeout=120.0
            )
            response.raise_for_status()
            result = response.json()

            return TextResponse(
                generated_text=result.get("response", "")
            )


        except Exception as e:
            exception_name = type(e).__name__
            return TextResponse(
                generated_text=exception_name
            )
