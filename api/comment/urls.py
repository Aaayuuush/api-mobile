from django.urls import path

from api.comment.views import CommentCreateView, CommentRetrieveUpdateDestroyView

url_patterns = [
    path("", CommentCreateView.as_view()),
    path("<uuid:uuid>/", CommentRetrieveUpdateDestroyView.as_view(lookup_field="uuid")),
    path("<int:pk>/", CommentRetrieveUpdateDestroyView.as_view()),
]