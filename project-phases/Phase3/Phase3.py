from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()
version = "v0.0.1"

# Endpoint to return app version
@app.get("/version")
def get_version():
    return {"version": version}

# Endpoint to return current average temperature based on senseBox data
@app.get("/temperature")
def get_temperature():
    global sensebox_data

    # Fetch new data if last data is older than 1 hour
    if (not sensebox_data or 
      (datetime.utcnow() - sensebox_data.get("timestamp", datetime.min)) >
      timedelta(hours=1)):
        response = requests.get("https://api.opensensemap.org/boxes/data")
 
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch senseBox data")

        data = response.json()
        temperatures = [
        box["sensors"][0]["lastMeasurement"] if "sensors" in box and 
        box["sensors"][0]["type"] == "temperature" else None
        for box in data if box
                       ]
        valid_temperatures = [temp for temp in temperatures if temp is not None]
        avg_temperature = sum(valid_temperatures) / len(valid_temperatures) 
        if valid_temperatures 
        else 0
        sensebox_data = {
            "timestamp": datetime.utcnow(),
            "avg_temperature": avg_temperature
        }

    return {"average_temperature": sensebox_data.get("avg_temperature")}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
