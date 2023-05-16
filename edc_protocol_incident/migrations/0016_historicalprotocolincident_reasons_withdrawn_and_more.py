# Generated by Django 4.1.2 on 2022-11-30 21:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_protocol_incident", "0001_squashed_0015_auto_20220927_0401"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalprotocolincident",
            name="reasons_withdrawn",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="protocolincident",
            name="reasons_withdrawn",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="historicalprotocolincident",
            name="report_status",
            field=models.CharField(
                choices=[
                    ("open", "Open. Some information is still pending."),
                    ("closed", "Closed. This report is complete"),
                    (
                        "withdrawn",
                        "Withdrawn. This report has been withdrawn after review with investigators",
                    ),
                ],
                max_length=25,
                verbose_name="What is the status of this report?",
            ),
        ),
        migrations.AlterField(
            model_name="protocolincident",
            name="report_status",
            field=models.CharField(
                choices=[
                    ("open", "Open. Some information is still pending."),
                    ("closed", "Closed. This report is complete"),
                    (
                        "withdrawn",
                        "Withdrawn. This report has been withdrawn after review with investigators",
                    ),
                ],
                max_length=25,
                verbose_name="What is the status of this report?",
            ),
        ),
    ]
