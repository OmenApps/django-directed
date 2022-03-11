from django.apps import AppConfig
from django.contrib.auth import get_user_model


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tests.example.core"

    def ready(self) -> None:
        User = get_user_model()
        user_exists = User.objects.filter(username="admin", email="admin@example.com").exists()
        if not user_exists:
            User.objects.create_superuser("admin", "admin@example.com", "pass")
