from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField


class Quiz(models.Model):
    name = models.CharField(max_length=256)
    date_started = models.DateField(default=datetime.now)
    date_ended = models.DateField(null=True)
    description = models.TextField(max_length=512)

    def __str__(self):
        return self.name


QUESTION_TYPES = (
    ('text_field', 'Ответ текстом'),
    ('single', 'Один вариант'),
    ('check_boxes', 'Выбор нескольких вариантов'),
)


class Question(models.Model):
    quiz_id = models.ForeignKey(Quiz,on_delete=CASCADE,related_name='quuiz')
    text = models.TextField(max_length=2048)
    type_question = models.CharField(max_length=50, choices=QUESTION_TYPES,editable=False, verbose_name='Type question')

    def __str__(self):
        return self.text


class ChoiceModel(models.Model):
    choice_name = models.CharField(max_length=200)
    choice_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.choice_name


class Answer(models.Model):
    user_id = IntegerField()
    quiz_id = models.ForeignKey(Quiz,related_name='quiz_id',on_delete=CASCADE)
    question_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField(max_length=2048,blank=True)
    many_choice = models.ManyToManyField(ChoiceModel)
    one_choice = models.ForeignKey(
        ChoiceModel,
        null=True,
        on_delete=models.CASCADE,
        related_name="answers_one_choice"
    )
    self_text = models.TextField(null=True)

    def __str__(self):
        return self.self_text

# Create your models here.
