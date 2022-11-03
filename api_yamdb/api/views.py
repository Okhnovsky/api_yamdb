from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import permissions

from reviews.models import Comment, Review, Title
from .serializers import CommentSerializer, ReviewSerializer
from .permissons import IsAuthorOrModeratorOrAdminOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(
            title=title,
            author=self.request.user,
        )


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthorOrModeratorOrAdminOrReadOnly,)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(
            review=review,
            author=self.request.user,
        )
