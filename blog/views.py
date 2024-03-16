from rest_framework import permissions, viewsets
from .models import Post
from .serializers import PostReadSerializer, PostWriteSerializer
from .permissions import IsAuthorOrReadOnly
#Blog Views

class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD posts
    """
    queryset = Post.objects.all()
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return PostWriteSerializer

        return PostReadSerializer

    # get_permissions(self) method helps you separate
    # permissions for different actions inside the same view.
    def get_permissions(self):
        if self.action in ("create",):
            self.permission_classes = (permissions.IsAuthenticated,)
        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = (IsAuthorOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()
