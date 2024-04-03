from django.test import TestCase
from trainee_validations.form_validators.education_questionaire_validator import EducationQuestionaireValidationForm
from django.core.exceptions import ValidationError
from edc_constants.constants import YES,NO

class TestEducationQuestionaireValidationForm (TestCase):
     
    def test_work_type_is_not_applicable(self):
        cleaned_data = {
            'working':NO,
            'work_type':'Farmer',
        }
        form_validator = EducationQuestionaireValidationForm(
            cleaned_data = cleaned_data)
        self.assertRaises(ValidationError,form_validator.validate)
        self.assertIn('work_type',form_validator._errors)


    def test_occupation_not_applicable(self):
        cleaned_data = {
             'working':NO,
            'occupation':'Teacher',
        }
        form_validator = EducationQuestionaireValidationForm(
            cleaned_data = cleaned_data)
        self.assertRaises(ValidationError,form_validator.validate)
        self.assertIn('occupation',form_validator._errors)
           
    def test_salary_not_applicable(self):
        cleaned_data = {
           'working':NO,
            'salary':'1 - 199 pula',
        }
        form_validator = EducationQuestionaireValidationForm(
            cleaned_data = cleaned_data)
        self.assertRaises(ValidationError,form_validator.validate)
        self.assertIn('salary',form_validator._errors)
           