from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.analyzers import analyze_signal

app = FastAPI()

# Разрешаем все домены или указываем нужные
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можно заменить на ["http://localhost:8080"], если хотите ограничить доступ только этим доменом
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

class SignalRequest(BaseModel):
    signal: str

@app.post("/analyze_signal")
async def analyze(signal_request: SignalRequest):
    signal_data = signal_request.signal
    result = analyze_signal(signal_data)
    return JSONResponse(content=result)
