from rest_framework import viewsets

from testDB.models import testInfo
from testDB.serializers.testInfo import testInfoSerializer


class testInfoModelViewSet(viewsets.ModelViewSet):
    queryset = testInfo.objects.all()
    serializer_class = testInfoSerializer
