# Generated by Django 3.1.6 on 2021-03-16 06:35

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
            name='MessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageText', models.TextField(blank=True)),
                ('timeSent', models.DateTimeField(auto_now_add=True)),
                ('timeDelivered', models.DateTimeField(blank=True, null=True)),
                ('timeRead', models.DateTimeField(blank=True, null=True)),
                ('messagestatus', models.CharField(default='1', max_length=4)),
                ('imageField', models.ImageField(upload_to='images')),
                ('receiver', models.ForeignKey(default='empty', on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]