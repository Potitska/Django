# Generated by Django 4.2.6 on 2023-10-18 08:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autoparkmodel',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='autoparkmodel',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z]{1,20}$', 'Only letters and first letter uppercase min 2 max 20 ch')]),
        ),
    ]
