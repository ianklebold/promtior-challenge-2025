// src/app/query.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environment';

export interface SubmitQueryRequest {
  query_text: string;
}

@Injectable({
  providedIn: 'root'
})
export class QueryService {

  // Configura el API URL en los environment files
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  submitQuery(query: string): Observable<string> {
    const payload: SubmitQueryRequest = { query_text: query };
    return this.http.post<string>(`${this.apiUrl}/submit_query`, payload);
  }
}
