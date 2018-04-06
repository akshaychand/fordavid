import { CommonModule } from '@angular/common';
import { MomentModule } from 'angular2-moment';
import { NgModule } from '@angular/core';

export const THIRD_PARTY_MODULES = [
    MomentModule
];

@NgModule({
    declarations: [],
    imports: [
        CommonModule,

        ...THIRD_PARTY_MODULES
    ],
    exports: [],
    providers: [],
})
export class SharedModule {

}
