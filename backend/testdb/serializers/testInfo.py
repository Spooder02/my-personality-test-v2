from rest_framework import serializers

from testDB.models import testInfo


class testInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = testInfo
        fields = ['title', 'description', 'author', 'created_at']