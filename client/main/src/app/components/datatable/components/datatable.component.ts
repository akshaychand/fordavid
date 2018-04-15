import * as fromModels from './../models';

import { ChangeDetectionStrategy, Component, Input, OnInit, Output } from '@angular/core';

@Component({
    selector: 'data-table',
    templateUrl: './datatable.component.html',
    styleUrls: ['./datatable.component.scss']
})
export class DataTableComponent<T extends fromModels.IEntity> implements OnInit {

    @Input() dataSource: fromModels.IDataSource<T>;
    @Input() data: fromModels.IDataTable<T>;

    constructor() { }

    ngOnInit(): void { }
}
