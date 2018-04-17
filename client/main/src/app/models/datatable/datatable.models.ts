export interface IEntity {
    id: number | string;
}

export interface IDataSource<T extends IEntity> extends IEntity {

    readUrl: string;
    insertUrl: string;
    updateUrl: string;
    deleteUrl: string;
}

export interface IDataTable<T extends IEntity> {
    columns: IColumn[];
    rows: T[];
}

export interface IColumn {
    name: string;
    caption: string;
    format: string;
    isCalculated: boolean;
    calculationCallback: any;

    childUrl: string;
    parentUrl: string;
}

export class DataSource<T extends IEntity> implements IEntity, IDataSource<T>  {
    id: string;

    readUrl: string;
    insertUrl: string;
    updateUrl: string;
    deleteUrl: string;

    constructor(options: IDataSource<T>) {
        this.readUrl = options.readUrl;
        this.insertUrl = options.insertUrl;
        this.updateUrl = options.updateUrl;
        this.deleteUrl = options.deleteUrl;
    }
}

export class DataTable<T extends IEntity> implements IEntity, IDataTable<T> {
    id: string;

    columns: IColumn[];
    rows: T[];

    constructor(options: IDataTable<T>) {
        this.columns = options.columns || [];
        this.rows = options.rows || [];
    }
}

export class Column implements IColumn {
    name: string;
    caption: string;
    format: string;
    isCalculated: boolean;
    calculationCallback: any;

    childUrl: string;
    parentUrl: string;

    constructor(options: IColumn) {
        this.name = options.name;
        this.caption = options.caption;
        this.format = options.format;
        this.childUrl = options.childUrl || null;
        this.parentUrl = options.parentUrl || null;

        this.isCalculated = options.isCalculated || false;
        this.calculationCallback = options.calculationCallback || null;
    }

}


export interface IDataTableOptions {
    allowExport: boolean;
    exportFileName: string;
}

export class DataTableOptions implements IDataTableOptions {
    allowExport: boolean;
    exportFileName: string;

    constructor(options?: IDataTableOptions) {
        this.allowExport = options && options.allowExport;
        this.exportFileName = options && options.exportFileName;

    }
}
