# Generated by Django 5.1.4 on 2024-12-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_group_studygroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='preferences',
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='preferences',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
