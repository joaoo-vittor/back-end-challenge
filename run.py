import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.main.configs.app:api", host="0.0.0.0", port=8000, reload=True, debug=True
    )
