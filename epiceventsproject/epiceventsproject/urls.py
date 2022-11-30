from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from crm_app.views import (
    ContractViewSet,
    CustomerViewSet,
    EventViewSet,
)

router = routers.SimpleRouter()
router.register(r"customers", CustomerViewSet, basename="customers")
router.register(r"contracts", ContractViewSet, basename="contracts")
router.register(r"events", EventViewSet, basename="events")

customers_router = routers.NestedSimpleRouter(router, r"customers", lookup="customer")

contracts_router = routers.NestedSimpleRouter(router, r"contracts", lookup="contract")

events_router = routers.NestedSimpleRouter(router, r"events", lookup="event")


urlpatterns = [
    # admin management authentification url
    # required to create a super user first
    path("ee-admin/", admin.site.urls),
    # api auth
    path("api-auth/", include("rest_framework.urls")),
    path("auth/login/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("auth/login/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    # api
    path("api/", include(router.urls)),
    path("api/", include(customers_router.urls)),
    path("api/", include(contracts_router.urls)),
    path("api/", include(events_router.urls)),
]
