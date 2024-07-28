import os
from dotenv import load_dotenv

# Load data from dotenv
load_dotenv(override=True)

BOT_TOKEN = os.environ.get('BOT_TOKEN')

ADMIN_IDS = [1094108028]