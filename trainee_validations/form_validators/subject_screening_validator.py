from edc_form_validators import FormValidator
from edc_constants.constants import NO, YES,NOT_APPLICABLE



class SubjectScreeningFormValidator(FormValidator):

    def clean(self):
       
       
       self.required_if(NO,field='enrollment_interest',field_required="disinterest_reason"
       )

       self.validate_other_specify(field='disinterest_reason',other_specify_field='disinterest_reason_other' )


       self.not_applicable(
        YES,
           field='citizen',
           field_applicable="legal_marriage",
       )
       
       self.not_applicable(
           NOT_APPLICABLE,
           field='legal_marriage',
           field_applicable="marriage_certificate"
       )

       self.required_if(
           YES,
           field='marriage_certificate',
           field_required="marriage_certificate_no"
       )
       self.not_applicable(
           NO,
           field='is_minor',
           field_applicable="guardian"
       )

       self.not_applicable(
           YES,
           field='literate',
           field_applicable="literate_witness"
       )


       


       


