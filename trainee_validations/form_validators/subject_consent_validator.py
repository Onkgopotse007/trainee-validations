from django.core.exceptions import ValidationError
from edc_form_validators import FormValidator
from edc_base.utils import age
from edc_constants.constants import MALE, FEMALE, NO




class SubjectConsentFormValidator(FormValidator):


    subject_screening_model = 'traineesubject.subjectscreening'

    def clean(self):
        self.screening_identifier = self.cleaned_data.get('screening_identifier')

        super().clean()
        
        self.validate_identity_gender()
        self.validate_verbal_script_field()
        self.validate_citizen_field()

        
    def validate_identity_gender(self):

        identity_key = self.cleaned_data.get('identity')[4]
        gender = self.cleaned_data.get('gender')

        if gender == MALE and identity_key != '1':
            message = {'national_identity': 'The national identity number '
                       f'does not match the pattern expected. Expected the '
                       f'fifth digit as \'1\' for male, got \'{identity_key}\''}
            self._errors.update(message)
            raise ValidationError(message)
        elif gender == FEMALE and identity_key != '2':
            message = {'identity': 'The national identity number '
                       f'does not match the pattern expected. Expected the '
                       f'fifth digit as \'2\' for female, got \'{identity_key}\''}
            self._errors.update(message)
            raise ValidationError(message)


    def validate_verbal_script_field(self):
        verbal_script = self.cleaned_data.get('verbal_script')

        if verbal_script == NO:
            message = {'verbal_script':
                       'Please provide participant\'s details on verbal script'
                       ' and sign the document.'}
            self._errors.update(message)
            raise ValidationError(message)

    def validate_citizen_field(self):
        citizen = self.cleaned_data.get('citizen')

        if citizen == NO:
            message = {'citizen':
                       'Participant is not a citizen of Botswana.'}
            self._errors.update(message)
            raise ValidationError(message)
