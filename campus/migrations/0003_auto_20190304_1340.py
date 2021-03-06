# Generated by Django 2.1.7 on 2019-03-04 08:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0002_stu_details_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu_details',
            name='class_12_percentage',
            field=models.FloatField(help_text='*required', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='stu_details',
            name='sop',
            field=models.CharField(default='statement of purpose', help_text='*required', max_length=500),
        ),
    ]
