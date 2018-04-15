import * as fromComponents from './components';
import * as fromMaterial from './../../shared/material.module';

import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

export const NAVBAR_COMPONENTS = [
    fromComponents.NavbarComponent
];

@NgModule({
    declarations: [
        ...NAVBAR_COMPONENTS
    ],
    imports: [
        CommonModule,
        fromMaterial.MaterialModule
    ],
    exports: [
        ...NAVBAR_COMPONENTS
    ],
    providers: [],
})
export class NavbarModule {}
