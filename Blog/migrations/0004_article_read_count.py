# Generated by Django 2.0.5 on 2018-07-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20180701_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='read_count',
            field=models.IntegerField(default=0),
        ),
    ]