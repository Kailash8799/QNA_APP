# Generated by Django 4.0.1 on 2023-02-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_credentials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_date_join',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]