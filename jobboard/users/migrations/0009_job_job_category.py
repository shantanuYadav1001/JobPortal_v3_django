# Generated by Django 4.2.1 on 2023-05-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_job_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_category',
            field=models.CharField(blank=True, choices=[('full-time', 'Full Time'), ('part-time', 'Part Time'), ('internship', 'Internship'), ('freelance', 'Freelance'), ('temporary', 'Temporary')], max_length=20, null=True),
        ),
    ]
