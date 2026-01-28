from django.shortcuts import render, get_object_or_404, redirect
from .models import User

# Home page
def index(request):
    return render(request, 'index.html')

# Static pages
def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    return render(request, 'contact.html')

# User registration page
def userreg(request):
    return render(request, 'demo.html')

# Insert user
def insertuser(request):
    if request.method == "POST":
        vuid = request.POST['uid']
        vuname = request.POST['name']
        vuemail = request.POST['email']
        vucont = request.POST['contact']
        feedback = request.POST.get('feedback')

        us = User(uid=vuid, name=vuname, email=vuemail, contact=vucont,feedback=feedback)
        us.save()

        return redirect('/')

# View all users
def viewuser(request):
    users = User.objects.all()
    return render(request, 'table.html', {'users': users})

# Edit user
def edituser(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'edit.html', {'user': user})

# Update user
def updateuser(request, id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=id)
        user.uid = request.POST['uid']
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.contact = request.POST['contact']
        user.save()
        return redirect('viewuser')

# Delete user
def deleteuser(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('viewuser')
