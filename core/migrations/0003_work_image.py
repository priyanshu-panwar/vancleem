# Generated by Django 2.2.8 on 2020-10-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='works/'),
        ),
    ]
