# Generated by Django 2.0.2 on 2018-03-02 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0002_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Status change'),
        ),
    ]
