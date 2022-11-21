from crm_app.views import (
    ContractViewSet,
    CustomerViewSet,
    ProspectViewSet,
    RegisterViewSet,
)
from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register(r"register", RegisterViewSet, basename="register")
router.register(r"customers", CustomerViewSet, basename="customers")
router.register(r"prospects", ProspectViewSet, basename="prospects")
router.register(r"contracts", ContractViewSet, basename="contracts")

customers_router = routers.NestedSimpleRouter(router, r"customers", lookup="customer")

prospects_router = routers.NestedSimpleRouter(router, r"prospects", lookup="prospect")

contracts_router = routers.NestedSimpleRouter(router, r"contracts", lookup="contract")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/login/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("auth/login/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("api/", include(router.urls)),
    path("api/", include(customers_router.urls)),
    path("api/", include(prospects_router.urls)),
    path("api/", include(contracts_router.urls)),
]
