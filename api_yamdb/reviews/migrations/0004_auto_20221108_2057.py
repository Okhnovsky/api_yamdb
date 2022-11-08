# Generated by Django 2.2.16 on 2022-11-08 17:57

from django.conf import settings
from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0003_auto_20221106_2108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-pub_date']},
        ),
        migrations.RemoveConstraint(
            model_name='review',
            name='unique review',
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.SmallIntegerField(default=1, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(db_index=True, max_length=256, verbose_name='Название произведения'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(db_index=True, validators=[reviews.validators.validate_year], verbose_name='Дата выхода'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('title', 'author')},
        ),
    ]
