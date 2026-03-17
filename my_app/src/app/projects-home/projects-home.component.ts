import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-projects-home',
  standalone: true,
  imports: [],
  templateUrl: './projects-home.component.html',
  styleUrl: './projects-home.component.css'
})
export class ProjectsHomeComponent implements OnInit {
  firstName: string = "Dylan";
  lastName: string = "Utsler"
  phoneNumber: string = "720-297-0078";

  setProperty(event: Event) {
    let target = event.target as HTMLInputElement;
    let property: string = target.id
    switch(property) {
      case "firstNameInput":
        this.firstName = target.value;
        break;
        case "lastNameInput":
          this.lastName = target.value;
          break; 
          case "phoneNumberInput":
            this.phoneNumber = target.value;
            break;
            default:
              console.warn("No matching ID found");
              break;
    }
  }
  constructor() { }

  ngOnInit(): void {
    
  }
}
