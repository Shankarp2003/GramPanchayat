from django.db import models


# Create your models here.
class userlogin(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    utype = models.CharField(max_length=20)


class applicationdetails(models.Model):
    Application_id = models.CharField(max_length=50)
    Application_type = models.CharField(max_length=255)
    Aadhar_no = models.CharField(max_length=50)
    Name = models.CharField(max_length=255)
    Details = models.CharField(max_length=255)
    Date = models.CharField(max_length=50)
    Time = models.CharField(max_length=50)
    Status = models.CharField(max_length=255)



class certificaterequest(models.Model):
    Request_id = models.CharField(max_length=50)
    Scheme_id = models.CharField(max_length=50)
    Aadhar_no = models.CharField(max_length=50)
    Apply_date = models.CharField(max_length=50)
    Status = models.CharField(max_length=255)



class certificatedetails(models.Model):
    Request_id = models.CharField(max_length=50)
    Certificate_no = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    Issue_Date = models.CharField(max_length=50)
    Name = models.CharField(max_length=255)
    Father_Name = models.CharField(max_length=255)
    Mother_Name = models.CharField(max_length=255)
    Reason = models.CharField(max_length=1000)
    Date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    status = models.CharField(max_length=255)



class citizendetails(models.Model):
    Aadhar_no = models.CharField( max_length=50)
    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Father_name = models.CharField(max_length=255)
    Mother_name = models.CharField(max_length=255)
    DateOfBirth = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Mobile_no = models.CharField(max_length=15)
    Cast = models.CharField(max_length=255)
    Sub_Cast = models.CharField(max_length=255)


class complaints(models.Model):
    Complaints_id = models.CharField(max_length=50)
    Givenby = models.CharField(max_length=255)
    Complaints_On = models.CharField(max_length=255)
    Date = models.CharField(max_length=50)
    Time = models.CharField(max_length=50)


class schemes(models.Model):
    Schemes_id = models.CharField(max_length=50)
    Schemes_name = models.CharField(max_length=255)
    Details = models.CharField(max_length=500)
    Release_Details = models.CharField(max_length=255)
    Start_Date = models.CharField(max_length=20)
    Eligibility = models.CharField(max_length=255)
    Releasedby = models.CharField(max_length=255)
    Min_age = models.CharField(max_length=50)
    Max_age = models.CharField(max_length=50)
    Mobile_no = models.CharField(max_length=15)

class contact(models.Model):
    Name = models.CharField(max_length=50)
    Email_id = models.CharField(max_length=50)
    Message = models.CharField(max_length=500)
    Feedback = models.CharField(max_length=250)
















from django.db import models


# Create your models here.
class userlogin(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    utype = models.CharField(max_length=20)


class applicationdetails(models.Model):
    Application_id = models.CharField(max_length=50)
    Application_type = models.CharField(max_length=255)
    Aadhar_no = models.CharField(max_length=50)
    Name = models.CharField(max_length=255)
    Details = models.CharField(max_length=255)
    Date = models.CharField(max_length=50)
    Time = models.CharField(max_length=50)
    Status = models.CharField(max_length=255)



class certificaterequest(models.Model):
    Request_id = models.CharField(max_length=50)
    Scheme_id = models.CharField(max_length=50)
    Aadhar_no = models.CharField(max_length=50)
    Apply_date = models.CharField(max_length=50)
    Status = models.CharField(max_length=255)



class certificatedetails(models.Model):
    Request_id = models.CharField(max_length=50)
    Certificate_no = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    Issue_Date = models.CharField(max_length=50)
    Name = models.CharField(max_length=255)
    Father_Name = models.CharField(max_length=255)
    Mother_Name = models.CharField(max_length=255)
    Reason = models.CharField(max_length=1000)
    Date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    status = models.CharField(max_length=255)



class citizendetails(models.Model):
    Aadhar_no = models.CharField( max_length=50)
    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Father_name = models.CharField(max_length=255)
    Mother_name = models.CharField(max_length=255)
    DateOfBirth = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Mobile_no = models.CharField(max_length=15)
    Cast = models.CharField(max_length=255)
    Sub_Cast = models.CharField(max_length=255)


class complaints(models.Model):
    Complaints_id = models.CharField(max_length=50)
    Givenby = models.CharField(max_length=255)
    Complaints_On = models.CharField(max_length=255)
    Date = models.CharField(max_length=50)
    Time = models.CharField(max_length=50)


class schemes(models.Model):
    Schemes_id = models.CharField(max_length=50)
    Schemes_name = models.CharField(max_length=255)
    Details = models.CharField(max_length=500)
    Release_Details = models.CharField(max_length=255)
    Start_Date = models.CharField(max_length=20)
    Eligibility = models.CharField(max_length=255)
    Releasedby = models.CharField(max_length=255)
    Min_age = models.CharField(max_length=50)
    Max_age = models.CharField(max_length=50)
    Mobile_no = models.CharField(max_length=15)

class contact(models.Model):
    Name = models.CharField(max_length=50)
    Email_id = models.CharField(max_length=50)
    Message = models.CharField(max_length=500)
    Feedback = models.CharField(max_length=250)
















