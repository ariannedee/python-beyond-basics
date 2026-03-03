import requests
import shutil

URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada_%28Pantone%29.svg/60px-Flag_of_Canada_%28Pantone%29.svg.png"

headers = {"User-Agent": f"Your name (your@email.com)"}
response = requests.get(URL, headers=headers, stream=True)

response.raise_for_status()

with open("image.png", "wb") as f:
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, f)
