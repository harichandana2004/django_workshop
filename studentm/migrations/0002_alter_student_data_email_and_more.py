# Generated by Django 5.0.3 on 2024-03-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='gender',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
