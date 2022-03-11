from django.db import models


class BaseGraph(models.Model):
    """
    Base Graph Model lets us verify that a given model instance derives from BaseGraph
    """

    class Meta:
        abstract = True


class BaseEdge(models.Model):
    """
    Base Edge Model lets us verify that a given model instance derives from BaseEdge
    """

    class Meta:
        abstract = True


class BaseNode(models.Model):
    """
    Base Node Model lets us verify that a given model instance derives from BaseNode
    """

    class Meta:
        abstract = True
