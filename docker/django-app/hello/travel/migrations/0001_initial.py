# Generated by Django 3.2.4 on 2021-06-15 12:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name_text', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('last_changed_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date changed')),
            ],
        ),
        migrations.CreateModel(
            name='CountryRestriction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200, null=True)),
                ('last_changed_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date changed')),
                ('allow_unvaccinated', models.BooleanField(default=True)),
                ('banned', models.BooleanField(default=False)),
                ('restricted', models.BooleanField(default=False)),
                ('quarantine_days', models.IntegerField(default=0)),
                ('restrictions_text', models.TextField()),
                ('restricting_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.country')),
            ],
        ),
    ]
