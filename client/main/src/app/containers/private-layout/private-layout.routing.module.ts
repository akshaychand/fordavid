import { RouterModule, Routes } from '@angular/router';

import { NgModule } from '@angular/core';
import { PrivateLayoutComponent } from './private-layout.component';

const routes: Routes = [
    {
        path: '',
        component: PrivateLayoutComponent,
        children: [
            { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
            {
                path: 'dashboard',
                loadChildren: 'app/features/dashboard/dashboard.module#DashboardModule',
                data: {
                    title: 'Dashboard'
                }
            }
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class PrivateLayoutRoutingModule {}
