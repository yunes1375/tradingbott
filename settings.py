import os
from dotenv import load_dotenv

load_dotenv()
MONGOENGINDB=os.getenv('MONGOENGINEDB')
HOST=os.getenv("HOST")
PORT=os.getenv("PORT")