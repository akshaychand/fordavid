import * as fromComponents from './components';
import * as fromMaterial from './../../shared/material.module';

import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

export const TOOLBOX_COMPONENTS = [
    fromComponents.ToolboxComponent
];

@NgModule({
    declarations: [
        ...TOOLBOX_COMPONENTS
    ],
    imports: [
        CommonModule,
        fromMaterial.MaterialModule
    ],
    exports: [
        ...TOOLBOX_COMPONENTS
    ],
    providers: [],
})
export class ToolboxModule {}
