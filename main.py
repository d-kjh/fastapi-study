from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "가상환경에서 FastAPI 서버 실행 테스트1"}