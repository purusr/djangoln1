# Generated by Django 4.1.5 on 2023-01-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=100)),
                ('Student_roll', models.IntegerField(default=0)),
                ('Student_department', models.CharField(max_length=100)),
                ('Student_contact', models.CharField(max_length=200)),
                ('Student_idenntity', models.CharField(max_length=100)),
            ],
        ),
    ]
