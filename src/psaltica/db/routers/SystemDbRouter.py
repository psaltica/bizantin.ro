class SystemDbRouter:
    """
    A router to control all database operations on models in the system
    applications.
    """

    db = 'default'
    apps = [
        'admin',
        'auth',
        'contenttypes',
        'sessions',
        'messages',
        'staticfiles'
    ]

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.apps:
            return self.db
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.apps:
            return self.db
        return None

    def allow_relations(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.apps and
            obj1._meta.app_label in self.apps
        ):
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.apps:
            return db == self.db
        return None