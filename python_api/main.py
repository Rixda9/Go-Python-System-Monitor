import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize the App
app = FastAPI()


# Structure the stats
class SystemStats(BaseModel):
    os: str
    cpu_percent: float = 0.0
    ram_percent: float


# When someone visits "/", this function runs
@app.get("/")
def read_root():
    return {"message": "Server is running! Go to /stats to see data."}


@app.get("/stats", response_model=SystemStats)
def get_system_stats():
    # set the exact url for Go worker
    go_worker_url = "http://localhost:9000/rawstats"

    try:
        # fetch the data
        response = requests.get(go_worker_url)
        # check if the go worker returned ok
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Go worker returned an error")
        # parse the json
        go_data = response.json()

        # map they keys
        stats = SystemStats(
            os=go_data.get("platform", "Unkown"),
            ram_percent=go_data.get("memoryUsedPercent", 0.0),
            cpu_percent=0.0,
        )
        return stats

    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail="Go worker is not running")
