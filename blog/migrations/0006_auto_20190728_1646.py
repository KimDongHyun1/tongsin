# Generated by Django 2.2.3 on 2019-07-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190728_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='gps1',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='posting',
            name='gps2',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=19),
        ),
    ]
