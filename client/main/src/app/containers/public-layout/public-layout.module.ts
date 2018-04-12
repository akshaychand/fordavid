import * as fromStatic from './../../static';

import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { PublicLayoutRoutingModule } from './public-layout.routing.module';

export const STATIC_COMPONENTS = [
    fromStatic.LandingComponent,
    fromStatic.RegisterComponent,
    fromStatic.LoginComponent,
    fromStatic.ForgotComponent,
    fromStatic.NotFoundComponent,
    fromStatic.ErrorComponent
];

@NgModule({
    declarations: [
        ...STATIC_COMPONENTS
    ],
    imports: [
        CommonModule,
        PublicLayoutRoutingModule
    ],
    exports: [
    ],
    providers: [],
})
export class PublicLayoutModule {}
