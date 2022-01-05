from django.urls import path
from collection.views.webviews import IndexView
from collection.views.apiviews import AuthorAPI

urlpatterns = [
    path('', IndexView.as_view()),
    path('api/author/', AuthorAPI.as_view()),
]
