from django.shortcuts import render
from django.contrib import messages
from user.forms import LoginForm, RegisterForm

# Create your views here.
def landing(request):
    return render(request,"auth/landing.html")

def user_register(request):
    form=RegisterForm(request.POST)

    if form.is_valid():
        user=form.save()

    else:
        messages.error(request,"Invalid credentions")
    return render(request,"auth/register.html")



def user_login(request):
    form=LoginForm(request.POST)
    if form.is_valid():
        email=request.POST['email']
        password=request.POST['password']
        
    if request.method == 'POST':

        print('test')
        form = LoginStudentForm(None, data=request.POST)
        print(request.POST)

        print("form is valid")
        # username = form.cleaned_data.get('username')
        username = request.POST['username']
        # print(email)
        # password = form.cleaned_data.get('password')
        password = request.POST['password']
        print(password)
        user = authenticate(username=username, password=password)
        if form.is_valid():
            form.clean()
            user = form.get_user()
            if user is not None:
                login(request, user)

                messages.info(request, 'You have successfully logged in!')
                return redirect('raise-ticket')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
# else:
#     messages.error(request, "Invalid email or password.")

    form = LoginStudentForm()

    return render(request, "student/login.html", {'form': form})