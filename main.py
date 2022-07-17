from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/posts")
def get_data():
    return {"data": "welcome to posts"}


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"message": "successfully created posts"}
