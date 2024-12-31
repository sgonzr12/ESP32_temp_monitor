from fastapi import FastAPI
import uvicorn

app = FastAPI()

def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/temperature")
def read_temperature():
    # Replace with actual temperature reading logic
    temperature = 25.0
    return {"temperature": temperature}

    