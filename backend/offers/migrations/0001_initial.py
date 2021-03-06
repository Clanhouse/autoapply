# Generated by Django 3.1 on 2021-09-26 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('company_name', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('experience_level', models.CharField(blank=True, choices=[('T', 'Trainee'), ('J', 'Junior'), ('M', 'Mid'), ('S', 'Senior'), ('E', 'Expert')], max_length=1)),
                ('salary_min', models.IntegerField(blank=True, null=True)),
                ('salary_max', models.IntegerField(blank=True, null=True)),
                ('remote', models.BooleanField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.offer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
