# Generated by Django 3.1.4 on 2020-12-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20201207_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_commencement_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_start_date',
            field=models.DateField(),
        ),
    ]
