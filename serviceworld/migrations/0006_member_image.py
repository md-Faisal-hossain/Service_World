# Generated by Django 4.0.6 on 2023-05-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceworld', '0005_connectionrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(default=12, upload_to='images'),
            preserve_default=False,
        ),
    ]
