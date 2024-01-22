# Generated by Django 4.2.4 on 2023-12-19 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('taskId', models.AutoField(primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=50)),
                ('taskIsDone', models.BooleanField(default=False)),
            ],
        ),
    ]
