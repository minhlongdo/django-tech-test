# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('registered_company', models.CharField(max_length=8)),
                ('business_sector', models.TextField(blank=True, choices=[('retail', 'Retail'), ('professional_services', 'Professional Services'), ('food_drinks', 'Food & Drinks'), ('entertainment', 'Entertainment')])),
            ],
        ),
        migrations.AlterField(
            model_name='borrower',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.Borrower'),
        ),
    ]
