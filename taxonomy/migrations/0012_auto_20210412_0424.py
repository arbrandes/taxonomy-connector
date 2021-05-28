# Generated by Django 2.2.20 on 2021-04-12 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0011_auto_20210412_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseskills',
            name='course_key',
            field=models.CharField(help_text='The key of the course whose text was used for skills extraction.', max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='courseskills',
            unique_together={('course_key', 'skill')},
        ),
    ]