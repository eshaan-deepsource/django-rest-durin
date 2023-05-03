# Generated by Django 4.1.3 on 2022-11-25 18:39

from django.db import migrations, models
import durin.models


class Migration(migrations.Migration):

    dependencies = [
        ("durin", "0002_client_throttlerate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="token_ttl",
            field=models.DurationField(
                default=durin.models.get_DEFAULT_TOKEN_TTL,
                help_text="\n            Token Time To Live (TTL) in timedelta. Format: <code>DAYS HH:MM:SS</code>.\n            ",
                verbose_name="Token Time To Live (TTL)",
            ),
        ),
    ]
