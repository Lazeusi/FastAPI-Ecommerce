from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="FastAPI E-Commerce API",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI E-Commerce API!"}

if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=8000 ,reload=True)