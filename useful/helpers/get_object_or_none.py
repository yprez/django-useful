def get_object_or_none(model, *args, **kwargs):
    """
    Like get_object_or_404, but doesn't throw an exception.

    Allows querying for an object that might not exist without triggering
    an exception.
    """
    try:
        return model._default_manager.get(*args, **kwargs)
    except model.DoesNotExist:
        return None
