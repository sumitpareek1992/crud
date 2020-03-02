# Generated by Django 3.0.3 on 2020-03-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=10)),
                ('dob', models.DateTimeField()),
                ('pic', models.ImageField(upload_to='media')),
            ],
        ),
    ]
