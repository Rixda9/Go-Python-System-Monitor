from fastapi import FastAPI
import psutil
import platform
from pydantic import BaseModel

# Initialize the App
app = FastAPI()


# Structure the stats
class SystemStats(BaseModel):
    os: str
    cpu_percent: float
    ram_percent: float


# When someone visits "/", this function runs
@app.get("/")
def read_root():
    return {"message": "Server is running! Go to /stats to see data."}


@app.get("/stats", response_model=SystemStats)
def get_system_stats():
    # Get CPU usage percentage
    cpu_usage = psutil.cpu_percent(interval=0.1)  # CHANGE THIS

    # Memory usage percentage
    mem = psutil.virtual_memory()
    memory_usage = mem.percent

    # Os name
    os_name = platform.system()
    if not os_name:
        os_name = "Unkown"

    # Return the data as JSON
    return {"os": os_name, "cpu_percent": cpu_usage, "ram_percent": memory_usage}
