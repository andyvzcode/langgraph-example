from fastapi import FastAPI

from app.agent import graph

app = FastAPI()


@app.get("/")
async def agent():
    return graph.invoke({"customer_name": "hola", "my_var": ""})
