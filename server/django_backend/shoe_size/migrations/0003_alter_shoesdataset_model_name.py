# Generated by Django 3.2.5 on 2021-07-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe_size', '0002_ownshoes_user_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoesdataset',
            name='model_name',
            field=models.CharField(max_length=255),
        ),
    ]