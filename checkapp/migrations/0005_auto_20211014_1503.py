# Generated by Django 3.2.5 on 2021-10-14 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0004_alter_customers_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='email',
            field=models.EmailField(default='@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='customers',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='customers',
            name='user_id',
            field=models.CharField(default='colxzd2j', editable=False, max_length=8),
        ),
    ]
