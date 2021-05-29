from rest_framework import serializers

from .models import GradeInfo


class GradeInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = GradeInfo
        fields = '__all__'
