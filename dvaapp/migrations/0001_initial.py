# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 05:16
from __future__ import unicode_literals

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
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multi_frame', models.BooleanField(default=False)),
                ('metadata_text', models.TextField(default='')),
                ('name', models.TextField(default='unnamed_annotation')),
                ('full_frame', models.BooleanField(default=True)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('h', models.IntegerField(default=0)),
                ('w', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Detection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_name', models.CharField(max_length=100)),
                ('confidence', models.FloatField(default=0.0)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('h', models.IntegerField(default=0)),
                ('w', models.IntegerField(default=0)),
                ('metadata', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ExternalDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algorithm', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('count_images', models.IntegerField()),
                ('count_entries', models.IntegerField()),
                ('cached_image_count', models.IntegerField()),
                ('index_downloaded', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_index', models.IntegerField()),
                ('name', models.CharField(max_length=200, null=True)),
                ('subdir', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='FrameLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('source', models.TextField()),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Frame')),
            ],
        ),
        migrations.CreateModel(
            name='IndexEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features_file_name', models.CharField(max_length=100)),
                ('entries_file_name', models.CharField(max_length=100)),
                ('algorithm', models.CharField(max_length=100)),
                ('detection_name', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('approximate', models.BooleanField(default=False)),
                ('contains_frames', models.BooleanField(default=False)),
                ('contains_detections', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('results', models.BooleanField(default=False)),
                ('results_metadata', models.TextField(default='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QueryResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('algorithm', models.CharField(max_length=100)),
                ('distance', models.FloatField(default=0.0)),
                ('detection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Detection')),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Frame')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Query')),
            ],
        ),
        migrations.CreateModel(
            name='TEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('operation', models.CharField(default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('seconds', models.FloatField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('length_in_seconds', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('metadata', models.TextField(default='')),
                ('frames', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('description', models.TextField(default='')),
                ('uploaded', models.BooleanField(default=False)),
                ('dataset', models.BooleanField(default=False)),
                ('detections', models.IntegerField(default=0)),
                ('url', models.TextField(default='')),
                ('youtube_video', models.BooleanField(default=False)),
                ('query', models.BooleanField(default=False)),
                ('parent_query', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Query')),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tevent',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='queryresults',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='indexentries',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='framelabel',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='frame',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='detection',
            name='frame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='detection',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='detection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Detection'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='end_frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_frame', to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='start_frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_frame', to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='annotation',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
    ]
