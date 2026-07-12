from fastapi import FastAPI

app = FastAPI(
    title="AssetFlow API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "success": True,
        "message": "AssetFlow API is running",
        "data": {}
    }