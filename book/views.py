from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Book
from . import serializers
from .permissions import IsAuthor
from django.contrib.auth import get_user_model

User = get_user_model()


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookListSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsAuthor()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.save(status=self.request.user.email)
