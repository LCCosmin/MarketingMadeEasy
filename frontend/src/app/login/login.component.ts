import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(private http: HttpClient){}
  login(data: any){
    console.log(data);
    this.http.post("http://localhost:8000/api/debug_api", data).subscribe(r => console.log(r));
  }
}
