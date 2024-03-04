from projects.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

# definomos que consultas se pueden realziar


class ProjectViewSet(viewsets.ModelViewSet):
    # consulta todas las propiedades de una tabla
    queryset = Project.objects.all()
    #permisos que puedo relizar, tambien podemos usar el isAuth es decir verificar si esta autentificado
    permission_classes = [permissions.AllowAny]
    #convierte los datos a consultar
    serializer_class = ProjectSerializer
