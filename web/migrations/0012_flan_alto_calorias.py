# Generated by Django 4.2 on 2024-05-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='alto_calorias',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=10),
        ),
    ]
