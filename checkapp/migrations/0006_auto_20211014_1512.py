# Generated by Django 3.2.5 on 2021-10-14 08:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0005_auto_20211014_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='id',
        ),
        migrations.AlterField(
            model_name='customers',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
