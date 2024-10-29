"""/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */"""
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