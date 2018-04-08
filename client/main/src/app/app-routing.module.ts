import * as fromStatic from './static';

import { RouterModule, Routes } from '@angular/router';

import { NgModule } from '@angular/core';

const routes: Routes = [
    { path: 'login', component: fromStatic.LoginComponent },
    { path: 'forgot', component: fromStatic.ForgotComponent },
    { path: 'register', component: fromStatic.RegisterComponent },
    { path: '**', component: fromStatic.NotFoundComponent },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {}
