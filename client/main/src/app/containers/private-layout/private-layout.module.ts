import * as fromShared from './../../shared';

import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { PrivateLayoutComponent } from './private-layout.component';
import { PrivateLayoutRoutingModule } from './private-layout.routing.module';

@NgModule({
    declarations: [
        PrivateLayoutComponent
    ],
    imports: [
        CommonModule,

        fromShared.MaterialModule,
        fromShared.SharedModule,

        PrivateLayoutRoutingModule
    ],
    exports: [],
    providers: [],
})
export class PrivateLayoutModule {}
