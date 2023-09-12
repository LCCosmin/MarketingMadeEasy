import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import * as $ from 'jquery';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(private router: Router, private http: HttpClient, private toastr: ToastrService){}
  login(data: any){
    if(!data.username && !data.password){
      $('input[type="text"]').trigger('focus').trigger('invalid');
      $('input[type="password"]').trigger('focus').trigger('invalid');
      this.toastr.error('Va rugam completati username-ul si parola!', undefined,{
        positionClass: 'toast-top-center',
      });
    }else if(!data.username && data.password){
      $('input[type="text"]').trigger('focus').trigger('invalid');
      this.toastr.error('Va rugam sa completati username-ul!', undefined,{
        positionClass: 'toast-top-center',
      });
    }else if(data.username && !data.password){
      $('input[type="password"]').trigger('focus').trigger('invalid');
      this.toastr.error('Va rugam sa completati parola!', undefined, {
        positionClass: 'toast-top-center',
      });
    }else{
      this.router.navigate(['/client/dashboard']);
      this.toastr.success('V-ati logat cu success!', undefined, {
        positionClass: 'toast-top-center',
      });
    }
    console.log(data);

    // this.http.post("http://localhost:8000/api/debug_api", data).subscribe(r => console.log(r));
  }
}
