from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm,AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login as loginUser ,logout
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

# @login_required(login_url='login')
# def home(request):
#     # Ensure the user is authenticated
#     Student_data = Student.objects.filter(user_id=request.user)
    
#     if request.method == "POST":
#         student_form = StudentForm(request.POST, request.FILES)
#         if student_form.is_valid():
#             usr = request.user
#             nm = student_form.cleaned_data['name']
#             ad = student_form.cleaned_data['Address']  # Use 'address' as per the model field
#             rl = student_form.cleaned_data['roll']
#             ia = student_form.cleaned_data['Active']
#             img = student_form.cleaned_data['image']  # Use 'active' as per the model field
#             reg = Student(name=nm, Address=ad, roll=rl, Active=ia, user_id=usr,image=img)  # Use 'user' instead of 'user_id'
#             reg.save()
#             messages.success(request, 'Your Data Added Successfully')
#             student_form = StudentForm()  # Reset the form after submission
#     else:
#         student_form = StudentForm()  # Instantiate the form correctly

#     return render(request, 'app/index.html', {'stu_name': Student_data, 'form': student_form})

# @login_required(login_url='login')
# def home(request):
#     # Ensure the user is authenticated and filter the data for the logged-in user
#     Student_data = Student.objects.filter(user=request.user)
    
#     if request.method == "POST":
#         student_form = StudentForm(request.POST, request.FILES)
#         if student_form.is_valid():
#             usr = request.user
#             nm = student_form.cleaned_data['name']
#             ad = student_form.cleaned_data['Address']  # Use 'address' as per the model field
#             #rl = student_form.cleaned_data['roll']
#             sb = student_form.cleaned_data['subject']
#             ia = student_form.cleaned_data['Active']  # Use 'active' as per the model field
#             img = student_form.cleaned_data['image']  # Handle image correctly
#             cost = student_form.cleaned_data['cost']
#             # Save the student data
#             reg = Student(name=nm, Address=ad, subject=sb, Active=ia, user=usr, image=img, cost=cost)
#             #reg = Student(name=nm, Address=ad, roll=rl, Active=ia, user=usr, image=img)
#             studentt = reg.save(commit=False)
#             studentt.cost=studentt.get_subject_cost()
#             studentt.save()

            
#             messages.success(request, 'Your Data Added Successfully')
#             student_form = StudentForm()  # Reset the form after submission
#     else:
#         student_form = StudentForm()  # Instantiate the form correctly

#     return render(request, 'app/index.html', {'stu_name': Student_data, 'form': student_form})
@login_required(login_url='login')
def home(request):
    # Ensure the user is authenticated and filter the data for the logged-in user
    student_data = Student.objects.filter(user=request.user)
    
    if request.method == "POST":
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():
            # Create an instance of the Student model from the form, but don't save it yet
            student = student_form.save(commit=False)
            student.user = request.user  # Set the user field
            student.cost = student.get_subject_cost()  # Set cost based on subject
            student.save()  # Save the student instance
            
            messages.success(request, 'Your data was added successfully!')
            student_form = StudentForm()  # Reset the form after submission
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        student_form = StudentForm()  # Instantiate the form correctly

    return render(request, 'app/index.html', {'stu_name': student_data, 'form': student_form})

@login_required(login_url='login')
def update(request, id):
    p = Student.objects.get(pk=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data has been updated")
            return redirect('home')
    else:
        form = StudentForm(instance=p)

    return render(request, 'app/update.html', {'form': form})

@login_required(login_url='login')
def delete(request, id):
    if request.method == "POST":
        p = Student.objects.get(pk=id)
        p.delete()
        messages.success(request, "Your Data Deleted successfully!!!")
        return redirect('home')
    # if request.method == "POST":
    #     p = Student.objects.get(pk=id)
    #     p.delete()
    #     messages.success(request, "Your data has been deleted")
    #     return redirect('home')


def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request,'app/signup.html',{'form':form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
            
        else:
            return render (request,"app/signup.html",{'form':form})
        

def login(request):
    if request.method =="GET":
        form = AuthenticationForm()
        return render (request,'app/login.html',{'form':form})
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            return render (request,'app/login.html',{'form':form})
        

def signout(request):
    logout(request)
    return redirect('login')

def MainPage(request):

    return render(request, 'app/home.html')



class StudentModel(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

def Aboutus(request):

    return render(request, 'app/aboutus.html')

def course(request):

    return render(request, 'app/course.html')


