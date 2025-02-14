from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers

from .views import QuestionsViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="Questions API",
        default_version="v1",
        description="API for retrieving questions data",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kris6uu7@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


router = routers.DefaultRouter()
router.register("questions", QuestionsViewSet, basename="questions")


urlpatterns = [
    path("api/", include(router.urls)),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
