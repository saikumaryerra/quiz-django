# Generated by Django 2.2.3 on 2019-07-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizattempt',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]
