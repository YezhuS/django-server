# Generated by Django 2.2.4 on 2019-08-22 20:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('adjunto', models.FileField(null=True, upload_to='uploads/')),
                ('task', models.BooleanField()),
                ('tag', models.CharField(blank=True, max_length=20, null=True)),
                ('type', models.CharField(choices=[('Agua', 'Agua'), ('Fuego', 'Fuego'), ('Planta', 'Planta')], max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.User')),
            ],
        ),
    ]
