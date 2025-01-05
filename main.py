import requests
import sys
from PIL import Image


txt = ""
def generate(prompt):
    url = "https://api.prodia.com/v1/sd/generate"

    payload = {
        "model": "absolutereality_V16.safetensors [37db0fc3]",
        "prompt": prompt,
        "steps": 20,
        "cfg_scale": 7,
        "seed": -1,
        "upscale": True,
        "width": 512,
        "height": 512,
        "sampler": "DPM++ 2M Karras"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-Prodia-Key": "--------Enter your Api Key------" # enter your api key here
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    txt = response.text[8:44:]
    result(txt)


def result(txt):
    Check = 1
    while True:
        if Check > 15:
            url = f"https://images.prodia.xyz/{txt}.png"
            save_path = "image.jpg"

            response = requests.get(url)

            if response.status_code == 200:
                with open(save_path, "wb") as file:
                    file.write(response.content)
                print(f"Image downloaded and saved to {save_path}")
            else:
                print(f"Failed to download image. Status code: {response.status_code}")

            break


        else:
            url = f"https://api.prodia.com/v1/job/{txt}"

            headers = {
            "accept": "application/json",
            "X-Prodia-Key": "38b15b3f-937c-4da2-85c5-37a98298df26"
        }

            response = requests.get(url, headers=headers)
            Check = Check+1

    

    image = Image.open("image.jpg")
    image.show()
            



prompt = "Generate a image of a lion riding a bike and racing a tiger"
generate(prompt)
