import * as fromComponents from './components';

import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

export const CHART_COMPONENTS = [
    fromComponents.BarChartComponent,
    fromComponents.LineChartComponent,
    fromComponents.PieChartComponent
];

@NgModule({
    declarations: [
        ...CHART_COMPONENTS
    ],
    imports: [
        CommonModule
    ],
    exports: [
        ...CHART_COMPONENTS
    ],
    providers: [],
})
export class ChartingModule {}
