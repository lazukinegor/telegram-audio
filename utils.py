from datetime import datetime

def log(msg: str):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")
