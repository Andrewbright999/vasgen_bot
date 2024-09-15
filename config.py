import os
from dotenv import load_dotenv

load_dotenv() 

TG_TOKEN = os.getenv("TG_TOKEN")
# You are connected to database "korobka" as user "korobka" via socket in "/var/run/postgresql" at port "5432".