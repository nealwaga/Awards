# Generated by Django 4.0.5 on 2022-06-12 13:53

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0002_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='screenshot')),
                ('url', models.URLField(default='website.url', max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('design', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], default=0)),
                ('usability', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], default=0)),
                ('content', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], default=0)),
                ('vote_submissions', models.IntegerField(default=0)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='awards.tags')),
            ],
        ),
    ]