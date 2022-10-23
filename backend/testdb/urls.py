from testDB.views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from testDB.views import *

router = DefaultRouter()
router.register(r'testInfo', testInfoModelViewSet)

urlpatterns = [
    path('status_check/', status_check),
    path('', include(router.urls)),
]
