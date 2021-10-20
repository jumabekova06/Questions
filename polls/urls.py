from rest_framework.routers import DefaultRouter
from polls.views import AnswerViewSet, QuestionAPIView, SurveyAPIView
from django.conf.urls import url, include
from django.urls import path

router = DefaultRouter()
router.register(r'answer', AnswerViewSet)

urlpatterns = [
    url(r'^v1', include((router.urls, 'v1'), namespace='v1')),

    path('api/v1/survey/', SurveyAPIView.as_view()),
    path('question/', QuestionAPIView.as_view()),
]
