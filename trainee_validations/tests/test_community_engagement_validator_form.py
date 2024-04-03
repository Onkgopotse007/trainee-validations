from django.test import TestCase
from trainee_validations.form_validators.community_engagement_validator import CommunityEngagementValidationForm
from edc_constants.constants import YES
from django.core.exceptions import ValidationError

class TestCommunityEngagementValidationForm (TestCase):
     
    def test_problem_solving_required(self):
        cleaned_data = {
            'major_problems':'Dont Know',
            'problem_solving':YES,
        }
        form_validator = CommunityEngagementValidationForm(
            cleaned_data = cleaned_data)
        self.assertRaises(ValidationError,form_validator.validate)
        self.assertIn('problem_solving',form_validator._errors)
      