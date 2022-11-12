from django.urls import path
from apps.profiles.views import *
from apps.profiles.apiViews import *

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
	path('home/',home_view, name='home'),
	path('createCustomer/',create_customer_view, name='createCustomer'),
	path('updateCustomer/<int:pk>',update_customer_view, name='updateCustomer'),
	path('readCustomer/',read_customer_view, name='readCustomer'),
	path('apiSendCodeSMS',send_code_sms, name='apiSendCodeSMS'),
	path('apiValidateCodeSMS',validate_code_sms, name='apiValidateCodeSMS')

]