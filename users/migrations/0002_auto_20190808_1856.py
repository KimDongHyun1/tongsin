# Generated by Django 2.2.3 on 2019-08-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='user_photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
