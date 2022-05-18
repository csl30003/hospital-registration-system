#coding = utf-8
from django.urls import path
from .views import *

urlpatterns=[
    path('',ChooseLoginView.as_view()),
    path('patientlogin/',PatientLoginView.as_view()),
    path('doctorlogin/',DoctorLoginView.as_view()),
    path('patientregister/',PatientRegisterView.as_view()),
    path('patientcenter/',PatientCenterView.as_view()),
    path('choosedepartment/',ChooseDepartmentView.as_view()),
    path('choosedoctorandtime/<int:department_id>/',ChooseDoctorAndTimeView.as_view()),
    path('confirmregistration/<int:department_id>/<int:doctor_id>/<str:consultation_hours>/',ConfirmRegistrationView.as_view()),
    path('confirmregistration/',ConfirmRegistrationView.as_view()),
]