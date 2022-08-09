from email import message
from tabnanny import check
from django.shortcuts import redirect, render
from importlib_metadata import email
from .models import*
from random import randint
# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")


def SignupPage(request):
    return render(request,"app/signup.html")

def RegisterUser(request):
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        fname =request.POST['firstname']
        lname =request.POST['lastname']
        email =request.POST['email']
        password =request.POST['password']
        cpassword =request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message ="User alrady Exist"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand= Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
    else:
    
        if request.POST['role']=="Company":
            role = request.POST['role']
            fname =request.POST['firstname']
            lname =request.POST['lastname']
            email =request.POST['email']
            password =request.POST['password']
            cpassword =request.POST['cpassword']

            user = UserMaster.objects.filter(email=email)
            
            if user:          
                message="User already Exist "
                return render (request,"app/signup.html",{'msg':message})
            else:
                if password == cpassword:
                    otp = randint(100000,999999)
                    newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                    newcand= Company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                    return render(request,"app/otpverify.html",{'email':email})
    # else:
    #     print("Comapny Registration!")


def new_func1(email):
    user = new_func(email)
    return user

def new_func(email):
    user = UserMaster.objects.filter(email=email)
    return user

def OTPPage(request):
    return render (request,"app/otpverify.html")


def OtpVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)
    if user:
        if user.otp == otp:
            message = "OTP Verify Successfully"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "OTP Is Incorrect"
            return render(request,"app/otpverify.html",{'msg':message})
    else:
        return render (request,"app/signup.html")

# I m Creating a  company views

def Loginpage(request):
    return render(request,"app/login.html")

def LoginUser(request):
    if request.POST['role']== "Candidate":
        email =request.POST['email']
        password =request.POST['password']
        user = UserMaster.objects.get(email=email)
        
        if user:
            if user.password==password and user.role=="Candidate":
                can =Candidate.objects.get(user_id=user)
                request.session['id']=user.id
                request.session ['role']=user.role
                request.session ['firstname'] = can.firstname
                request.session['lastname']= can.lastname
                request.session['email']= user.email
                return redirect('index')
            else:
                message="Password doesnot match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message="User doesnot exist"
            return render(request,"app/login.html",{'msg':message})
    else:
        if request.POST ['role'] =="Company":
            email = request.POST['email']
            password = request.POST['password']

            user = UserMaster.objects.get(email=email)

      ########################Company Role#########################      
            if user:

                if user.password==password and user.role=="Company":
                    comp=Company.objects.get(user_id=user)
                    request.session['id']=user.id 
                    request.session ['role']=user.role
                    request.session ['firstname'] = comp.firstname
                    request.session['lastname']= comp.lastname
                    request.session['email']= user.email
                    return redirect('companyindex')                 
                else:
                    message="Password doesnot match"
                    return render(request,"app/login.html",{'msg':message})
            else:
                message="User doesnot exist"
                return render(request,"app/login.html",{'msg':message})
      

def ProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)
    return render (request,"app/profile.html",{'user':user,'can':can})
                                              
    
def Logoutpage (request):
    return render (request,"app/signup.html")

def Updateprofile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role =="Candidate":
        can = Candidate.objects.get(user_id=user)
        can.state = request.POST ['state'] #First country this belong to Database field and secound belongs to HTML input name 
        can.city = request.POST ['city']
        can.jobtype = request.POST ['jobtype']
        can.country = request.POST ['country']
        can.jobcategory = request.POST ['jobcategory']
        can.highestedu = request.POST ['eduction']
        can.experience = request.POST ['experience']
        can.website = request.POST ['website']
        can.shift = request.POST ['shift']
        can.jobdescription = request.POST ['description']
        can.min_salary = request.POST ['minsalary']
        can.max_salary = request.POST ['maxsalary']
        can.contact = request.POST ['contact']
        can.gender = request.POST ['gender']
        can.profile_pic = request.FILES ['image']
        can.save()
        print("Data SAVED")
        url = f'/profile/{pk}'#Formating URL
        return redirect(url)


########################################Company side##################################

def CompanyIndexPage(request):
    return render(request,"app/company/index.html")
    
## I am creating Logout views
def LogoutPage(request):
    return render(request,"app/signup.html")

def CompanyProfilePage(request,pk):
    user =UserMaster.objects.get(pk=pk)
    comp =Company.objects.get(user_id=user)
    return render(request,"app/company/profile.html",{'user':user,'comp':comp})

def UpdateCompanyProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role =="Company":
        comp =Company.objects.get(user_id=user) 
        comp.Firstname = request.POST ['firstname']
        comp.Lastname = request.POST ['firstname']
        comp.city = request.POST ['city']
        comp.website = request.POST ['website']
        comp.contact = request.POST ['contact']
        comp.profile_pic = request.FILES ['image']
        comp.save()
        url = f"/companyprofile/{pk}"#Formating URL
        return redirect(url)

def JobPostPage(request):
    return render (request,"app/company/jobpost.html")


    

    
        
    
    
        
      

        

    

            


                


    



    

    
    
        

     
        
     
