from edc_constants.constants import CLOSED, OTHER, YES
from edc_form_validators import INVALID_ERROR, FormValidator

# from ..constants import VIOLATION


class ProtocolIncidentFormValidator(FormValidator):
    def clean(self):

        self.required_if(YES, field="safety_impact", field_required="safety_impact_details")

        self.required_if(
            YES,
            field="study_outcomes_impact",
            field_required="study_outcomes_impact_details",
        )
        if (
            self.cleaned_data.get("incident_datetime")
            and self.cleaned_data.get("report_datetime")
            and self.cleaned_data.get("incident_datetime")
            > self.cleaned_data.get("report_datetime")
        ):
            self.raise_validation_error(
                {"incident_datetime": "May not be after report date/time"},
                error_code=INVALID_ERROR,
            )
        self.validate_other_specify(field="incident", other_specify_field="incident_other")

        self.required_if_not_none(
            field="corrective_action_datetime", field_required="corrective_action"
        )
        self.validate_date_not_before_incident("corrective_action_datetime")
        self.required_if_not_none(
            field="preventative_action_datetime", field_required="preventative_action"
        )
        self.validate_date_not_before_incident("preventative_action_datetime")

        self.required_if(
            CLOSED, field="report_status", field_required="report_closed_datetime"
        )
        self.validate_date_not_before_incident("report_closed_datetime")

    def validate_date_not_before_incident(self, fld_name):
        if self.cleaned_data.get(fld_name) and self.cleaned_data.get("incident_datetime"):
            if self.cleaned_data.get(fld_name) < self.cleaned_data.get("incident_datetime"):
                self.raise_validation_error(
                    {fld_name: "May not be before incident date/time"},
                    error_code=INVALID_ERROR,
                )
