# Generated by Django 4.2.4 on 2023-09-08 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='label1',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='label2',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
