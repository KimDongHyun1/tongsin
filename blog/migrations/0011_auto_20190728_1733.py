# Generated by Django 2.2.3 on 2019-07-28 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190728_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posting',
            old_name='cocoment',
            new_name='cnt',
        ),
        migrations.RenameField(
            model_name='posting',
            old_name='gps1',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='posting',
            old_name='gps2',
            new_name='lng',
        ),
    ]
