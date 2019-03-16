import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-alliance-card',
  templateUrl: './alliance-card.component.html',
  styleUrls: ['./alliance-card.component.scss']
})
export class AllianceCardComponent implements OnInit {

  @Input() alliance: object;
  @Input() match_key: string;
  @Input() color: string;

  constructor() { }

  ngOnInit() {
  }

}
