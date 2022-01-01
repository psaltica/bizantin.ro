class PsalticaDbRouter:
    """
    A router to control all database operations on models accross all
    applications. It allocates apps and models to databases in a 1-to-1 fashion
    with the exception of the contenttypes app which is required by both the
    system apps (auth, admin, etc.) and the collection app.
    """

    def _default_routing(instance=None):
        return 'default'

    def _content_routing(instance=None):
        return 'content'

    def _contenttypes_routing(instance=None):
        if instance is not None:
            if instance.app_label == 'collection':
                return 'content'
            else:
                return 'default'
        else:
            return None

    mapping = {
        'admin': _default_routing,
        'auth': _default_routing,
        'collection': _content_routing,
        'contenttypes': _contenttypes_routing,
        'session': _default_routing,
    }

    def db_for_read(self, model, **hints):
        app_label = model._meta.app_label
        instance = hints['instance'] if 'instance' in hints else None
        if app_label in self.mapping.keys():
            return self.mapping[app_label](instance)
        return None

    def db_for_write(self, model, **hints):
        app_label = model._meta.app_label
        instance = hints['instance'] if 'instance' in hints else None
        if app_label in self.mapping.keys():
            return self.mapping[app_label](instance)
        return None

    def allow_relations(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.mapping.keys() and
            obj2._meta.app_label in self.mapping.keys()
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.mapping.keys():
            choice = self.mapping[app_label]()

            if choice is None:
                return True
            else:
                return db == choice

        return None
