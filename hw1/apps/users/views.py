from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer

import logging

logger = logging.getLogger('users')

class RegisterViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
