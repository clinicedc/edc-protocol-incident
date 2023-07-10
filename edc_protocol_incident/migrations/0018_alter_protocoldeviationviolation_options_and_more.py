# Generated by Django 4.2.1 on 2023-07-05 02:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "edc_protocol_incident",
            "0017_alter_historicalprotocolincident_reasons_withdrawn_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="protocoldeviationviolation",
            options={
                "default_manager_name": "objects",
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Protocol Deviation/Violation",
                "verbose_name_plural": "Protocol Deviations/Violations",
            },
        ),
        migrations.AlterModelOptions(
            name="protocolincident",
            options={
                "default_manager_name": "objects",
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Protocol Incident",
                "verbose_name_plural": "Protocol Incident",
            },
        ),
    ]
