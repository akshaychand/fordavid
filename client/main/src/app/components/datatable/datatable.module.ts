import * as fromComponents from './components';
import * as fromServices from './services';

import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

export const DATA_TABLE_COMPONENTS = [
    fromComponents.DataTableComponent
];

export const DATA_TABLE_PROVIDERS = [
];

@NgModule({
    declarations: [
        ...DATA_TABLE_COMPONENTS
    ],
    imports: [ CommonModule ],
    exports: [
        ...DATA_TABLE_COMPONENTS
    ],
    providers: [
        ...DATA_TABLE_PROVIDERS
    ],
})
export class DataTableModule {}
