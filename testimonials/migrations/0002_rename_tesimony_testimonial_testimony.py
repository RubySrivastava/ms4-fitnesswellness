# Generated by Django 3.2.3 on 2021-06-16 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='tesimony',
            new_name='testimony',
        ),
    ]