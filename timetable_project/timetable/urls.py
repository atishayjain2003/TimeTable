from rest_framework.routers import DefaultRouter
from .views import TimetableViewSet,StudentViewSet

router = DefaultRouter()
router.register(r'timetables', TimetableViewSet)
router.register(r'student', StudentViewSet)

urlpatterns = router.urls
