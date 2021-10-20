from rest_framework import serializers
from .models import Question, Quiz, ChoiceModel, Answer 
from django.db.models import Q

# QuestionModel, AnswerModel,

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'date_started', 'date_ended', 'description')
        model = Quiz


# варианты ответов
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ChoiceModel


# вопросы
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = 'id', 'quiz_id', 'question_id', 'text', 'many_choice', 'one_choice','user_id'
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation["user_id"] = UserSerializer(instance.user_id).data
    #     return representation


class QuestionListSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField('get_answers')

    class Meta:
        fields = ['text', 'answers']
        model = Question

    def get_answers(self, question):
        user_id = self.context.get('request').user.id
        answers = Answer.objects.filter(
            Q(question=question) & Q(user_id__id=user_id))
        serializer = AnswerSerializer(instance=answers, many=True)
        return serializer.data

