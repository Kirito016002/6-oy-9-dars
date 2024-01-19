# Generated by Django 5.0.1 on 2024-01-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'About me',
                'verbose_name_plural': 'About me',
            },
        ),
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('massage', models.TextField()),
            ],
            options={
                'verbose_name': 'Massage',
                'verbose_name_plural': 'Massages',
            },
        ),
        migrations.CreateModel(
            name='My_equpment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name': 'My equpment',
                'verbose_name_plural': 'My equpments',
            },
        ),
        migrations.CreateModel(
            name='My_portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField()),
            ],
            options={
                'verbose_name': 'My portfolio',
                'verbose_name_plural': 'My portfolio images',
            },
        ),
        migrations.CreateModel(
            name='My_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('path', models.TextField()),
            ],
            options={
                'verbose_name': 'My servics',
                'verbose_name_plural': 'My services',
            },
        ),
    ]
