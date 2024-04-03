from django.test import TestCase
from django.core.exceptions import ValidationError
from edc_constants.constants import NO, YES

from trainee_validations.form_validators.subject_screening_validator import SubjectScreeningFormValidator



class TestSubjectScreeningValidationForm(TestCase):

    def test_enrollment_interest_is_required(self):
        cleaned_data = {
            'enrollment_interest':NO,
            'disinterest_reason':None,
        }
        form_validator = SubjectScreeningFormValidator(
            cleaned_data = cleaned_data)
        self.assertRaises(ValidationError,form_validator.validate)
        self.assertIn('disinterest_reason',form_validator._errors)


    def test_legal_marriage_is_not_applicable(self):
        cleaned_data = {
            'citizen':YES,
            'legal_marriage':YES,
        }
        form_validator = SubjectScreeningFormValidator(
            cleaned_data = cleaned_data)
        self.assertRaises(ValidationError,form_validator.validate)
        self.assertIn('legal_marriage',form_validator._errors)
            
        

