"""Provides exceptions relevant to the django-directed package."""


class NodeNotReachableError(Exception):
    """Used when a node is not reachable in a path query."""

    pass


class GraphModelsCannotBeParsedError(Exception):
    """Used when there is some issue using the set of Graph, Node, and Edge models together."""

    pass


class IncorrectInputTypeError(Exception):
    """Exception when an input value if the wrong type."""

    pass


class IncorrectQuerySetTypeError(Exception):
    """Used when the QuerySet is not of the type expected."""

    pass


class AppNotInstalledError(Exception):
    """Used when refering to an application that is not yet installed."""

    pass


class ServiceDoesNotExistError(Exception):
    """Used when refering to an application that is not yet installed."""

    pass
