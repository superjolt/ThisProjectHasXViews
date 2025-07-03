import scratchattach as sa
import os
from dotenv import load_dotenv

load_dotenv()

SESSION_ID = os.getenv("SESSION_ID")

if SESSION_ID is None:
    print("SESSION_ID must be present in .env")
    exit(1)

session = sa.login_by_id(SESSION_ID)
project = session.connect_project("1193782687")

# def create_thumbnail(views, loves, faves):
#     img = Image.new('RGB', (480, 360), color='white')
#     d = ImageDraw.Draw(img)
    
#     font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 40)

#     text = f"Views: {views}\nLoves: {loves}\nFaves: {faves}"
#     d.text((10,10), text, fill=(0,0,0), font=font)

#     img.save("thumbnail.png")

views = project.views
loves = project.loves
faves = project.favorites
remix = project.remix_count
comments = len(project.comments())

title = f"This Project Has {views} Views, {loves} Loves and {faves} Faves"
instructions = f"And this has {remix} remixes.\nAnd {comments} comments."

if not project.title == title and not project.instructions == instructions:
    project.set_title(title)
    project.set_instructions(instructions)
    
    # create_thumbnail(views, loves, faves)
    # project.set_thumbnail(file="thumbnail.png")

    print(f"Updated, {views} views, {loves} loves, {faves} faves, and {remix} remixes.")
