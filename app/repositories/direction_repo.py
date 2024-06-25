from app.repositories.firebase_config import ref
import json

def dbGetDirection():
    direc = ref.child('templates')
    snapshot = direc.get()
    # json_data = json.dumps(list(snapshot.items()))
    # text_data = json.dumps(json_data)
    return snapshot.items()