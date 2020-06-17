# Generated by Django 2.0 on 2020-06-17 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='persondetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Address', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='persondetails',
        ),
    ]
