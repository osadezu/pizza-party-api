# Generated by Django 4.0.2 on 2022-02-13 04:28

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
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blurb', models.CharField(max_length=280)),
                ('hero_image', models.ImageField(blank=True, upload_to='team_image/')),
                ('custom_prompt', models.CharField(max_length=150)),
                ('collab_prompt', models.CharField(max_length=150)),
                ('required_fields', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, max_length=150)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(blank=True, max_length=25)),
                ('goes_by', models.CharField(blank=True, max_length=25)),
                ('pronouns', models.CharField(blank=True, max_length=25)),
                ('avatar', models.ImageField(blank=True, upload_to='user_image/')),
                ('link', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('loc_lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('loc_long', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('interests', models.CharField(blank=True, max_length=280)),
                ('pets', models.CharField(blank=True, max_length=100)),
                ('custom_answer', models.CharField(blank=True, max_length=280)),
                ('collab_answer', models.CharField(blank=True, max_length=280)),
                ('reactions_count', models.IntegerField(default=0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='teams.team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]