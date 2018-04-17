import * as fromSharedModules from './../components';

import { AgGridModule } from 'ag-grid-angular';
import { CommonModule } from '@angular/common';
import { MomentModule } from 'angular2-moment';
import { NgModule } from '@angular/core';

export const SHARED_MODULES = [

    // Navigation
    fromSharedModules.SideNavModule,
    fromSharedModules.NavbarModule,
    fromSharedModules.ToolboxModule,

    // Charting + Data
    fromSharedModules.ChartingModule,
    fromSharedModules.DataTableModule
];

export const THIRD_PARTY_MODULES = [
    MomentModule,
    AgGridModule.withComponents([])
];

@NgModule({
    declarations: [],
    imports: [
        CommonModule,

        ...SHARED_MODULES,

        ...THIRD_PARTY_MODULES
    ],
    exports: [
        ...SHARED_MODULES,

        MomentModule,
        AgGridModule
    ],
    providers: [],
})
export class SharedModule {

}
