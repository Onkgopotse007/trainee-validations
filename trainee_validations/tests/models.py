from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import GENDER,YES_NO
from edc_base.utils import get_utcnow
from django.db.models.deletion import PROTECT
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin


class SubjectScreening (BaseUuidModel):

    screening_identifier = models.CharField(
        max_length=36,
        unique=True
    )

    report_datetime = models.DateTimeField()


    enrollment_interest  = models.CharField (
        max_length= 3,
        choices=YES_NO,
    )

    disinterest_reason = models.CharField (
        max_length=50,
    )
    
    citizen = models.CharField(
        max_length=3,
        choices=YES_NO
        

    )
    legal_marriage =models.CharField(
        max_length=3,
        choices=YES_NO
        
    )

    marriage_certificate = models.CharField(
        max_length=3,
        null=True,
        choices=YES_NO
        )
    
    marriage_certificate_no = models.CharField(
        max_length=9,


    )


    is_minor =models.CharField(
        max_length= 10,
        choices=YES_NO


    )

    guardian = models.CharField(
        max_length=3,
        choices=YES_NO
    )

    literate = models.CharField(
        max_length=3,
        choices=YES_NO
    )



    literate_witness = models.CharField(
        max_length=3,
        choices=YES_NO

    )

    gender = models.CharField(
        max_length=6,
        choices=GENDER

    )
   
    
class SubjectConsent(UpdatesOrCreatesRegistrationModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    screening_identifier = models.CharField(max_length=50)

    gender = models.CharField(max_length=25)

    is_literate = models.CharField(max_length=25,
                                   blank=True,
                                   null=True)

    witness_name = models.CharField(max_length=25,
                                    blank=True,
                                    null=True)

    dob = models.DateField()

    consent_datetime = models.DateTimeField()

    version = models.CharField(
        max_length=10,
        editable=False)
    

class Appointment(BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    appt_datetime = models.DateTimeField(default=get_utcnow)

    visit_code = models.CharField(max_length=25)

    
class SubjectVisit(BaseUuidModel):

    appointment = models.OneToOneField(Appointment, on_delete=PROTECT)

    subject_identifier = models.CharField(max_length=25)

    visit_code = models.CharField(max_length=25)

    visit_code_sequence = models.IntegerField(default=0)

    report_datetime = models.DateTimeField(
        default=get_utcnow)

    def save(self, *args, **kwargs):
        self.visit_code = self.appointment.visit_code
        self.subject_identifier = self.appointment.subject_identifier
        super().save(*args, **kwargs)



class SubjectLocator(BaseUuidModel):

    subject_identifier = models.CharField(
        max_length=50)

    report_datetime = models.DateTimeField(
        null=True,
        blank=True)

    may_sms = models.CharField(
        max_length=3)

    may_call = models.CharField(
        max_length=3)

    may_visit_home = models.CharField(
        max_length=3)
    

class EducationalQuestionaire():

    working = models.CharField(
        verbose_name= "Are you currently working ?",
        max_length=11,
        choices=YES_NO,
    )


    work_type = models.CharField(
        verbose_name= "In your main job what type of work do you do ?",
        max_length=100,

    )

    occupation = models.CharField(
        verbose_name= "Describe the work that you do or did in your most recent job",
        max_length=100,
    )

    salary = models.CharField(
        verbose_name="In the past month, how much money did you earn from work you did or received in payment?",
        max_length=150,

    )


class Demographic ():

    marital_status = models.CharField(
        verbose_name= "What is your marital status",
        max_length=20,
    )

    women_number_husbands = models.IntegerField(
        verbose_name=("How many wives does your husband have (including traditional marriage),"
        " including yourself?"),
        blank=True,
        null=True,

    )

    men_number_wives = models.IntegerField(
        verbose_name=("How many wives do you have, including traditional marriage?"),
        blank=True,         
        null=True,

    )


    housemate = models.CharField(
        verbose_name= "Who do you currently live with?",
        max_length=20

    )

class CommunityEngagement():

    community_activity = models.CharField(
        verbose_name= ("How active are you in community activities such as burial society,"),
        max_length=50,
    
    )

    voting_status = models.CharField(
        verbose_name= "Did you vote in the last local government election ?",
        max_length=21,

    )
    
    major_problems = models.CharField(
        verbose_name="What are the major problems in this neighborhood?",
        max_length=50,


    )

    problem_solving =models.CharField(
        verbose_name="If there is a problem in this neighborhood,do the adults work together in solving it?",
        max_length=50,
        
    )
    