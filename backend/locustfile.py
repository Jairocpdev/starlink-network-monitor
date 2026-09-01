from locust import HttpUser, task, between
import websocket
import json
import time

class StarlinkUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://starlink-network-monitor.onrender.com"

    @task
    def test_rest(self):
        # Testa seu /antennas
        self.client.get("/antennas")
        self.client.get("/health")

    @task
    def test_websocket(self):
        # Testa seu /ws/telemetry
        ws_url = "wss://starlink-network-monitor.onrender.com/ws/telemetry"
        try:
            ws = websocket.create_connection(ws_url, timeout=5)
            start = time.time()
            data = ws.recv()  # recebe os 50 nós
            latency = (time.time() - start) * 1000
            print(f"WS latency: {latency:.2f}ms - {len(data)} bytes")
            ws.close()
        except Exception as e:
            print(f"WS fail: {e}")