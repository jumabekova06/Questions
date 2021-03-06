# Generated by Django 3.2.8 on 2021-10-19 18:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_id', models.CharField(max_length=32)),
                ('text', models.TextField(max_length=2048)),
                ('type_question', models.CharField(choices=[('text_field', 'Ответ текстом'), ('single', 'Один вариант'), ('check_boxes', 'Выбор нескольких вариантов')], max_length=50, verbose_name='Type question')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('date_started', models.DateField(default=datetime.datetime.now)),
                ('date_ended', models.DateField(null=True)),
                ('description', models.TextField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_name', models.CharField(max_length=200)),
                ('choice_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_id', models.CharField(max_length=32)),
                ('text', models.TextField(max_length=2048)),
                ('self_text', models.TextField(null=True)),
                ('many_choice', models.ManyToManyField(to='polls.ChoiceModel')),
                ('one_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers_one_choice', to='polls.choicemodel')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.quiz')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
