# Generated by Django 5.1.3 on 2024-11-15 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_class_subject_timeslot_remove_timetableentry_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='class_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='teacher',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='timeslot',
            field=models.CharField(max_length=50),
        ),
    ]