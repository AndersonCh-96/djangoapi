from rest_framework import serializers
from .models import Project

# convierte un modelo en datos que pueden ser consultadas


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # definimos los campos que deseamos ser consultados por nuestra api
        fields = ("id", "title", "description", "technology", "created_at")
        ##indicamos los campos que solo queremos que sean 'unicamente de lectura
        read_only_fields = ("created_at",)
