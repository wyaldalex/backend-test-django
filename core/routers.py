class CoreDBRouter:
    def db_for_read(self, model, **hints):
        """
        Reads from core.
        """
        return 'core'

    def db_for_write(self, model, **hints):
        """
        Writes always go to core.
        """
        return 'core'

    def allow_relation(self, obj1, obj2, **hints):

        return True


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return False