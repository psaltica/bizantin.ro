from django.urls import path
from collection.views.webviews import IndexView
from collection.views.apiviews import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('api/authors/', AuthorAPI.as_view()),
    path('api/authors/<uuid:author_id>/', AuthorDetailAPI.as_view()),
    path('api/texts/', MusicalTextAPI.as_view()),
    path('api/texts/<uuid:text_id>/', MusicalTextDetailAPI.as_view()),
    path('api/publications/', PublicationAPI.as_view()),
    path('api/publications/<uuid:publication_id>/', PublicationDetailAPI.as_view()),
    path('api/performances/', PerformanceAPI.as_view()),
    path('api/performances/<uuid:performance_id>/', PerformanceDetailAPI.as_view()),
]
