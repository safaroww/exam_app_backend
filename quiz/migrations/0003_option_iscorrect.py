# Generated by Django 4.2.7 on 2023-11-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_option_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='iscorrect',
            field=models.BooleanField(default=False),
        ),
    ]
