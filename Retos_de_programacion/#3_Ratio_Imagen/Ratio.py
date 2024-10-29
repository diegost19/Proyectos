from PIL import Image
import requests
from io import BytesIO
from math import gcd

def tamanio(url):
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        width, height = img.size
    else:
        return 0,0
    return width, height

def ratio(url):
    width,height= tamanio(url)
    divisor = gcd(width, height)
    x = width // divisor
    y = height // divisor
    print(f"El ratio es {x}:{y}")

ratio("https://www.asadorcitywoktalavera.com/wp-content/uploads/2021/10/alimentos-ricos-en-proteinas-1024x683.jpg")
