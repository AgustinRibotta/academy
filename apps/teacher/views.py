# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Teacher
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404


def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fName')
        lname = request.POST.get('lName')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cPassword = request.POST.get('cPassword')

        if password != cPassword:
            messages.error(request, "Passwords do not match.")
            return render(request, 'teacher/register.html')

        if Teacher.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'teacher/register.html')

        teacher = Teacher(
            fname=fname,
            lname=lname,
            username=username,
            password=make_password(password)
        )
        teacher.save()
        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'teacher/register.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fName')
        lname = request.POST.get('lName')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cPassword = request.POST.get('cPassword')

        if password != cPassword:
            messages.error(request, "Passwords do not match.")
            return render(request, 'teacher/register.html')

        if Teacher.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'teacher/register.html')

        teacher = Teacher(
            fname=fname,
            lname=lname,
            username=username,
            password=make_password(password)
        )
        teacher.save()
        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'teacher/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            teacher = Teacher.objects.get(username=username)
        except Teacher.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

        if teacher.check_password(password):
            request.session['teacher_id'] = teacher.id
            messages.success(request, f"Login successful! Welcome {username}")
            return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'teacher/login.html')


def update(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login')

    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        fname = request.POST.get('fName')
        lname = request.POST.get('lName')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cPassword = request.POST.get('cPassword')

        if password and password != cPassword:
            messages.error(request, "Passwords do not match.")
            return render(request, 'teacher/update.html', {'teacher': teacher})

        teacher.fname = fname
        teacher.lname = lname
        teacher.username = username

        if password:
            teacher.set_password(password)

        teacher.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('update')

    return render(request, 'teacher/update.html', {'teacher': teacher})


def logout(request):
    request.session.flush()  
    messages.success(request, "Logged out successfully!")
    return redirect('login')