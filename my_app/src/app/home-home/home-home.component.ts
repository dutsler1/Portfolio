import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home-home',
  standalone: true,
  imports: [],
  templateUrl: './home-home.component.html',
  styleUrl: './home-home.component.css'
})
export class HomeHomeComponent implements OnInit {
  personname = "Dylan Utsler";
  personaddress = "5108 Miriam Lane";
  personcity = "Parker";
  personstate = "Colorado";
  personzip = "80134";
  personphone = "720-297-0078";
  personemail = "Dutsler1@gmail.com";
  summary = "Skilled at problem solving, critical thinking, and working in fast-paced environments where accuracy and accountability are essential. Experienced in leadership and process improvement, with a strong foundation in programming and software development concepts.Eager to contribute to a development team and grow as a software engineer.";
  school1 = "Western Governors University";
  school1Dates = "2024 - present";
  experience1 = "United States Marine Corps (Artillery)";
  experience1Dates = "2014-2018";
  experience2 = "Store manager for Grease Monkey";
  experience2Dates = "2018-2023";
  experience3 = "Deputy Sheriff at Arapahoe County Sheriffs office";
  experience3Dates = "2023-present";
  constructor() { }
  ngOnInit(): void {
    
  }

}
