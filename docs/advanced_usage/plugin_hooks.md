# Plugin Hooks

django-directed plugins use [pluggy](https://pluggy.readthedocs.io/en/stable/) plugin hooks to customize behavior.

Each plugin can implement one or more hooks using the @hookimpl decorator against a function matching one of the hooks documented on this page.

When you implement a plugin hook, your implementation can accept any or all of the parameters that are documented below as parameters for that hook.

Work In Progress
