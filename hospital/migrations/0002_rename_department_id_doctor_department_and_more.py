# Generated by Django 4.0.3 on 2022-05-07 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='department_id',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='doctor_id',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='patient_id',
            new_name='patient',
        ),
    ]
