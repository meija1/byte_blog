# Generated by Django 3.2.19 on 2023-07-07 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='approved',
        ),
    ]