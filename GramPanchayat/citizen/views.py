import smtplib

from django.shortcuts import render

from citizen.models import applicationdetails

from citizen.models import certificaterequest
from citizen.models import schemes
from citizen.models import complaints
from citizen.models import citizendetails
from citizen.models import certificatedetails
from citizen.models import contact
from citizen.models import userlogin


# Create your views here.
def index(request):
    return render(request, "index.html")


# create user login page
# def userlogin(request):
#     if request.method == 'POST':
#         s1 = request.POST.get("t1")
#         s2 = request.POST.get("t2")
#         userlogin.objects.create(username=s1, password=s2)
#         return render(request, "userlogin_page.html")
#
#     return render(request, "userlogin_page.html")

def logcheck(request):
    if request.method == "POST":
        s1 = request.POST.get("t1")
        request.session['username'] = s1
        s2 = request.POST.get("t2")
        ucheck = userlogin.objects.filter(username=s1).count()
        if ucheck >= 1:
            udata = userlogin.objects.get(username=s1)
            upass = udata.password
            utype = udata.utype
            if upass == s2:
                if utype == "admin":
                    return render(request, 'admin_page.html')
                if utype == "citizen":
                    return render(request, 'citizen_page.html')
            else:
                return render(request, 'userlogin_page.html', {'msg': 'invalid password'})
        else:
            return render(request, 'userlogin_page.html', {'msg': 'invalid username'})
    return render(request, "userlogin_page.html")


def insertcontact(request):
    if (request.method == 'POST'):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        contact.objects.create(Name=s1, Email_id=s2, Message=s3, Feedback=s4)
        return render(request, "contact.html")

    return render(request, "contact.html")


def insertapplicationDetails(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        applicationdetails.objects.create(Application_id=s1, Application_type=s2, Aadhar_no=s3, Name=s4, Details=s5,
                                          Date=s6, Time=s7, Status=s8)

        return render(request, "'Application_Details'.html")
    return render(request, "'Application_Details'.html")


def insertCertificaterequest(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")

        certificaterequest.objects.create(Request_id=s1, Scheme_id=s2, Aadhar_no=s3, Apply_date=s4, Status=s5)

        return render(request, "'Certificate_request'.html")

    return render(request, "'Certificate_request'.html")


def insertCertificateDetails(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s9 = request.POST.get("t9")
        s8 = request.POST.get("t8")
        s10 = request.POST.get("t10")
        s11 = request.POST.get("t11")
        certificatedetails.objects.create(Request_id=s1, Certificate_no=s2, Type=s3, Issue_Date=s4, Name=s5,
                                          Father_Name=s6, Mother_Name=s7, Reason=s8, Date=s9, time=s10, status=s11)

        return render(request, "'CertificateDetails'.html")
    return render(request, "'CertificateDetails'.html")


def insertCitizenDetails(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        s10 = request.POST.get("t10")
        citizendetails.objects.create(Aadhar_no=s1, First_name=s2, Last_name=s3, Father_name=s4, Mother_name=s5,
                                      DateOfBirth=s6, Gender=s7, Mobile_no=s8, Cast=s9, Sub_Cast=s10)

        return render(request, "'CitizenDetails'.html")
    return render(request, "'CitizenDetails'.html")


def insertComplaints(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")

        complaints.objects.create(Complaints_id=s1, Givenby=s2, Complaints_On=s3, Date=s4, Time=s5)

        return render(request, "'Complaints'.html")
    return render(request, "'Complaints'.html")


def insertSchemes(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        s10 = request.POST.get("t10")
        schemes.objects.create(Schemes_id=s1, Schemes_name=s2, Details=s3, Release_Details=s4, Start_Date=s5,
                               Eligibility=s6, Releasedby=s7, Min_age=s8, Max_age=s9, Mobile_no=s10)

        return render(request, "'Schemes'.html")
    return render(request, "'Schemes'.html")


def view_applicationsdetails(request):
    userdict = applicationdetails.objects.all()
    return render(request, "view_'Application_Details'.html", {'userdict': userdict})


def applicationdetails_del(request, pk):
    rid = applicationdetails.objects.get(id=pk)
    rid.delete()
    userdict = applicationdetails.objects.all()
    return render(request, "view_'Application_Details'.html", {'userdict': userdict})


def view_certificaterequest(request):
    userdict = certificaterequest.objects.all()
    return render(request, "views_certificate_request.html", {'userdict': userdict})


def certificaterequest_del(request, pk):
    rid = certificaterequest.objects.get(id=pk)
    rid.delete()
    userdict = certificaterequest.objects.all()
    return render(request, "views_certificate_request.html", {'userdict': userdict})


def view_certificatedetails(request):
    userdict = certificatedetails.objects.all()
    return render(request, "views_certificate_details.html", {'userdict': userdict})


def certificatedetails_del(request, pk):
    rid = certificatedetails.objects.get(id=pk)
    rid.delete()
    userdict = certificatedetails.objects.all()
    return render(request, "views_certificate_details.html", {'userdict': userdict})


def view_citizendetails(request):
    userdict = citizendetails.objects.all()
    return render(request, "view_citizen_details.html", {'userdict': userdict})


def citizendetails_del(request, pk):
    rid = citizendetails.objects.get(id=pk)
    rid.delete()
    userdict = citizendetails.objects.all()
    return render(request, "view_citizen_details.html", {'userdict': userdict})


def view_complaints(request):
    userdict = complaints.objects.all()
    return render(request, "view_complaints.html", {'userdict': userdict})


def complaints_del(request, pk):
    rid = complaints.objects.get(id=pk)
    rid.delete()
    userdict = complaints.objects.all()
    return render(request, "view_complaints.html", {'userdict': userdict})


def view_schemes(request):
    userdict = schemes.objects.all()
    return render(request, "view_schemes.html", {'userdict': userdict})


def schemes_del(request, pk):
    rid = schemes.objects.get(id=pk)
    rid.delete()
    userdict = schemes.objects.all()
    return render(request, "view_schemes.html", {'userdict': userdict})


def view_contact(request):
    userdict = contact.objects.all()
    return render(request, "view_contact.html", {'userdict': userdict})


def contact_del(request, pk):
    rid = contact.objects.get(id=pk)
    rid.delete()
    userdict = contact.objects.all()
    return render(request, "view_contact.html", {'userdict': userdict})


def sendpass(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        udata = userlogin.objects.get(username=s1)
        upass = udata.password
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('zoro11112024@gmail.com', 'gxqj tvgj ktmg onfn')
        mail.sendmail('zoro11112024@gmail.com', s1, upass)
        mail.close()
        return render(request, "userlogin_page.html")
    return render(request, "forgotpassword.html")



