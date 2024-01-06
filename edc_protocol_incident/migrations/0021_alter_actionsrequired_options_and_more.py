# Generated by Django 4.2.7 on 2023-12-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "edc_protocol_incident",
            "0020_alter_historicalprotocoldeviationviolation_device_created_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="actionsrequired",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Actions Required",
                "verbose_name_plural": "Actions Required",
            },
        ),
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
                "verbose_name": "Protocol Incident",
                "verbose_name_plural": "Protocol Incident",
            },
        ),
        migrations.AlterModelOptions(
            name="protocolincidents",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Protocol Incidents",
                "verbose_name_plural": "Protocol Incidents",
            },
        ),
        migrations.AlterModelOptions(
            name="protocolviolations",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Protocol Violations",
                "verbose_name_plural": "Protocol Violations",
            },
        ),
        migrations.RemoveIndex(
            model_name="actionsrequired",
            name="edc_protoco_id_17a455_idx",
        ),
        migrations.RemoveIndex(
            model_name="protocoldeviationviolation",
            name="edc_protoco_subject_366adb_idx",
        ),
        migrations.RemoveIndex(
            model_name="protocolincident",
            name="edc_protoco_subject_1c6fcb_idx",
        ),
        migrations.RemoveIndex(
            model_name="protocolincidents",
            name="edc_protoco_id_7c6a33_idx",
        ),
        migrations.RemoveIndex(
            model_name="protocolviolations",
            name="edc_protoco_id_58f1f5_idx",
        ),
        migrations.AddField(
            model_name="historicalprotocoldeviationviolation",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="historicalprotocoldeviationviolation",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AddField(
            model_name="historicalprotocolincident",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="historicalprotocolincident",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AddField(
            model_name="protocoldeviationviolation",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="protocoldeviationviolation",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AddField(
            model_name="protocolincident",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="protocolincident",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AlterField(
            model_name="actionsrequired",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="actionsrequired",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="actionsrequired",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AlterField(
            model_name="protocolincidents",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="protocolincidents",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="protocolincidents",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AlterField(
            model_name="protocolviolations",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="protocolviolations",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="protocolviolations",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AddIndex(
            model_name="actionsrequired",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_protoco_display_33f026_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="protocoldeviationviolation",
            index=models.Index(
                fields=["subject_identifier", "action_identifier", "site"],
                name="edc_protoco_subject_d2572f_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="protocoldeviationviolation",
            index=models.Index(
                fields=["subject_identifier"], name="edc_protoco_subject_b70719_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="protocoldeviationviolation",
            index=models.Index(
                fields=[
                    "action_identifier",
                    "action_item",
                    "related_action_item",
                    "parent_action_item",
                ],
                name="edc_protoco_action__1aec09_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="protocoldeviationviolation",
            index=models.Index(
                fields=["modified", "created"], name="edc_protoco_modifie_09d487_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="protocoldeviationviolation",
            index=models.Index(
                fields=["user_modified", "user_created"],
                name="edc_protoco_user_mo_1e4dfd_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="protocolincident",
            index=models.Index(
                fields=["subject_identifier", "action_identifier", "site"],
                name="edc_protoco_subject_27ef7f_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="protocolincident",
            index=models.Index(
                fields=["subject_identifier"], name="edc_protoco_subject_46900a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="protocolincident",
            index=models.Index(
                fields=[
                    "action_identifier",
                    "action_item",
                    "related_action_item",
                    "parent_action_item",
                ],
                name="edc_protoco_action__a276b5_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="protocolincident",
            index=models.Index(
                fields=["modified", "created"], name="edc_protoco_modifie_1029be_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="protocolincident",
            index=models.Index(
                fields=["user_modified", "user_created"],
                name="edc_protoco_user_mo_937eb4_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="protocolincidents",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_protoco_display_980b51_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="protocolviolations",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_protoco_display_036d9b_idx",
            ),
        ),
    ]