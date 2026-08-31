import { Component } from '@angular/core';
import { FleetDashboardComponent } from './fleet-dashboard/fleet-dashboard.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FleetDashboardComponent],
  template: `<app-fleet-dashboard />`,
  styles: []
})
export class AppComponent {
  title = 'starlink-monitor';
}