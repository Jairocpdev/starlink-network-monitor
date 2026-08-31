import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';

@Injectable({ providedIn: 'root' })
export class TelemetryService {
  private socket$: WebSocketSubject<any>;
  constructor(){
    this.socket$ = webSocket('ws://localhost:8000/ws/telemetry');
  }
  getTelemetry() {
    return this.socket$.asObservable();
  }
}