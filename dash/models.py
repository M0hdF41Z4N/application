from django.db import models
from phonenumber_field.modelfields import PhoneNumberField




"""-------- Small Down Lead Model -------------------"""


BEDROOMS = (
    ('2','2 BHK'),
    ('2+st', '2 BHK + Study'),
    ('2+sr', '2 BHK + Servant'),
    ('3','3 BHK'),
    ('3+st','3 BHK + Study'),
    ('3+sr','3 BHK + Servant'),
    ('4','4 BHK'),
    ('4+sr','4 BHK + Servant'),
)

LEAD_STATUS = (
    ('N','New'),
    ('C','Cold'),
    ('W','Warm'),
    ('H','Hot'),
    ('I','Hot Ice'),
)

STATUS = (
    ('F','Fresh Lead'),

)

TYPE = (
    ('AP', 'Apartment'),
    ('BF', 'Builder Floor'),
    ('BT', 'Both'),
)

BUDGET_CATEGORY = (
    ('50-70', '50 L to 70 L '),
    ('70-90', '70 L to 90 L '),
    ('90-120', '90 L to 1.20 Cr '),
    ('120-140','1.20 Cr to 1.40 Cr'),
    ('140-160','1.40 Cr to 1.60 Cr'),
    ('160-180','1.60 Cr to 1.80 Cr'),
    ('180-200','1.80 Cr to 2.00 Cr'),
    ('200-250','2.00 Cr to 2.50 Cr'),
    ('250-300','2.50 Cr to 3.00 Cr'),
    ('300-350','3.00 Cr to 3.50 Cr'),
    ('350+','3,50 Cr +'),
)

PURPOSE = (
    ('INV','Investment'),
    ('END','End Use'),
)


PROJECT_STATUS = (
    ('R','Ready To Move'),
    ('U', 'Under Construction'),
    ('A', 'Any'),
)

CITY = (
    ('G','Gurgaon'),
    ('N','New Delhi'),
)




# Address Model
class Office_Address(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    office_zone = models.CharField(max_length=100) # give choices
    office_location = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    #    def __str__(self):
    #        return self.user.username


class Residence_Address(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    residence_zone = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)


#    def __str__(self):
#        return self.user.username


# Lead Model
class Lead(models.Model):
    id = models.BigAutoField(primary_key=True) #Modify this field for Date wise pattern
    created_on = models.DateTimeField(auto_now_add = True)
    lead_status = models.CharField(choices=LEAD_STATUS, max_length=1,default="N") # make default new
    #status = models.CharField(choices=,max_length=4)
    #assigned to
    campaign = models.CharField(max_length=30,blank=True ,null=True)

    # basic Info
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30 , blank=True , null=True,default="/")
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    mail = models.EmailField(max_length = 254)

    # Property Info
    property_type = models.CharField(choices=TYPE, max_length=2) # Create Default
    bedrooms = models.CharField(choices=BEDROOMS, max_length=4) # Create Default
    budget_category = models.CharField(choices=BUDGET_CATEGORY, max_length=7)
    budget = models.DecimalField(max_digits=5, decimal_places=2)
    project_status = models.CharField(choices=PROJECT_STATUS, max_length=1)

    # wigdgets
    purpose = models.CharField(choices=PURPOSE, max_length=3,default="END")
    preferred_location = models.CharField(max_length=30,blank=True , null=True)
    remarks = models.TextField(max_length = 254,blank=True , null=True)
    notes = models.TextField(max_length = 254,blank=True , null=True)
    inventory_shared = models.BooleanField(default=False,blank=True , null=True)
    next_call_date = models.DateTimeField()
    #site_visits/meetings =


    #Extra Info
    #
    occupation = models.CharField(max_length=30,blank=True , null=True)
    office_address = models.ForeignKey(Office_Address,on_delete=models.CASCADE,blank=True , null=True)
    residence_address = models.ForeignKey(Residence_Address,on_delete=models.CASCADE,blank=True , null=True)


    def __str__(self):
        return "Lead Id : {0} , Name : {1} {2}                ^^  Create on : {3}".format(self.id,self.first_name,self.last_name,self.created_on)

    def get_absolute_url(self):
        return reverse('dash:detail', kwargs={'pk': self.pk})
