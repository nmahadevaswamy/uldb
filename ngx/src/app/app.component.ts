import { Component } from '@angular/core';
import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'ngx';
  
  userList: any= [];

  constructor (private Svc : AppService){
  }

  ngOnInit(){
    this.getdata()
  } 

  getdata(){

    this.Svc.getUser().subscribe(res => {
      // console.log(res, 'str')
      this.userList = res ;
    })
    // console.log(this.Svc.getUser())
  }

}
