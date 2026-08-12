cat > main.py << 'EOF'
import os
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("API_KEY")
db_url = os.getenv("DATABASE_URL")

# DO NOT hard-code secrets like this:
# api_key = "supersecret123"
EOF