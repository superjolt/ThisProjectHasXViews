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

views = project.views
loves = project.loves
faves = project.favorites
remix = project.remix_count
comments = len(project.comments())
studios = len(project.studios())
moderation = project.moderation_status()

title = f"This Project Has {views} Views, {loves} Loves and {faves} Faves"
instructions = f"And this has {remix} remixes. And {comments} comments. And in {studios} studios. Moderation status: {moderation}"

print(f"Script ran. Current project stats: {views} views, {loves} loves, {faves} faves, {remix} remixes, {comments} comments.")

if not project.title == title:
    project.set_title(title)
    print("UPDATED PROJECT: Title")

if not project.instructions == instructions:
    project.set_instructions(instructions)
    print("UPDATED PROJECT: Instructions")
