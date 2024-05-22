"""panchayat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from citizen import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    #url('userlogin',views.userlogin,name="userlogin"),
    url('logcheck', views.logcheck, name="logcheck"),
    url('^$', views.index, name="index"),
    url('index',views.index,name='index'),
    url('insertapplicationDetails', views.insertapplicationDetails, name="insertapplicationDetails"),
    url('insertCertificaterequest', views.insertCertificaterequest, name="insertCertificaterequest"),
    url('insertCertificateDetails', views.insertCertificateDetails, name="insertCertificateDetails"),
    url('insertCitizenDetails', views.insertCitizenDetails, name="insertCitizenDetails"),
    url('insertComplaints', views.insertComplaints, name="insertComplaints"),
    url('insertSchemes', views.insertSchemes, name="insertSchemes"),

    url('insertcontact', views.insertcontact,name="insertcontact"),
    url('sendpass', views.sendpass, name="sendpass"),







    #Application detalis view and delete from database
    url('view_applicationsdetails', views.view_applicationsdetails,name="view_applicationsdetails"),
    url('applicationdetails_del/(?P<pk>\d+)/$', views.applicationdetails_del, name='applicationdetails_del'),

    #cdertifiate request view and delete from database
    url('view_certificaterequest', views.view_certificaterequest,name="view_certificaterequest"),
    url('certificaterequest_del/(?P<pk>\d+)/$', views.certificaterequest_del, name='certificaterequest_del'),

    #certifiate detalis view and delete from database
    url('view_certificatedetails', views.view_certificatedetails,name="view_certificatedetails"),
    url('certificatedetails_del/(?P<pk>\d+)/$', views.certificatedetails_del, name='certificatedetails_del'),

    #citizen detalis view and delete from database
    url('view_citizendetails', views.view_citizendetails,name="view_citizendetails"),
    url('citizendetails_del/(?P<pk>\d+)/$', views.citizendetails_del, name='citizendetails_del'),

    #Complaints view and delete from database
    url('view_complaints', views.view_complaints,name="view_complaints"),
    url('complaints_del/(?P<pk>\d+)/$', views.complaints_del, name='complaints_del'),

    #Complaints view and delete from database
    url('view_schemes', views.view_schemes,name="view_schemes"),
    url('schemes_del/(?P<pk>\d+)/$', views.schemes_del, name='schemes_del'),

    #Contact view and delete from database
    url('view_contact', views.view_contact,name="view_contact"),
    url('contact_del/(?P<pk>\d+)/$', views.contact_del, name='contact_del'),
]
