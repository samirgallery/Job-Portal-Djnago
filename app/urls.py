from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("signup/",views.SignupPage,name="signup"),
    path("register/",views.RegisterUser,name="register"),
    path("otppage/",views.OTPPage,name="otppage"),
    path("otp/",views.OtpVerify,name="otp"),
    path("loginpage",views.Loginpage,name="loginpage"),
    path("loginuser/",views.LoginUser,name="login"),
    path("profile/<int:pk>",views.ProfilePage,name="profile"),
    path("logout/",views.Logoutpage,name="logout"),
    path("updateprofile/<int:pk>",views.Updateprofile,name="updateprofile"),

    #path("profile/<int:pk>",views.ProfilePage,name="profile"),


    ########################company side ###################
    path("companyindex/",views.CompanyIndexPage,name="companyindex"),
    path("logoutpage/",views.Logoutpage,name="logoutpage"),
    path("companyprofile/<int:pk>",views.CompanyProfilePage,name="companyprofile"),
    path("updatecompanyprofile/<int:pk>",views.UpdateCompanyProfile,name="updatecompanyprofile"),
    path("jobpostpage/",views.JobPostPage,name="jobpostpage"),
 
  
]
