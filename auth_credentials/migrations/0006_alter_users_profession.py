# Generated by Django 4.1.4 on 2023-02-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_credentials', '0005_alter_users_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profession',
            field=models.CharField(default='Student', max_length=200),
        ),
    ]
