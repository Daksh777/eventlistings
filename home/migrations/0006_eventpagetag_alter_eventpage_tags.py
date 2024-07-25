# Generated by Django 5.0.7 on 2024-07-25 03:44

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_eventpage_tags_eventpage_tags'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='home.eventpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(help_text='A comma-separated list of tags.', through='home.EventPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]