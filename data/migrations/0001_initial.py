# Generated by Django 5.1.2 on 2024-10-29 12:59

import data.storage
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Earring',
            fields=[
                ('id', models.CharField(default='E-', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('total_weight', models.TextField()),
                ('gold_net_weight', models.TextField()),
                ('gems_1', models.TextField(blank=True, null=True)),
                ('gems_2', models.TextField(blank=True, null=True)),
                ('gems_3', models.TextField(blank=True, null=True)),
                ('a_ywrt', models.TextField(blank=True, null=True)),
                ('latkha', models.TextField(blank=True, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('purchased', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EPRSet',
            fields=[
                ('id', models.CharField(default='ERP-', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('total_weight', models.TextField()),
                ('gold_net_weight', models.TextField()),
                ('gems_1', models.TextField(blank=True, null=True)),
                ('gems_2', models.TextField(blank=True, null=True)),
                ('gems_3', models.TextField(blank=True, null=True)),
                ('a_ywrt', models.TextField(blank=True, null=True)),
                ('latkha', models.TextField(blank=True, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('purchased', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Handchain',
            fields=[
                ('id', models.CharField(default='H-', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('total_weight', models.TextField()),
                ('gold_net_weight', models.TextField()),
                ('gems_1', models.TextField(blank=True, null=True)),
                ('gems_2', models.TextField(blank=True, null=True)),
                ('gems_3', models.TextField(blank=True, null=True)),
                ('a_ywrt', models.TextField(blank=True, null=True)),
                ('latkha', models.TextField(blank=True, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('purchased', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Necklace',
            fields=[
                ('id', models.CharField(default='N-', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('total_weight', models.TextField()),
                ('gold_net_weight', models.TextField()),
                ('gems_1', models.TextField(blank=True, null=True)),
                ('gems_2', models.TextField(blank=True, null=True)),
                ('gems_3', models.TextField(blank=True, null=True)),
                ('a_ywrt', models.TextField(blank=True, null=True)),
                ('latkha', models.TextField(blank=True, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('purchased', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pendant',
            fields=[
                ('id', models.CharField(default='P-', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('total_weight', models.TextField()),
                ('gold_net_weight', models.TextField()),
                ('gems_1', models.TextField(blank=True, null=True)),
                ('gems_2', models.TextField(blank=True, null=True)),
                ('gems_3', models.TextField(blank=True, null=True)),
                ('a_ywrt', models.TextField(blank=True, null=True)),
                ('latkha', models.TextField(blank=True, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('purchased', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ring',
            fields=[
                ('id', models.CharField(default='R-', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('total_weight', models.TextField()),
                ('gold_net_weight', models.TextField()),
                ('gems_1', models.TextField(blank=True, null=True)),
                ('gems_2', models.TextField(blank=True, null=True)),
                ('gems_3', models.TextField(blank=True, null=True)),
                ('a_ywrt', models.TextField(blank=True, null=True)),
                ('latkha', models.TextField(blank=True, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('purchased', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(max_length=255)),
                ('image', models.FileField(blank=True, storage=data.storage.ClassSpecificStorage(location='images/'), upload_to='get_upload_path')),
                ('content_type', models.ForeignKey(default=19, limit_choices_to={'model__in': ['necklace', 'eprset', 'earring', 'ring', 'handchain', 'pendant']}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]