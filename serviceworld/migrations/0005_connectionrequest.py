# Generated by Django 4.1.2 on 2023-04-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceworld', '0004_member_lat_member_lng'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField()),
                ('pid', models.IntegerField()),
            ],
        ),
    ]