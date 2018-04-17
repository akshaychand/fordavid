import { ChangeDetectorRef, Component, OnDestroy, OnInit } from '@angular/core';

import { MediaMatcher } from '@angular/cdk/layout';

@Component({
    templateUrl: './private-layout.component.html',
    styleUrls: ['./private-layout.component.scss']
})
export class PrivateLayoutComponent implements OnInit, OnDestroy {

    public menuOpened: boolean;
    public mobileQuery: MediaQueryList;
    private _mobileQueryListener: () => void;

    public title = 'FOOBAR'; // 'Loan Viz.\xAE';

    constructor(changeDetectorRef: ChangeDetectorRef, media: MediaMatcher) {
        this.mobileQuery = media.matchMedia('(max-width: 600px)');
        this._mobileQueryListener = () => changeDetectorRef.detectChanges();
        this.mobileQuery.addListener(this._mobileQueryListener);
    }

    ngOnInit(): void { }

    ngOnDestroy(): void {
        this.mobileQuery.removeListener(this._mobileQueryListener);
    }

}
