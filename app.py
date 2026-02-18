from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str

@app.get("/hello")
def hello():
    return {"message": "Hello World from EC2"}

@app.post("/hello")
def hello_user(user: User):
    return {"message": f"Hello {user.name} from EC2"}
