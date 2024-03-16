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
    base64: str

app = FastAPI()

@app.post("/labels")
def Labels_m(image_data: ImageData):
    try:
        image_bytes = base64.b64decode(image_data.base64)
        with open("test_image.jpg", "wb") as file:
            file.write(image_bytes)
    except Exception as ex:
        raise HTTPException(status_code=400, detail="Error decodificando la imagen")
    
    try:
        response = client.detect_labels(Image={'Bytes': image_bytes})
        return response
    except Exception as ex:
        print(ex)
        return False