from flask_sqlalchemy import Pagination

from server.core.globals import db


class ModelService(object):
    """
    A :class:`Service` instance encapsulates common SQLAlchemy model operations in the context of a :class:`Flask`
    application.
    """
    __model__ = None
    __bind__ = None
    __default_order_by__ = None

    def add(self, model):
        """
        Adds the instance of the model to the database session, but does not commit (unless autocommit feature is
        enabled) in SQLAlchemy
        :param model: instance of the model
        """
        self._isinstance(model)
        db.session.add(model)
        return model

    def save(self, model):
        """
        Adds the instance of the model to the database and commits the transaction.
        :param model: instance of the model
        """
        self._isinstance(model)
        db.session.add(model)
        db.session.commit()
        return model

    def upsert(self, model):
        """
        Inserts/Updates the model to the database and commits the transaction.
        :param model: instance of the model
        """
        self._isinstance(model)
        db.session.merge(model)
        db.session.commit()
        return model

    def all(self):
        """
        Returns a generator containing all instances of the service's model.
        """
        return self.__model__.query.all()

    def get(self, id):
        """
        Returns an instance of the service's model with the specified id. Returns `None` if an instance with the
        specified id does not exist.
        :param id: the instance id
        """
        return self.__model__.query.get(id)

    def get_by_ids(self, *ids):
        """
        Returns a list of instances of the model for the specified ids.
        :param ids: list of ids to retrieve from the server
        """
        return self.__model__.query.filter(self.__model__.id.in_(ids)).all()

    def find(self, **kwargs):
        """
        Returns a list of instances of the service's model filtered by the specified key word arguments.
        :param kwargs: filter parameters
        """
        return self.__model__.query.filter_by(**kwargs)

    def first(self, **kwargs):
        """
        Returns the first instance found of the service's model filtered by the specified key word arguments.
        :param kwargs: filter parameters
        """
        return self.find(**kwargs).first()

    def get_or_404(self, id):
        """
        Returns an instance of the service's model with the specified id or raises an 404 error if an instance with
        the specified id does not exist.
        :param id: the instance id
        """
        return self.__model__.query.get_or_404(id)

    # CRUD operations

    def new(self, **kwargs):
        """
        Returns a new, unsaved instance of the service's model class. It does not persist the instance to the database.
        :param kwargs: instance parameters
        """
        return self.__model__(**self._preprocess_params(kwargs))

    def create(self, **kwargs):
        """
        Returns a new, saved instance of the service's model class.
        :param kwargs: instance parameters
        """
        return self.save(self.new(**kwargs))

    def update(self, model, **kwargs):
        """
        Returns an updated instance of the service's model class. Can be used for performing partial updates to an
        instance of the object.
        :param model: the model to update
        :param kwargs: update parameters
        """
        self._isinstance(model)
        for k, v in self._preprocess_params(kwargs).items():
            setattr(model, k, v)
        self.save(model)
        return model

    def delete(self, model):
        """
        Immediately deletes the specified model instance.
        :param model: instance of the model to delete
        """
        self._isinstance(model)
        db.session.delete(model)
        db.session.commit()
        return model

    def bulk_insert(self, models):
        for model in models:
            self._isinstance(model)
        db.session.bulk_save_objects(models)
        db.session.commit()

    def bulk_delete(self, key, values):
        table_name = getattr(self.__model__, '__tablename__')
        values_to_in_clause = ",".join(["'{0}'".format(val) for val in values])
        sql = 'DELETE T FROM [{0}] T WHERE [{1}] IN ({2})'.format(table_name, key, values_to_in_clause)
        db.session.execute(sql)
        db.session.commit()

    # Read operations

    def page(self, select=None, filters=None, order_by=None, page=1, limit=100, page_size=20, **kwargs):
        """
        Performs paginated operations on the model such as
        :param select:
        :param filters:
        :param order_by:
        :param page:
        :param limit:
        :param page_size:
        :return:
        """
        if page <= 0:
            raise ValueError('Page number cannot be less than 1!')

        if order_by is None:
            order_by = self.__default_order_by__

        # filter_by = dict()
        # if len(filters > 0):
        #     filter_by = self.prepare_filters(filter)

        items = self.__model__.query.filter_by(**kwargs).order_by(order_by).limit(limit).offset((page-1)*page_size).all()

        if page == 1 and len(items) < page_size:
            total = len(items)
        else:
            total = self.__model__.query.order_by(None).count()

        return Pagination(self.__model__.query, page, page_size, total, items)

    # Helper methods

    def _isinstance(self, model, raise_error=True):
        """
        Checks if the specified model instance matches the service's model.
        By default this method will raise a `ValueError` if the model is not the
        expected type.
        :param model: the model instance to check
        :param raise_error: flag to raise an error on a mismatch
        """
        rv = isinstance(model, self.__model__)
        if not rv and raise_error:
            raise ValueError('%s is not of type %s' % (model, self.__model__))
        return rv

    @staticmethod
    def _preprocess_params(kwargs):
        """
        Returns a preprocessed dictionary of parameters. Used by default
        before creating a new instance or updating an existing instance.
        :param kwargs: a dictionary of parameters
        """
        kwargs.pop('csrf_token', None)
        return kwargs


class SQLService(object):

    def __init__(self, bind=None):
        self.bind = bind
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
