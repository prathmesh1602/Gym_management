from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact,MembershipPlan,Trainer,Enrollment,Gallary,Attendence,Services

def home(request):
        user_phone=request.user
        post=Enrollment.objects.filter(PhoneNumber=user_phone)
        context={"post":post}
        return render(request, 'index.html',context)

    


def signin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signin')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signin')
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signin')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signin')
           
        except Exception as identifier:
            pass
        
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request," Signin Successfuly!! ")
        return redirect('/login')     

    return render(request, 'signin.html')


def handalelogin(request):
    if request.method =="POST":
        username=request.POST.get("usernumber")
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request, 'Login Successfuly!!')
            return redirect("/")
        else:
            messages.error(request, 'Invalid Data')  
            return redirect("/login")  

    return render(request, 'login.html')
    
def handaleLogout(request):
    logout(request)
    messages.success(request, "Logout Successfuly!!")   
    return redirect('/login')

def contact(request):
    if request.method =="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("num")
        desc=request.POST.get("desc")
        myquery=Contact(name=name,email=email,pnumbner=number,description=desc)
        myquery.save()

        messages.info(request, "Thanks for Contacting Us We Will Get Back You Soon")
        return redirect("/contact")

    return render(request, 'contact.html')    
def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login And Try Again")
        return redirect("/login")
    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        Fullname=request.POST.get("Fullname")
        email=request.POST.get("email")
        PhoneNumber=request.POST.get("PhoneNumber")
        DOB=request.POST.get("DOB")
        gender=request.POST.get("gender")
        trainer=request.POST.get("trainer")
        member=request.POST.get("member")
        reference=request.POST.get("reference")
        address=request.POST.get("address")
        paymentstatus=request.POST.get("paymentstatus")
        amountpaid=request.POST.get("amountpaid")
        query=Enrollment(fullname=Fullname,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,
        SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address,paymentStatus=paymentstatus,Amount=amountpaid)
        query.save()
        messages.success(request, "Thanks For Enrollment")
        return redirect("/join")
    return render(request, 'enroll.html',context)   
def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login And Try Again")
        return redirect("/login")
    user_phone=request.user
    post=Enrollment.objects.filter(PhoneNumber=user_phone)
    attendance=Attendence.objects.filter(phonenumber=user_phone)
    print(attendance)
    context={"post":post,"attendance":attendance}
    return render(request, 'profile.html',context) 
    
def gallery(request):
    posts=Gallary.objects.all()
    context={'posts':posts}
    return render(request, 'gallery.html',context)
    

def attendance(request):
     if not request.user.is_authenticated:
        messages.warning(request, "Please Login And Try Again")
        return redirect("/login")
     SelectTrainer=Trainer.objects.all()
     context={'SelectTrainer':SelectTrainer}
     if request.method=="POST":
        Phonenumber=request.POST.get("PhoneNumber")
        login=request.POST.get("logintime")
        logout=request.POST.get("logintime")
        selectworkout=request.POST.get("workout")
        trainedby=request.POST.get("trainer")
        query=Attendence(phonenumber=Phonenumber,login=login,logout=logout,selectworkout=selectworkout,trainedby=trainedby)
        query.save()
        messages.success(request, "Attendencw Apply Successfuly!!!")
        return redirect("/attendance")
     return render(request, 'attendance.html',context)    
def services(request):  
    posts=Services.objects.all()
    context={'posts':posts}
    return render(request, 'services.html',context) 

    
from django.shortcuts import render

def calculate_bmi(request):
    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        bmi = round(weight / (height * height) * 703, 2)
        if bmi < 18.5:
            result = f"BMI : {bmi:.2f},Underweight"
            return render(request, 'bmi.html', {'result': result})
        
                
        elif bmi <= 24.9:
                result = f" BMI : {bmi:.2f},Normal"
                return render(request, 'bmi.html', {'result': result})
        elif bmi <= 29.9:
                result = f" BMI : {bmi:.2f},Overweight"
                return render(request, 'bmi.html', {'result': result})
        
                
        else:
           result = f"BMI : {bmi:.2f},Obese.."
           return render(request, 'bmi.html', {'result': result})
       
    else:
        result = ''
        
    return render(request, 'bmi.html')

def Workout(request): 
    posts=Gallary.objects.all()
    context={'posts':posts}
    return render(request, "Workout.html",context)       
         
    
         