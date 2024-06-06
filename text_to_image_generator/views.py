from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests
import io
import base64
from PIL import Image
import json

load_dotenv()

API_URL = os.getenv('API_URL', None)
TOKEN = os.getenv('TOKEN', None)
headers = {"Authorization": f'Bearer {TOKEN}'}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response


def index_view(request):
    context = {}

    if TOKEN is not None and request.method == 'POST':
        user_prompt = request.POST.get('user_prompt')

        response = query({
            "inputs": user_prompt,
        })

        

        if response.status_code == 200:
            try:
                image_bytes = response.content
                image = Image.open(io.BytesIO(image_bytes))

                # Convert image to base64 string
                buffer = io.BytesIO()
                image.save(buffer, format='PNG')
                buffer.seek(0)
                image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

                context['image_base64'] = image_base64
            except Exception as e:
                context['error'] = f"Error processing image: {str(e)}"
        else:
            try:
                error_message = response.json().get('error', 'Unknown error occurred')
            except json.JSONDecodeError:
                error_message = 'Unknown error occurred'
            context['error'] = f"Error fetching image from API: {error_message}"

    return render(request, 'index.html', context)



def image_generation_view(request):
    return render(request, 'img_gen_page.html')