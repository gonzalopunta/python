import { Injectable } from '@angular/core';
import { LoginDto } from '../dto/login.dto';
import { LoginResponse } from '../models/login-response.interface';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

const LOGIN_URL = 'localhost/4200/inicio';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  login(loginDto: LoginDto): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(
      LOGIN_URL,
      loginDto,
      httpOptions
    );
  }
}
