import scratchattach as sa
import os
from dotenv import load_dotenv
import time
from PIL import Image, ImageDraw, ImageFont
import random

load_dotenv()

SESSION_ID = os.getenv("SESSION_ID")

if SESSION_ID is None:
    print("SESSION_ID must be present in .env")
    exit(1)

session = sa.login_by_id(SESSION_ID)
project = session.connect_project("1193782687")

# Optional: Load a background image or set size
def create_thumbnail(views, loves, faves):
    img = Image.new('RGB', (480, 360), color='white')
    d = ImageDraw.Draw(img)
    
    font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 40)

    text = f"Views: {views}\nLoves: {loves}\nFaves: {faves}"
    d.text((10,10), text, fill=(0,0,0), font=font)

    img.save("thumbnail.png")

while True:
    views = project.views
    loves = project.loves
    faves = project.favorites
    remix = project.remix_count

    title = f"This Project Has {views} Views, {loves} Loves and {faves} Faves"
    instructions = f"And this has {remix} remixes."

    if project.title == title and project.instructions == instructions:
        print("Skipping, they're the same.")

        sleeping = random.randint(30, 50)
        print(f"Waiting an extra {sleeping}")

        time.sleep(sleeping)
    else:
        project.set_title(title)
        project.set_instructions(instructions)

        create_thumbnail(views, loves, faves)
        project.set_thumbnail(file="thumbnail.png")

        print(f"Updated, {views} views, {loves} loves, {faves} faves, and {remix} remixes.")

    sleeping = random.randint(10, 30)
    print(f"Waiting {sleeping}")
    time.sleep(sleeping)
