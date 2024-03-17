from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import boto3
from dotenv import load_dotenv
import os

load_dotenv()

region_name = os.getenv('AWS_REGION')
aws_access_key_id = os.getenv('AWS_ACCESS_KEY')
aws_secret_access_key = os.getenv('AWS_SECRET_KEY')

client = boto3.client(
    'rekognition',
    region_name = region_name,
    aws_access_key_id = aws_access_key_id,
    aws_secret_access_key = aws_secret_access_key
)

class ImageData(BaseModel):
    base64_1: str
    base64_2: str

app = FastAPI()

@app.post("/tarea4-201345126")
def Compare_m(imagenes: ImageData):
    try:
        image_bytes = base64.b64decode(imagenes.base64_1)
        image_bytes2 = base64.b64decode(imagenes.base64_2)
        with open("foto1.jpg", "wb") as file:
            file.write(image_bytes)
        with open("foto2.jpg", "wb") as file:
            file.write(image_bytes2)
                 
    except Exception as ex:
        raise HTTPException(status_code=400, detail="Error decodificando la imagen")
    
    try:
        response = client.compare_faces(
            SourceImage={
                'Bytes': image_bytes
            },
            TargetImage={
                'Bytes': image_bytes2
            }
        )
        return response["FaceMatches"][0]["Similarity"]
    except Exception as ex:
        print(ex)
        return False