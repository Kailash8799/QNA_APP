# Generated by Django 4.0.1 on 2023-02-13 13:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_ans', '0002_remove_question_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='content',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
