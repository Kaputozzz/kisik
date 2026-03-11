import os
import uvicorn
from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from aiogram import Bot, Dispatcher, types
import asyncio

TOKEN = "8686415598:AAG2F6-jONDK_gKw7hgXWO__7NptbK9v_Rk"
ADMIN_ID = 6240780160

app = FastAPI()
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Створюємо папку для завантажень, якщо її нема
UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_item():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# Тут буде твій API для додавання/видалення товарів (як у попередньому повідомленні)

async def main():
    # Render передає порт через змінну оточення PORT
    port = int(os.environ.get("PORT", 8000))
    config = uvicorn.Config(app, host="0.0.0.0", port=port)
    server = uvicorn.Server(config)
    
    # Запускаємо сервер та бот паралельно
    await asyncio.gather(server.serve(), dp.start_polling(bot))

if __name__ == "__main__":
    asyncio.run(main())