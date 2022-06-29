# Generated by Django 4.0.5 on 2022-06-25 18:48

import _socket
from django.conf import settings
from django.db import migrations, models
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
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('edc_action_item', '0028_auto_20210203_0706'),
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edc_protocol_violation', '0004_alter_protocoldeviationviolation_violation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtocolIncident',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50)),
                ('tracking_identifier', models.CharField(max_length=32, unique=True)),
                ('action_identifier', models.CharField(max_length=50, unique=True)),
                ('parent_action_identifier', models.CharField(blank=True, help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(blank=True, help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('action_item_reason', models.TextField(editable=False, null=True)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, verbose_name='Report Date and Time')),
                ('short_description', models.CharField(help_text='Max 35 characters. Note: there is additional space below for a more detailed description', max_length=35, null=True, verbose_name='Provide a short description of this incident')),
                ('report_type', models.CharField(choices=[('protocol_violation', 'Protocol violation'), ('protocol_deviation', 'Protocol deviation')], max_length=25, verbose_name='Type of incident')),
                ('safety_impact', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Could this incident have an impact on safety of the participant?')),
                ('safety_impact_details', models.TextField(blank=True, null=True, verbose_name='If "Yes", provide details')),
                ('study_outcomes_impact', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Could this incident have an impact on study outcomes?')),
                ('study_outcomes_impact_details', models.TextField(blank=True, null=True, verbose_name='If "Yes", provide details')),
                ('incident_datetime', models.DateTimeField(null=True, validators=[edc_model.validators.date.datetime_not_future], verbose_name='Date incident occurred')),
                ('incident_other', models.CharField(blank=True, max_length=75, null=True, verbose_name='If other, please specify')),
                ('incident_description', models.TextField(help_text='Describe in full. Explain how the incident happened, what occurred, etc.', null=True, verbose_name='Describe the incident')),
                ('incident_reason', models.TextField(null=True, verbose_name='Explain the reason why the incident occurred')),
                ('corrective_action_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.validators.date.datetime_not_future], verbose_name='Corrective action date and time')),
                ('corrective_action', models.TextField(blank=True, null=True, verbose_name='Corrective action taken')),
                ('preventative_action_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.validators.date.datetime_not_future], verbose_name='Preventative action date and time')),
                ('preventative_action', models.TextField(blank=True, null=True, verbose_name='Preventative action taken')),
                ('report_status', models.CharField(choices=[('open', 'Open. Some information is still pending.'), ('closed', 'Closed. This report is complete')], max_length=25, verbose_name='What is the status of this report?')),
                ('report_closed_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.validators.date.datetime_not_future], verbose_name='Date and time report closed.')),
                ('action_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_action_item.actionitem')),
                ('action_required', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_protocol_violation.actionsrequired')),
                ('incident', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_protocol_violation.protocolviolations', verbose_name='Type of incident')),
                ('parent_action_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.actionitem')),
                ('related_action_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_action_item.actionitem')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'Protocol Incident',
                'verbose_name_plural': 'Protocol Incident',
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
            managers=[
                ('on_site', edc_action_item.managers.ActionIdentifierSiteManager()),
                ('objects', edc_action_item.managers.ActionIdentifierManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalProtocolIncident',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(max_length=50)),
                ('tracking_identifier', models.CharField(db_index=True, max_length=32)),
                ('action_identifier', models.CharField(db_index=True, max_length=50)),
                ('parent_action_identifier', models.CharField(blank=True, help_text='action identifier that links to parent reference model instance.', max_length=30, null=True)),
                ('related_action_identifier', models.CharField(blank=True, help_text='action identifier that links to related reference model instance.', max_length=30, null=True)),
                ('action_item_reason', models.TextField(editable=False, null=True)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, verbose_name='Report Date and Time')),
                ('short_description', models.CharField(help_text='Max 35 characters. Note: there is additional space below for a more detailed description', max_length=35, null=True, verbose_name='Provide a short description of this incident')),
                ('report_type', models.CharField(choices=[('protocol_violation', 'Protocol violation'), ('protocol_deviation', 'Protocol deviation')], max_length=25, verbose_name='Type of incident')),
                ('safety_impact', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Could this incident have an impact on safety of the participant?')),
                ('safety_impact_details', models.TextField(blank=True, null=True, verbose_name='If "Yes", provide details')),
                ('study_outcomes_impact', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Could this incident have an impact on study outcomes?')),
                ('study_outcomes_impact_details', models.TextField(blank=True, null=True, verbose_name='If "Yes", provide details')),
                ('incident_datetime', models.DateTimeField(null=True, validators=[edc_model.validators.date.datetime_not_future], verbose_name='Date incident occurred')),
                ('incident_other', models.CharField(blank=True, max_length=75, null=True, verbose_name='If other, please specify')),
                ('incident_description', models.TextField(help_text='Describe in full. Explain how the incident happened, what occurred, etc.', null=True, verbose_name='Describe the incident')),
                ('incident_reason', models.TextField(null=True, verbose_name='Explain the reason why the incident occurred')),
                ('corrective_action_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.validators.date.datetime_not_future], verbose_name='Corrective action date and time')),
                ('corrective_action', models.TextField(blank=True, null=True, verbose_name='Corrective action taken')),
                ('preventative_action_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.validators.date.datetime_not_future], verbose_name='Preventative action date and time')),
                ('preventative_action', models.TextField(blank=True, null=True, verbose_name='Preventative action taken')),
                ('report_status', models.CharField(choices=[('open', 'Open. Some information is still pending.'), ('closed', 'Closed. This report is complete')], max_length=25, verbose_name='What is the status of this report?')),
                ('report_closed_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.validators.date.datetime_not_future], verbose_name='Date and time report closed.')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.actionitem')),
                ('action_required', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_protocol_violation.actionsrequired')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('incident', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_protocol_violation.protocolviolations', verbose_name='Type of incident')),
                ('parent_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.actionitem')),
                ('related_action_item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_action_item.actionitem')),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Protocol Incident',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddIndex(
            model_name='protocolincident',
            index=models.Index(fields=['subject_identifier', 'action_identifier', 'site', 'id'], name='edc_protoco_subject_6848b1_idx'),
        ),
    ]
