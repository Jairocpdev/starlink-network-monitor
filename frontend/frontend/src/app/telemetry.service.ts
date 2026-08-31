import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';

@Injectable({ providedIn: 'root' })
export class TelemetryService {
  private socket$: WebSocketSubject<any>;
  
  constructor(){
    this.socket$ = webSocket('wss://starlink-network-monitor.onrender.com/ws/telemetry');
  }
  
  getTelemetry() {
    return this.socket$.asObservable();
  }
}