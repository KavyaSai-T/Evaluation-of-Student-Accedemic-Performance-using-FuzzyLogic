# Generated by Django 2.2.4 on 2021-06-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_studentdetail_no_of_backlogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsection',
            name='reg_no',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentsection',
            name='student_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
