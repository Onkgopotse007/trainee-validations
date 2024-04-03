from django.test import TestCase
from trainee_validations.form_validators.demographic_validator import DemographicValidationForm
from edc_constants.constants import FEMALE
from django.core.exceptions import ValidationError

class TestDemographicValidationForm (TestCase):

   def test_number_of_partners_required_by_gender(self): 
    cleaned_data ={
        'gender':FEMALE,
        'marital_status':'Married',
        'women_number_husbands':None,
      }
    form_validator = DemographicValidationForm(
            cleaned_data = cleaned_data)
    self.assertRaises(ValidationError,form_validator.validate)
    self.assertIn('women_number_husbands',form_validator._errors)