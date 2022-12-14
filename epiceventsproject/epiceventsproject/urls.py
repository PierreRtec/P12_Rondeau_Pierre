from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from crm_app.views import (
    ContractViewSet,
    CustomerViewSet,
    CustomUserViewSet,
    EventViewSet,
    GroupViewSet,
)

router = routers.SimpleRouter()
router.register(r"customers", CustomerViewSet, basename="customers")
router.register(r"contracts", ContractViewSet, basename="contracts")
router.register(r"events", EventViewSet, basename="events")
router.register(r"users", CustomUserViewSet, basename="users")
router.register(r"groups", GroupViewSet, basename="group")

customers_router = routers.NestedSimpleRouter(router, r"customers", lookup="customer")
contracts_router = routers.NestedSimpleRouter(router, r"contracts", lookup="contract")
events_router = routers.NestedSimpleRouter(router, r"events", lookup="event")
custom_users_router = routers.NestedSimpleRouter(router, r"users", lookup="user")
groups_router = routers.NestedSimpleRouter(router, r"groups", lookup="group")


urlpatterns = [
    # admin management authentication url
    # required to create a superuser first
    path("management-admin/", admin.site.urls),
    # api auth
    path("api-auth/", include("rest_framework.urls")),
    path("auth/login/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("auth/login/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    # api routes
    path("api/", include(router.urls)),
    path("api/", include(customers_router.urls)),
    path("api/", include(contracts_router.urls)),
    path("api/", include(events_router.urls)),
    path("api/", include(custom_users_router.urls)),
    path("api/", include(groups_router.urls)),
]
