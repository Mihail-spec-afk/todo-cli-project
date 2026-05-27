class TodoError(Exception): pass
class TaskNotFoundError(TodoError): pass
class StorageError(TodoError): pass
