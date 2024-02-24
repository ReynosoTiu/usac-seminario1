from fastapi import FastAPI

app = FastAPI()

@app.get("/check")
def index():
    return True

@app.get("/")
def index():
    return {
        "Instancia": "Instancia #1 - API #1",
        "Curso": "Seminario de Sistemas 1",
        "Estudiante": "Estudiante - <201345126>"
    }