# Generated by Django 4.1.1 on 2022-10-01 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_alter_tipo_formapago_tifo_forma_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='realizado',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]