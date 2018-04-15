import {
    MatAutocompleteModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatCardModule,
    MatCheckboxModule,
    MatChipsModule,
    MatDatepickerModule,
    MatDialogModule,
    MatDividerModule,
    MatExpansionModule,
    MatFormFieldModule,
    MatGridListModule,
    MatIconModule,
    MatInputModule,
    MatListModule,
    MatMenuModule,
    MatPaginatorModule,
    MatProgressBarModule,
    MatProgressSpinnerModule,
    MatRadioModule,
    MatSelectModule,
    MatSidenavModule,
    MatSlideToggleModule,
    MatSliderModule,
    MatSnackBarModule,
    MatSortModule,
    MatStepperModule,
    MatTableModule,
    MatTabsModule,
    MatToolbarModule,
    MatTooltipModule,
} from '@angular/material';

import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

export const MATERIAL_MODULES = [
    // Menus
    MatMenuModule,
    MatSidenavModule,
    MatToolbarModule,

    // Layout
    MatCardModule,
    MatDividerModule,
    MatExpansionModule,
    MatGridListModule,
    MatListModule,
    MatStepperModule,
    MatTabsModule,

    // Icons
    MatIconModule,

    // Forms
    MatAutocompleteModule,
    MatCheckboxModule,
    MatDatepickerModule,
    MatFormFieldModule,
    MatInputModule,
    MatRadioModule,
    MatSelectModule,
    MatSliderModule,
    MatSlideToggleModule,

    // Buttons & Indicators
    MatButtonModule,
    MatButtonToggleModule,
    MatChipsModule,
    MatIconModule,
    MatProgressSpinnerModule,
    MatProgressBarModule,

    // Popups & Modals
    MatDialogModule,
    MatSnackBarModule,
    MatTooltipModule,

    // Data Grid
    MatPaginatorModule,
    MatSortModule,
    MatTableModule

];

@NgModule({
    declarations: [],
    imports: [
        ...MATERIAL_MODULES
    ],
    exports: [
        ...MATERIAL_MODULES
    ],
    providers: [],
})
export class MaterialModule {}
