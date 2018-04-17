import * as fromModels from './../../../../models/datatable';

import { Action } from '@ngrx/store';

/**
 * For each action type in an action group, make a simple
 * enum object for all of this group's action types.
 */
export enum DataTableActionTypes {
    LOAD_ENTITIES = '[DataTable] Load entities',
    LOAD_ENTITIES_COMPLETE = '[DataTable] Load entities complete',
    LOAD_ENTITIES_FAILED = '[DataTable] Load entities failed',
    ADD_ENTITY = '[DataTable] Add entity',
    ADD_ENTITY_COMPLETE = '[DataTable] Add entity complete',
    ADD_ENTITY_FAILED = '[DataTable] Add entity failed',
    ADD_ENTITIES = '[DataTable] Add entities',
    ADD_ENTITIES_COMPLETE = '[DataTable] Add entities complete',
    ADD_ENTITIES_FAILED = '[DataTable] Add entities failed',
    UPSERT_ENTITY = '[DataTable] Update or add entity',
    UPSERT_ENTITY_COMPLETE = '[DataTable] Update or add entity complete',
    UPSERT_ENTITY_FAILED = '[DataTable] Update or add entity failed',
    UPSERT_ENTITIES = '[DataTable] Update or add entities',
    UPSERT_ENTITIES_COMPLETE = '[DataTable] Update or add entities complete',
    UPSERT_ENTITIES_FAILED = '[DataTable] Update or add entities failed',
    DELETE_ENTITY = '[DataTable] Delete entity',
    DELETE_ENTITY_COMPLETE = '[DataTable] Delete entity complete',
    DELETE_ENTITY_FAILED = '[DataTable] Delete entity failed',
    DELETE_ENTITIES = '[DataTable] Delete entities',
    DELETE_ENTITIES_COMPLETE = '[DataTable] Delete entities complete',
    DELETE_ENTITIES_FAILED = '[DataTable] Delete entities failed'
}

/**
 * Every action is comprised of at least a type and an optional
 * payload. Expressing actions as classes enables powerful
 * type checking in reducer functions.
 */
export class LoadEntities<T extends fromModels.IEntity> implements Action {
    readonly type = DataTableActionTypes.LOAD_ENTITIES;

    constructor(public payload: fromModels.IDataSource<T>) { }
}

export class LoadEntitiesComplete<T extends fromModels.IEntity> implements Action {
    readonly type = DataTableActionTypes.LOAD_ENTITIES_COMPLETE;

    constructor(public payload: fromModels.IDataTable<T>) { }
}

export class LoadEntitiesFailed<T extends fromModels.IEntity> implements Action {
    readonly type = DataTableActionTypes.LOAD_ENTITIES_COMPLETE;

    constructor(public payload?: string) { }
}

/**
 * Export a type alias of all actions in this action group
 * so that reducers can easily compose action types
 */
export type DataTableActionsUnion<T extends fromModels.IEntity>
        = LoadEntities<T>
        | LoadEntitiesComplete<T>
        | LoadEntitiesFailed<T>;
