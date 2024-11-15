from rest_framework.routers import DefaultRouter
from .views import TimetableViewSet

router = DefaultRouter()
# router.register(r'classes', ClassViewSet)
# router.register(r'subjects', SubjectViewSet)
# router.register(r'teachers', TeacherViewSet)
# router.register(r'timeslots', TimeslotViewSet)
router.register(r'timetables', TimetableViewSet)

urlpatterns = router.urls
