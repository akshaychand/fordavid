import { IHttp } from './IHttp';

export class MockHttp implements IHttp {

    getServerUrl(): string {
        throw new Error('Method not implemented.');
    }

}
