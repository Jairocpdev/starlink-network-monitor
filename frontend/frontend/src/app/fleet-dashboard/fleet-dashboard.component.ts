import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TelemetryService } from '../telemetry.service';

@Component({
  selector: 'app-fleet-dashboard',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div style="background:#0a0a0f;color:#fff;padding:20px;font-family:monospace;min-height:100vh">
      <h2>🛰️ STARLINK FLEET - {{telemetry?.antennas?.length || 50}} NODES | AVG: {{telemetry?.avg_latency | number:'1.0-0'}}ms</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fill,120px);gap:10px;margin-top:20px">
        <div *ngFor="let ant of telemetry?.antennas"
             [style.border-color]="ant.status==='online'?'#00ff88':'#ffaa00'"
             style="padding:10px;border:1px solid #333;border-radius:8px;background:#111">
          <b>{{ant.id}}</b><br><small>{{ant.region}}</small><br>{{ant.latency | number:'1.0-0'}}ms<br>
          <span [style.color]="ant.status==='online'?'#00ff88':'#ffaa00'">{{ant.status}}</span>
        </div>
      </div>
    </div>
  `
})
export class FleetDashboardComponent implements OnInit {
  telemetry: any = { antennas: [], avg_latency: 0 };
  constructor(private telem: TelemetryService){}
  ngOnInit(){
    this.telem.getTelemetry().subscribe((data: any) => {
      this.telemetry = data;
    });
  }
}