from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()

    def perform_update(self, serializer):
        if self.request.user.is_staff or self.request.user == serializer.instance:
            serializer.save()
        else:
            raise permissions.PermissionDenied("У вас нет прав редактировать этого пользователя.")
