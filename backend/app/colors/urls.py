from django.urls import path

from colors.views import RenderColorSwatches

app_name = "probability"

urlpatterns = [
    path(r"get-colors/", RenderColorSwatches.as_view()),
]
