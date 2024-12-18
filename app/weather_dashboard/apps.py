from django.apps import AppConfig


class WeatherDashboardConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "weather_dashboard"

    def ready(self):
        import weather_dashboard.signals

