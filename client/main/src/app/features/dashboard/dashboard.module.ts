import * as fromComponents from './components';
import * as fromContainers from './containers';
import * as fromShared from './../../shared';

import { CommonModule } from '@angular/common';
import { DashboardRoutingModule } from './dashboard-routing.module';
import { NgModule } from '@angular/core';

export const FEATURE_CONTAINERS = [
    fromContainers.DashboardContainerComponent
];

export const FEATURE_COMPONENTS = [
    fromComponents.DashboardComponent
];

export const FEATURE_PROVIDERS = [
];

export const FEATURE_GUARDS = [

];

@NgModule({
    declarations: [
        ...FEATURE_CONTAINERS,
        ...FEATURE_COMPONENTS
    ],
    imports: [
        CommonModule,

        fromShared.SharedModule,
        fromShared.MaterialModule,

        DashboardRoutingModule
    ],
    exports: [
        ...FEATURE_CONTAINERS,
        ...FEATURE_COMPONENTS
    ],
    providers: [
        ...FEATURE_PROVIDERS,
        ...FEATURE_GUARDS
    ],
})
export class DashboardModule {}
