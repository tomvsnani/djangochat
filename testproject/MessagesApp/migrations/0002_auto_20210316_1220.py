# Generated by Django 3.1.6 on 2021-03-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessagesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='imageField',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
