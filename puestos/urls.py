from rest_framework.routers import DefaultRouter

from puestos.views import PuestosViewSet

router = DefaultRouter()
router.register(r'', PuestosViewSet)

urlpatterns = router.urls
