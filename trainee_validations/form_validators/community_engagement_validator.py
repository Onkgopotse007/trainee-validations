from edc_form_validators import FormValidator
from edc_constants.constants import NO, YES


class CommunityEngagementValidationForm(FormValidator):

    def clean(self):
        self.not_applicable(
            'Dont Know',
            field='major_problems',
            field_applicable="problem_solving")
