# Generated by Django 4.0.6 on 2023-05-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceworld', '0006_member_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='providermember',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]