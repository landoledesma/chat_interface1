from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    message: str

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/send_message")
def send_message(data: Message):
    user_message = data.message

    # Aquí puedes conectarte a la API de ChatGPT para obtener la respuesta.
    # Por ahora, sólo devolvemos el mensaje en mayúsculas como ejemplo.
    chatgpt_response = user_message.upper()

    return JSONResponse(content={"reply": chatgpt_response})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
