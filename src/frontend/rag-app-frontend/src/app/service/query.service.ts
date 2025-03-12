import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environment';

@Injectable({
  providedIn: 'root'
})
export class QueryService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  submitQuery(query: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/submit_query`, { query_text: query });
  }
}
