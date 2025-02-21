# Generated by Django 5.1.5 on 2025-02-01 07:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_en', models.CharField(max_length=255)),
                ('question_hi', models.CharField(blank=True, max_length=255, null=True)),
                ('answer_en', ckeditor.fields.RichTextField()),
                ('answer_hi', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
