from django.urls import path
from authapp import views

urlpatterns = [
   path("",views.home,name='home'), 
   path("signin",views.signin,name='signin'),
   path("login",views.handalelogin,name='login'),
   path("logout",views.handaleLogout,name='handaleLogout'),
   path("contact",views.contact,name='contact'),
   path("join",views.enroll,name='enroll'),
   path("profile",views.profile,name='profile'),
   path("gallery",views.gallery,name='gallery'),
   path("attendance",views.attendance,name='attendance'),
   path("services",views.services,name='services'),
   path("bmi",views.calculate_bmi,name='bmi'),
   path("Workout",views.Workout,name='Workout'),
]
