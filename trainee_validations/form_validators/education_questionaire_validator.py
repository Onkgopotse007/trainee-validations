from edc_form_validators import FormValidator
from edc_constants.constants import NO, YES


class EducationQuestionaireValidationForm(FormValidator):

     def clean(self):
       
       
       self.not_applicable(NO,field='working',field_applicable="work_type"
       )
       self.not_applicable(NO,field='working',field_applicable="occupation"
       )
       self.not_applicable(NO,field='working',field_applicable="salary"
       )
       
    
