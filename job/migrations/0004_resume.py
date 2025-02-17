# Generated by Django 2.2.6 on 2020-04-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20200401_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('gmail', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=20)),
                ('profession', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='profile')),
                ('video', models.CharField(max_length=100)),
                ('catagory', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=250)),
                ('skills', models.CharField(max_length=300)),
            ],
        ),
    ]
