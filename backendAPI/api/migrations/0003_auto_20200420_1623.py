# Generated by Django 3.0.5 on 2020-04-20 16:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_article_progress_resource'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Thing',
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='task',
            new_name='thing',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='task',
            new_name='thing',
        ),
        migrations.AlterUniqueTogether(
            name='progress',
            unique_together={('user', 'thing')},
        ),
        migrations.AlterIndexTogether(
            name='progress',
            index_together={('user', 'thing')},
        ),
    ]
