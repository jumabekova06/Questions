from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from polls.models import Quiz, Answer
from polls.serializers import QuizSerializer, AnswerSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer

class SurveyAPIView(APIView):
    
    def get(self, request):
        survey = Quiz.objects.all()
        serializers = QuizSerializer(survey, many=True)
        return Response(serializers.data)



class QuestionAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        question = Question.objects.all()
        serializers = QuestionSerializer(question, many=True)
        return Response(serializers.data)


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class AnswerViewSet(ModelViewSet,
                    CreateModelMixin,
                    GenericAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = (DjangoFilterBackend,)
    http_method_names = ('get', 'post')

    # def perform_create(self, serializer):
    #     if self.request.user_id.is_authenticated:
    #         return serializer.save(user_id=self.request.user_id)
    #     return super().perform_create(serializer)
