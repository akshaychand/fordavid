import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class DataTableService {

    constructor(public httpClient: HttpClient) { }

    public fetchData<T>(url: string): Observable<T[]> {
        return this.httpClient
            .get<T[]>(url)
            .pipe();
    }

    public postData<T>(url: string, payload: T): Observable<T> {
        return this.httpClient
            .post<T>(url, payload)
            .pipe();
    }

    public updateData<T>(url: string, payload: T): Observable<T> {
        return this.httpClient
            .put<T>(url, payload)
            .pipe();
    }

    public deleteData<T>(url: string, payload: T): Observable<T> {
        return this.httpClient
            .delete<T>(url, payload)
            .pipe();
    }

    public patchData<T>(url: string, payload: T): Observable<T> {
        return this.httpClient
            .patch<T>(url, payload)
            .pipe();
    }

}
