import {
    DxDataGridModule,
    DxTreeListModule
} from 'devextreme-angular';

import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

export const FEATURE_MODULES = [
    DxDataGridModule,
    DxTreeListModule
];

@NgModule({
    declarations: [],
    imports: [
        CommonModule,
        ...FEATURE_MODULES
    ],
    exports: [
        ...FEATURE_MODULES
    ],
    providers: [],
})
export class DevExtremeModule {}
