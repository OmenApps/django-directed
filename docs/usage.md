# Usage

To use django-directed in a project, add it to your `INSTALLED_APPS`:

``` python
INSTALLED_APPS = (
    ...
    'django_directed.apps.DjangoDirectedConfig',
    ...
)
```

Add django-directed's URL patterns:

``` python
from django_directed import urls as django_directed_urls


urlpatterns = [
    ...
    url(r'^', include(django_directed_urls)),
    ...
]
```