from django import forms 
from accounts.models import TypeApproval,DealershipLicense
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget,RegionalPhoneNumberWidget
from phonenumber_field.modelfields import PhoneNumber
from django.utils import timezone






CLASSNAME='mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'


class TypeApprovalForm(forms.ModelForm):
    class Meta:
        model = TypeApproval
        #fields = "__all__"
        exclude = ['customer','status']


    company_name = forms.CharField(max_length=100,label="Company Name", widget=forms.TextInput(attrs={
        'class': "mt-1 block w-full px-3 py-2 border border-gray-300  shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    contact_person = forms.CharField(max_length=100,label="Contact Person", widget=forms.TextInput(attrs={
        'class':'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    
    postal_address = forms.CharField(max_length=255,label="Postal Address", widget=forms.Textarea(attrs={

        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    phone_no = PhoneNumberField()
    
    phone_no2 = PhoneNumberField()

    fax_no = forms.CharField(max_length=100,label="Fax Number", widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    email = forms.CharField(label="Email",widget=forms.EmailInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    
    alt_email = forms.CharField(label="Alternative Email",widget=forms.EmailInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))


    product_type = forms.CharField(max_length=100, label="Product Type",widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    brand_name = forms.CharField(max_length=100, label="Brand Name",widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    model_no = forms.CharField(max_length=50, label="Product Model Number",widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    product_no = forms.CharField(max_length=50, label="Product Number" ,widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    product_name = forms.CharField(max_length=100,label="Product Name", widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    software_version = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    antenna_type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    antenna_gain = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    technical_variants = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))


    issue_body = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    issue_date = forms.CharField(widget=forms.DateInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
        'type':'date',

        'placeholder':'yyyy-mm-dd'
    })) 


    validity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))


    emc = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    radio = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))

    health_and_safety = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))



#new forms for multiple forms or sliding 

#company info form


class CompanyInfoForm(forms.Form):
    class Meta:
        model = TypeApproval
        fields = ('company_name', 'contact_person', 'postal_address','phone_no', 'phone_no2', 'fax_no', 'email', 'alt_email')
        

    company_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'w-full'
    }))
    contact_person = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
      'class':'w-full'
    }))
    postal_address = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    phone_no = PhoneNumberField(
        widget=RegionalPhoneNumberWidget(region='GH', attrs={
            'class': 'w-full'
        })
    )
    phone_no2 = PhoneNumberField(
        widget=RegionalPhoneNumberWidget(region='GH', attrs={
            'class':'w-full'
        })
    )
       
    fax_no = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
        'class':'w-full'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'w-full'
    }))
    alt_email = forms.CharField(required=False, widget=forms.EmailInput(attrs={
        'class':'w-full'
    }))


    #product info form
class ProductInfoForm(forms.Form):
    product_type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    brand_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    model_no = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    product_no = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    product_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    software_version = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    antenna_type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    antenna_gain = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    technical_variants = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))


    # approval detail info form

class ApprovalDetailsForm(forms.Form):
    issue_body = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    issue_date = forms.CharField(widget=forms.DateInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
        'placeholder':'yyyy-mm-dd',
        'type':'date'
    }))
    validity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    emc = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    radio = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))
    health_and_safety = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class':"mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    }))



# DEALERSHIP FORMS
class serviceOptionForm(forms.ModelForm):
    class Meta:
        model = DealershipLicense
        fields = ('cls_options', 'equipments')

        widgets = {
            'cls_options':forms.RadioSelect(attrs={
                'class':'font-bold text-gray-800 text-xl',
            }),


            'equipments':forms.Textarea(attrs={
                'class':'w-full h-40 p-2O px-3 py-2 border-2 border-dashed rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-solid',
                'placeholder':'Enter equipment and/or services you intend to provide here... '
            })
        
        }
class corporateProfileForm(forms.ModelForm):
    class Meta:
        model = DealershipLicense
        fields = (
            'reg_company_name', 'reg_trade_name', 'reg_company_num', 'tin_num','incorporation_date',
            'commencement_date', 'district', 'town', 'region', 'postal_addr',
            'gps', 'tele_num', 'phone_num', 'site', 'fax'
        )

    reg_company_name = forms.CharField(widget=forms.TextInput(attrs={}),label='Registered Name Of Company')

    reg_trade_name = forms.CharField(label='Registered Trade Name(If Any)')

    reg_company_num = forms.CharField(max_length=8,label='Company Registration Number', widget=forms.TextInput(attrs={
        'placeholder': 'e.g XXXXXXXX'
    }))

    tin_num = forms.CharField(max_length=11,required=True,label='Taxpayer Identification Number(TIN)', widget=forms.TextInput(attrs={
        'placeholder':'e.g AXXXXXXXXXX'
    }))

    postal_addr = forms.CharField(label='Postal Address')
    
    gps = forms.CharField(label='Digital Addres (Ghana Post)')

    #tele_num = forms.CharField(label='Telephone Number')
    tele_num = PhoneNumber()

    phone_num = PhoneNumber()

    site = forms.URLField(label='Website', widget=forms.URLInput(attrs={
        'placeholder': 'www.example.com'
    }))

    fax = forms.CharField(label='Fax (if applicable)')


    
    incorporation_date = forms.CharField(widget=forms.DateInput(attrs={
        'type':'date',
        'placeholder':'yyyy-mm-dd'
    }, format='%Y-%m-%d'), label='Date Of Incorporation')
    
    commencement_date = forms.CharField(label='Date Of Commencement',widget=forms.DateInput(attrs={
        'type':'date',
        'placeholder':'yyyy-mm-dd'
    }, format='%Y-%m-%d'))

class contactInformationForm(forms.ModelForm):
    class Meta:
        model = DealershipLicense
        fields = ('auth_rep_name', 'auth_rep_tele_num', 'email')

    auth_rep_name = forms.CharField(max_length=100, label='Authorization Representative Name')
    auth_rep_tele_num = PhoneNumber()

class ownershipForm(forms.ModelForm):
    class Meta:
        model = DealershipLicense
        fields = ('shareholder_name', 'sharehold', 'nationality', 'address', 'shareholder_tin_num')

    sharehold = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={}))

    shareholder_tin_num = forms.CharField(max_length=11,label="Shareholder Taxpayer Identification Number (TIN)", widget=forms.TextInput(attrs={
        'placeholder':'e.g C00XXXXXXXX'
    }))

class directorsForm(forms.ModelForm):
    class Meta:
        model = DealershipLicense
        fields = ('d_name', 'd_nationality', 'd_address', 'd_tin_num')

    d_name = forms.CharField(label="Director's Name")
    d_nationality = forms.CharField(label="Director's Nationality")
    d_address = forms.CharField(label="Director's Address")
    d_tin_num = forms.CharField(max_length=11,label="Director's TIN Number", widget=forms.TextInput(attrs={
        'placeholder':'CXXXXXXXXXX'
    }))

class evidenceForm(forms.ModelForm):
    class Meta:
        model = DealershipLicense
        fields = (
            'incorporation_cert','commence_cert','share_cert',
            'gipc_cert', 'tax_cert', 'ssnit_cert', 'afiliate_cert','tech_stuff',
            'company_profile_atch'
        )
        
    incorporation_cert = forms.FileField(label='Certification Of Incorporation (in Ghana)', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500  file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700',
    }))

    

    commence_cert = forms.FileField(label='Certificate to Commence Business (in Ghana)', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500  file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700',
    }))

    share_cert = forms.FileField(label='Shareholders/Company Regualtions', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500  file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700',
    }))
    
    gipc_cert = forms.FileField(label='GIPC Certificate (where applicable)', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500  file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700',
    }))

    tax_cert = forms.FileField(label='Tax Clearance Certificate', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500  file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700',
    }))
    
    ssnit_cert = forms.FileField(label='SSNIT Clearance Certificate for Existing Companies', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500  file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700',
    }))
    
    afiliate_cert = forms.FileField(label='List of Afiliate Companies', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500  file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700',
    }))
    
    tech_stuff = forms.FileField(label='Profile Of Technical Staff', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500  file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700',
    }))
    
    company_profile_atch = forms.FileField(label='Company Profile', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500  file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700',
    }))
    
   

class businessForm(forms.ModelForm):
    class Meta:
        model = DealershipLicense
        fields = ('market_plan_atch', 'financial_report_atch', 'bank_receipt')
        
    market_plan_atch = forms.FileField(label='Marketing Plan', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500 file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700'
    }))

    financial_report_atch = forms.FileField(label='Financial Reports', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500 file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700'
    }))

    bank_receipt = forms.FileField(label='Bank Receipt/ Bank Transfer', widget=forms.FileInput(attrs={
        'accept':'.pdf',
        'class':'block w-full text-sm text-gray-500 file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700'
    }))

    '''
    
        widgets = {
            'market_plan_atch': forms.FileInput(attrs={
                'accept':'.pdf',
                'class':'block w-full text-sm text-gray-500 file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700'
            }),
            'financial_report_atch': forms.FileInput(attrs={
                'accept':'.pdf',
                'class':'block w-full text-sm text-gray-500 file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700'
            }),
            'bank_receipt': forms.FileInput(attrs={
                'accept':'.pdf',
                'class':'block w-full text-sm text-gray-500 file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700'
            })
        }
    '''

class othersForm(forms.ModelForm):
    class Meta:
        model = DealershipLicense
        fields = ('num_employee', 'num_employee_props', 'oath', 'date', 'passport')

    num_employee = forms.IntegerField(min_value=0,label='Number Of Employees (Proposed)', widget=forms.NumberInput(attrs={
        
    }))
    num_employee_props = forms.IntegerField(min_value=0,label='Number Of Employees (Actual)', widget=forms.NumberInput(attrs={
        
    }))

    oath = forms.CharField(max_length=250, label='Authorization ')

    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={
        'type':'date',
        'placeholder': 'yyyy-mm-dd',
    }, format='%Y-%m-%d'))

    passport = forms.FileField(label='Passport Picture', widget=forms.FileInput(attrs={
        'accept':'.png, .jpg',
        'class':'block w-full text-sm text-gray-500 file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700'
    }))

    '''
        widgets = {
            'date': forms.DateInput(attrs={
                'type':'date',
                'placeholder': 'yyyy-mm-dd',
                
            }, format='%Y-%m-%d'),

            'passport': forms.FileInput(attrs={
                'accept':'.png, .jpg',
                 'class':'block w-full text-sm text-gray-500 file:mr-4 file:py-2 px-4 rounded-md border-0 text-sm font-semibold border border-2 border-solid file:bg-blue-50 file:text-blue-700'
            })

        }
    '''



