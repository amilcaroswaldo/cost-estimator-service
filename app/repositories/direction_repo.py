from fastapi import FastAPI
from .firebase_config import ref
import json
app = FastAPI()

@app.get("/direction")
def dbGetDirection():
    direc = ref.child('direction')
    snapshot = direc.get()
    # json_data = json.dumps(list(snapshot.items()))
    # text_data = json.dumps(json_data)
    return snapshot.items()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    #uvicorn.run(app, host="127.0.0.1", port=8000)
    #uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
    #uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")