"""Provides exceptions relevant to the django-directed package."""


class NodeNotReachableException(Exception):
    """Used when a node is not reachable in a path query."""

    pass


class GraphModelsCannotBeParsedException(Exception):
    """Used when there is some issue using the set of Graph, Node, and Edge models together."""

    pass


class IncorrectInputTypeException(Exception):
    """Exception when an input value if the wrong type."""

    pass


class IncorrectQuerySetTypeException(Exception):
    """Used when the QuerySet is not of the type expected."""

    pass


class AppNotInstalledException(Exception):
    """Used when refering to an application that is not yet installed."""

    pass


class ServiceDoesNotExistException(Exception):
    """Used when refering to an application that is not yet installed."""

    pass
