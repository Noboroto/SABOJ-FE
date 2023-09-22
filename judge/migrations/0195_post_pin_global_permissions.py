# Generated by Django 3.2.21 on 2023-09-15 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0194_ban_permission'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'permissions': (('edit_all_post', 'Edit all posts'), ('edit_organization_post', 'Edit organization posts'), ('mark_global_post', 'Mark post as global'), ('pin_post', 'Pin post')), 'verbose_name': 'blog post', 'verbose_name_plural': 'blog posts'},
        ),
    ]