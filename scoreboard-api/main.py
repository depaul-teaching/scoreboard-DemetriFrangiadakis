import os
from fastapi import FastAPI, HTTPException

app = FastAPI(title="scoreboard-api")

VALID_TEAMS = ["Cubs", "White Sox", "Bears", "Bulls", "Blackhawks"]

@app.get("/")
def scoreboard():
    team = os.getenv("FAVORITE_TEAM", "Cubs")
    if team not in VALID_TEAMS:
        raise HTTPException(status_code=400, detail=f"Invalid team: {team}")

    return {
        "team": team,
        "build": os.getenv("BUILD_SHA", "unknown"),
        "status": "ok"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
