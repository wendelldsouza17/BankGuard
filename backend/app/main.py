from fastapi import FastAPI

app = FastAPI(title="BankGuard")


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "BankGuard",
    }