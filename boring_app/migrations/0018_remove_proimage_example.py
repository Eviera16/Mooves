# Generated by Django 2.2 on 2020-11-28 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boring_app', '0017_proimage_example'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proimage',
            name='example',
        ),
    ]
