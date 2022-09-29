# Generated by Django 3.2.6 on 2021-09-09 23:34

import uuid

import _socket
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_action_item.managers
import edc_model.validators.date
import edc_utils.date
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("edc_action_item", "0028_auto_20210203_0706"),
    ]

    operations = [
        migrations.CreateModel(
            name="ActionsRequired",
            fields=[
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                ("version", models.CharField(default="1.0", editable=False, max_length=35)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "verbose_name": "Actions Required",
                "verbose_name_plural": "Actions Required",
                "ordering": ["display_index", "display_name"],
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
            },
        ),
        migrations.CreateModel(
            name="HistoricalProtocolDeviationViolation",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                ("subject_identifier", models.CharField(max_length=50)),
                ("tracking_identifier", models.CharField(db_index=True, max_length=30)),
                ("action_identifier", models.CharField(db_index=True, max_length=50)),
                (
                    "parent_action_identifier",
                    models.CharField(
                        blank=True,
                        help_text="action identifier that links to parent reference model instance.",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "related_action_identifier",
                    models.CharField(
                        blank=True,
                        help_text="action identifier that links to related reference model instance.",
                        max_length=30,
                        null=True,
                    ),
                ),
                ("action_item_reason", models.TextField(editable=False, null=True)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow, verbose_name="Report Date and Time"
                    ),
                ),
                (
                    "short_description",
                    models.CharField(
                        help_text='Max 35 characters. Note: If this occurrence is a "violation" there is additional space below for a more detailed description',
                        max_length=35,
                        null=True,
                        verbose_name="Provide a short description of this occurrence",
                    ),
                ),
                (
                    "report_type",
                    models.CharField(
                        choices=[
                            ("protocol_violation", "Protocol violation"),
                            ("protocol_deviation", "Protocol deviation"),
                        ],
                        max_length=25,
                        verbose_name="Type of occurrence",
                    ),
                ),
                (
                    "safety_impact",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Could this occurrence have an impact on safety of the participant?",
                    ),
                ),
                (
                    "safety_impact_details",
                    models.TextField(
                        blank=True, null=True, verbose_name='If "Yes", provide details'
                    ),
                ),
                (
                    "study_outcomes_impact",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Could this occurrence have an impact on study outcomes?",
                    ),
                ),
                (
                    "study_outcomes_impact_details",
                    models.TextField(
                        blank=True, null=True, verbose_name='If "Yes", provide details'
                    ),
                ),
                (
                    "violation_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Date violation occurred",
                    ),
                ),
                (
                    "violation_other",
                    models.CharField(
                        blank=True,
                        max_length=75,
                        null=True,
                        verbose_name="If other, please specify",
                    ),
                ),
                (
                    "violation_description",
                    models.TextField(
                        blank=True,
                        help_text="Describe in full. Explain how the violation happened, what occurred, etc.",
                        null=True,
                        verbose_name="Describe the violation",
                    ),
                ),
                (
                    "violation_reason",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="Explain the reason why the violation occurred",
                    ),
                ),
                (
                    "corrective_action_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Corrective action date and time",
                    ),
                ),
                (
                    "corrective_action",
                    models.TextField(
                        blank=True, null=True, verbose_name="Corrective action taken"
                    ),
                ),
                (
                    "preventative_action_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Preventative action date and time",
                    ),
                ),
                (
                    "preventative_action",
                    models.TextField(
                        blank=True, null=True, verbose_name="Preventative action taken"
                    ),
                ),
                (
                    "report_status",
                    models.CharField(
                        choices=[
                            ("open", "Open. Some information is still pending."),
                            ("closed", "Closed. This report is complete"),
                        ],
                        max_length=25,
                        verbose_name="What is the status of this report?",
                    ),
                ),
                (
                    "report_closed_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Date and time report closed.",
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Protocol Deviation/Violation",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="ProtocolDeviationViolation",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("subject_identifier", models.CharField(max_length=50)),
                ("tracking_identifier", models.CharField(max_length=30, unique=True)),
                ("action_identifier", models.CharField(max_length=50, unique=True)),
                (
                    "parent_action_identifier",
                    models.CharField(
                        blank=True,
                        help_text="action identifier that links to parent reference model instance.",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "related_action_identifier",
                    models.CharField(
                        blank=True,
                        help_text="action identifier that links to related reference model instance.",
                        max_length=30,
                        null=True,
                    ),
                ),
                ("action_item_reason", models.TextField(editable=False, null=True)),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow, verbose_name="Report Date and Time"
                    ),
                ),
                (
                    "short_description",
                    models.CharField(
                        help_text='Max 35 characters. Note: If this occurrence is a "violation" there is additional space below for a more detailed description',
                        max_length=35,
                        null=True,
                        verbose_name="Provide a short description of this occurrence",
                    ),
                ),
                (
                    "report_type",
                    models.CharField(
                        choices=[
                            ("protocol_violation", "Protocol violation"),
                            ("protocol_deviation", "Protocol deviation"),
                        ],
                        max_length=25,
                        verbose_name="Type of occurrence",
                    ),
                ),
                (
                    "safety_impact",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Could this occurrence have an impact on safety of the participant?",
                    ),
                ),
                (
                    "safety_impact_details",
                    models.TextField(
                        blank=True, null=True, verbose_name='If "Yes", provide details'
                    ),
                ),
                (
                    "study_outcomes_impact",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Could this occurrence have an impact on study outcomes?",
                    ),
                ),
                (
                    "study_outcomes_impact_details",
                    models.TextField(
                        blank=True, null=True, verbose_name='If "Yes", provide details'
                    ),
                ),
                (
                    "violation_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Date violation occurred",
                    ),
                ),
                (
                    "violation_other",
                    models.CharField(
                        blank=True,
                        max_length=75,
                        null=True,
                        verbose_name="If other, please specify",
                    ),
                ),
                (
                    "violation_description",
                    models.TextField(
                        blank=True,
                        help_text="Describe in full. Explain how the violation happened, what occurred, etc.",
                        null=True,
                        verbose_name="Describe the violation",
                    ),
                ),
                (
                    "violation_reason",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="Explain the reason why the violation occurred",
                    ),
                ),
                (
                    "corrective_action_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Corrective action date and time",
                    ),
                ),
                (
                    "corrective_action",
                    models.TextField(
                        blank=True, null=True, verbose_name="Corrective action taken"
                    ),
                ),
                (
                    "preventative_action_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Preventative action date and time",
                    ),
                ),
                (
                    "preventative_action",
                    models.TextField(
                        blank=True, null=True, verbose_name="Preventative action taken"
                    ),
                ),
                (
                    "report_status",
                    models.CharField(
                        choices=[
                            ("open", "Open. Some information is still pending."),
                            ("closed", "Closed. This report is complete"),
                        ],
                        max_length=25,
                        verbose_name="What is the status of this report?",
                    ),
                ),
                (
                    "report_closed_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.datetime_not_future],
                        verbose_name="Date and time report closed.",
                    ),
                ),
            ],
            options={
                "verbose_name": "Protocol Deviation/Violation",
                "verbose_name_plural": "Protocol Deviations/Violations",
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
            },
            managers=[
                ("on_site", edc_action_item.managers.ActionIdentifierSiteManager()),
                ("objects", edc_action_item.managers.ActionIdentifierModelManager()),
            ],
        ),
        migrations.CreateModel(
            name="ProtocolViolations",
            fields=[
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                ("version", models.CharField(default="1.0", editable=False, max_length=35)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "verbose_name": "Protocol Violations",
                "verbose_name_plural": "Protocol Violations",
                "ordering": ["display_index", "display_name"],
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
            },
        ),
        migrations.AddIndex(
            model_name="protocolviolations",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="edc_protoco_id_fe21ea_idx",
            ),
        ),
        migrations.AddField(
            model_name="protocoldeviationviolation",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AddField(
            model_name="protocoldeviationviolation",
            name="action_required",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_protocol_incident.actionsrequired",
            ),
        ),
        migrations.AddField(
            model_name="protocoldeviationviolation",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AddField(
            model_name="protocoldeviationviolation",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AddField(
            model_name="protocoldeviationviolation",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.site",
            ),
        ),
        migrations.AddField(
            model_name="protocoldeviationviolation",
            name="violation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_protocol_incident.protocolviolations",
            ),
        ),
        migrations.AddField(
            model_name="historicalprotocoldeviationviolation",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AddField(
            model_name="historicalprotocoldeviationviolation",
            name="action_required",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_protocol_incident.actionsrequired",
            ),
        ),
        migrations.AddField(
            model_name="historicalprotocoldeviationviolation",
            name="history_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="historicalprotocoldeviationviolation",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AddField(
            model_name="historicalprotocoldeviationviolation",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AddField(
            model_name="historicalprotocoldeviationviolation",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.site",
            ),
        ),
        migrations.AddField(
            model_name="historicalprotocoldeviationviolation",
            name="violation",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_protocol_incident.protocolviolations",
            ),
        ),
        migrations.AddIndex(
            model_name="actionsrequired",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="edc_protoco_id_158eab_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="protocoldeviationviolation",
            index=models.Index(
                fields=["subject_identifier", "action_identifier", "site", "id"],
                name="edc_protoco_subject_e56b31_idx",
            ),
        ),
    ]
