import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "15671595")

API_HASH = os.environ.get("API_HASH", "bb8f36f9c39a24c7f8b2acbc7ea8c60a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5879389660:AAHWvhjQpxMIBhTSObCXUOrzVaNYTN6MQOc") 

FORCE_SUB = os.environ.get("FORCE_SUB", "TG_UPDATES1") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Rename:Rename@cluster0.vlfzuid.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get('PORT', '8080')
