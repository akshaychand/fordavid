import * as fromStatic from '../../static';

import { RouterModule, Routes } from '@angular/router';

import { NgModule } from '@angular/core';

const routes: Routes = [
    { path: '', redirectTo: 'landing', pathMatch: 'full' },
    {
        path: 'landing',
        component: fromStatic.LandingComponent,
        data: {
            title: 'Home'
        }
    },
    {
        path: 'login',
        component: fromStatic.LoginComponent,
        data: {
            title: 'Login'
        }
    },
    {
        path: 'forgot',
        component: fromStatic.ForgotComponent,
        data: {
            title: 'Forgot Password'
        }
    },
    {
        path: 'register',
        component: fromStatic.RegisterComponent,
        data: {
            title: 'Sign up'
        }
    },
    {
        path: '**',
        component: fromStatic.NotFoundComponent,
        data: {
            title: 'Page not found'
        }
    },
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class PublicLayoutRoutingModule {}
