# Generated by Django 4.1.1 on 2022-10-01 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_remove_personas_pers_identidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='propietariocliente',
            name='procl_nota',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
