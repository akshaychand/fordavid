import * as fromShared from './shared';
import * as fromStatic from './static';

import { BrowserModule, Title } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { NgModule } from '@angular/core';

export const STATIC_COMPONENTS = [
  fromStatic.RegisterComponent,
  fromStatic.LoginComponent,
  fromStatic.ForgotComponent,
  fromStatic.NotFoundComponent,
  fromStatic.ErrorComponent
];

@NgModule({
  declarations: [
    AppComponent,

    ...STATIC_COMPONENTS
  ],
  imports: [
    BrowserModule,

    fromShared.SharedModule
  ],
  providers: [
    Title
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
