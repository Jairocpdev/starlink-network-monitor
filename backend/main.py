from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import json
import random
from datetime import datetime

app = FastAPI(title="Starlink Network Monitor", version="1.0.0")

@app.get("/")
def root():
    return {
        "project": "Starlink Network Monitor",
        "status": "online",
        "docs": "/docs",
        "health": "/health",
        "antennas": "/antennas",
        "ws": "/ws/telemetry",
        "fleet": 50
    }

@app.get("/health")
def health():
    return {"status": "ok", "fleet": 50}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REGIONS = ["BR-SE", "US-WEST", "EU-WEST"]

def generate_antenna(id_num):
    region = random.choice(REGIONS)
    base_latency = random.uniform(15, 60)
    
    r = random.random()
    if r < 0.12:
        latency = random.uniform(100, 150)
        status = "degraded" if latency < 130 else "offline"
    else:
        latency = base_latency
        status = "online"

    return {
        "id": f"ANT-{id_num:03d}",
        "region": region,
        "latency": round(latency, 2),
        "signal": random.randint(-65, -35),
        "status": status,
        "uptime": 99.9,
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/antennas")
def get_all():
    return [generate_antenna(i) for i in range(1, 51)]

@app.websocket("/ws/telemetry")
async def telemetry(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            antennas = [generate_antenna(i) for i in range(1, 51)]
            avg = sum(a["latency"] for a in antennas) / len(antennas)
            payload = {
                "antennas": antennas,
                "avg_latency": round(avg, 2),
                "timestamp": datetime.utcnow().isoformat()
            }
            await ws.send_text(json.dumps(payload))
            await asyncio.sleep(0.9)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"WS Error: {e}")
        try:
            await ws.close()
        except:
            pass