// src/app/app.component.ts
import { Component } from '@angular/core';
import { QueryService } from './service/query.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: false
})
export class AppComponent {
  queryText: string = '';
  response: string = '';
  loading: boolean = false;

  constructor(private queryService: QueryService) { }

  setPredefinedQuery(query: string): void {
    this.queryText = query;
  }

  executeQuery(): void {
    if (!this.queryText) return;
    this.loading = true;
    this.response = '';

    this.queryService.submitQuery(this.queryText).subscribe({
      next: (res: string) => {
        this.response = res;
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.response = 'Error al procesar la consulta';
        this.loading = false;
      }
    });
  }
}
