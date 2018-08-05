# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-05 04:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Documenttype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documet_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuepayments', models.IntegerField()),
                ('datepayment', models.DateField()),
                ('observations', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paymentsconcepts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentsconcepts', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('code_student', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name_student', models.CharField(max_length=50)),
                ('lastname_student', models.CharField(max_length=50)),
                ('number_document', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=30)),
                ('address', models.CharField(max_length=60)),
                ('neighborhood', models.CharField(max_length=50)),
                ('number_telephone', models.CharField(max_length=40)),
                ('cellphone_number', models.CharField(max_length=40)),
                ('register_date', models.DateField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.City')),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Documenttype')),
            ],
        ),
        migrations.AddField(
            model_name='payments',
            name='code_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='payments',
            name='paymentsconcepts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Paymentsconcepts'),
        ),
    ]