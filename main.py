from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello():
    return {'message': 'hello world'}

# codes
# 070: year
# __ : competition
# __ : name
# __ : project
# __ : position


@app.get('/certificate/')
async def certificate(id: str):
    return id
