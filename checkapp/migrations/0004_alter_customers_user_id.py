# Generated by Django 3.2.5 on 2021-10-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0003_alter_customers_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='user_id',
            field=models.CharField(default='6nr7lif9', editable=False, max_length=8),
        ),
    ]