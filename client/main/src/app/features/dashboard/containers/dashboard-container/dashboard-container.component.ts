import * as fromDataTables from './../../../../models/datatable';

import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'dashboard-container',
    templateUrl: './dashboard-container.component.html',
    styleUrls: ['./dashboard-container.component.scss']
})
export class DashboardContainerComponent implements OnInit {

    public options: fromDataTables.IDataTableOptions;

    constructor() { }

    ngOnInit(): void { }
}
