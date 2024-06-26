# Generated by Django 4.2.11 on 2024-05-16 12:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_conversa_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='day_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='usuario',
            name='image',
            field=models.ImageField(default='assets/icon.png', upload_to='assets/'),
        ),
    ]
