# Generated by Django 5.0.6 on 2024-07-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_enter_time_alter_student_exit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enter_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='exit_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
