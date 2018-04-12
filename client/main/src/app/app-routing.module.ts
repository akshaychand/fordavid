import * as fromStatic from './static';

import { RouterModule, Routes } from '@angular/router';

import { NgModule } from '@angular/core';

const routes: Routes = [
    { path: '', redirectTo: 'app', pathMatch: 'full'},
    {
        path: 'app',
        loadChildren: 'app/containers/private-layout/private-layout.module#PrivateLayoutModule'
    },
    {
        path: 'public',
        loadChildren:  'app/containers/public-layout/public-layout.module#PublicLayoutModule'
    }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {}
