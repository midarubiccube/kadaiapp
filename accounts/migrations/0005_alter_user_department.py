# Generated by Django 5.2.3 on 2025-07-24 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_department'),
        ('sisan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, help_text='所属している学科を選択できます', on_delete=django.db.models.deletion.PROTECT, to='sisan.department'),
        ),
    ]
