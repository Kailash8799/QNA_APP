# Generated by Django 4.1.4 on 2023-02-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_credentials', '0006_alter_users_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(default='Not Selected', max_length=20),
        ),
    ]