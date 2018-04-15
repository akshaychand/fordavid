import * as fromComponents from './components';

import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

export const SIDEBAR_COMPONENTS = [
    fromComponents.SideNavComponent
];

@NgModule({
    declarations: [
        ...SIDEBAR_COMPONENTS
    ],
    imports: [ CommonModule ],
    exports: [
        ...SIDEBAR_COMPONENTS
    ],
    providers: [],
})
export class SideNavModule {}
