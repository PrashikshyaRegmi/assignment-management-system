# Generated by Django 2.2.7 on 2019-12-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=100)),
                ('studentemail', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('studassignments', models.FileField(upload_to='teacher/assignments/')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachername', models.CharField(max_length=100)),
                ('teacheremail', models.EmailField(max_length=100)),
                ('teachersubject', models.CharField(max_length=100)),
                ('assignments', models.FileField(upload_to='teacher/assignments/')),
                ('duedate', models.CharField(max_length=100)),
            ],
        ),
    ]
