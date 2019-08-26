from rest_framework import routers

from .viewsets import NoteViewSet
from .viewsets import UserViewSet

router = routers.DefaultRouter()
router.register('notes', NoteViewSet)
router.register('users', UserViewSet)

urlpatterns = router.urls