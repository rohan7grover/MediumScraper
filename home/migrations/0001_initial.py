# Generated by Django 3.2.8 on 2021-10-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_Tag', models.CharField(max_length=120)),
                ('Blog_Title', models.TextField()),
                ('Blog_Author', models.CharField(max_length=120)),
                ('Publishing_Date', models.CharField(max_length=120)),
                ('Estimated_Reading_Time', models.CharField(max_length=120)),
                ('date', models.DateField()),
            ],
        ),
    ]
