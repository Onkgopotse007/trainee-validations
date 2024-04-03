from edc_form_validators import FormValidator
from edc_constants.constants import MALE


class DemographicValidationForm(FormValidator):

    def clean(self):

        self.screening_identifier = self.cleaned_data.get('screening_identifier')

        gender = self.cleaned_data.get('gender')

        if gender == MALE:
            self.required_if('Married', field='marital_status',
                             field_required='men_number_wives')
        else:
            self.required_if('Married', field='marital_status',
                             field_required='women_number_husbands')
