from rest_framework.routers import DefaultRouter
from .views import Memberviewset

router = DefaultRouter()

router.register("members", Memberviewset)

urlpatterns = router.urls