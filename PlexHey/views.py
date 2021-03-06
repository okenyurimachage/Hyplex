from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, EditProfileForm, ProfileForm,PasswordForm, EditProfile
from .models import feedback,model1,booking,make1
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator
from django.shortcuts import render
from .filters import UserFilter
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View 
from mpesa.implementation.lipanampesa import lipa_na_mpesa
from .documents import PostDocument
from mpesa.models import LNMonline


class CoupesListView(ListView):
    template_name = 'Hey_Plex/Coupes.html'
    context_object_name = 'coupe'
    ordering = ['-created_at']
    paginate_by = 3

    def get_queryset(self):
      return model1.objects.filter(car_make=2)

class CoupesDetailView(DetailView):
    model = model1
    template_name = 'Hey_Plex/details1.html'


class HatchListView(ListView):
    template_name = 'Hey_Plex/hatchback.html'
    context_object_name = 'hatchback'

    def get_queryset(self):
      return model1.objects.filter(car_make=1)

class HatchDetailView(DetailView):
    model = model1
    template_name = 'Hey_Plex/details1.html'

class convertibleListView(ListView):
    template_name = 'Hey_Plex/convertible.html'
    context_object_name = 'convertible'

    def get_queryset(self):
      return model1.objects.filter(car_make=3)

class convertibleDetailView(DetailView):
    model = model1
    template_name = 'Hey_Plex/details1.html'


class sedanListView(ListView):
    template_name = 'Hey_Plex/sedan.html'
    context_object_name = 'sedan'

    def get_queryset(self):
      return model1.objects.filter(car_make=4)

class sedanDetailView(DetailView):
    model = model1
    template_name = 'Hey_Plex/details1.html'

class suvListView(ListView):
    template_name = 'Hey_Plex/suv.html'
    context_object_name = 'suv'

    def get_queryset(self):
      return model1.objects.filter(car_make=5)

class suvDetailView(DetailView):
    model = model1
    template_name = 'Hey_Plex/details1.html'

class mpvListView(ListView):
    template_name = 'Hey_Plex/mpv.html'
    context_object_name = 'mpv'

    def get_queryset(self):
      return model1.objects.filter(car_make=6)

class mpvDetailView(DetailView):
    model = model1
    template_name = 'Hey_Plex/details1.html'

class crossoverListView(ListView):
    template_name = 'Hey_Plex/crossover.html'
    context_object_name = 'crossover'

    def get_queryset(self):
      return model1.objects.filter(car_make=7)

class crossoverDetailView(DetailView):
    model = model1
    template_name = 'Hey_Plex/details1.html'

class pickupListView(ListView):
    template_name = 'Hey_Plex/pickups.html'
    context_object_name = 'pickups'

    def get_queryset(self):
      return model1.objects.filter(car_make=26)

class pickupDetailView(DetailView):
    model = model1
    template_name = 'Hey_Plex/details1.html'

class extrasListView(ListView):
    template_name = 'Hey_Plex/extras.html'
    context_object_name = 'extras'

    def get_queryset(self):
      return model1.objects.filter(car_make=27)

class extrasDetailView(DetailView):
    model = model1
    template_name = 'Hey_Plex/details1.html'


def home(request):
    return render(request,'Hey_Plex/home.html', {})

def feeditback(request):
    return render(request,'Hey_Plex/feeditback.html', {})

def help(request):
    return render(request,'Hey_Plex/help.html', {})

def help1(request):
    return render(request,'Hey_Plex/help1.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('admin:index')
            else:
                login(request, user)
                # messages.success(request, 'You have successfully logged in dear...')
                # Redirect to a success page.
                return redirect('ShowCase')
        else:
            # Return an 'invalid login' error message.
            messages.info(request, 'Wrong Username/Password.')
            return redirect('login')
    else:
        return render(request,'Hey_Plex/login.html', {})

def details(request):
    return render(request,'Hey_Plex/details.html', {})

def endsession(request):
    return render(request,'Hey_Plex/end.html', {})

def bookingtable(request):
    det = booking.objects.filter(user= request.user)
    ordering = ['-created_at']
    context = {
        'det': det
    }

    return render(request, 'Hey_Plex/bookingtable.html', context)


class ShowCase(ListView):
    template_name = 'Hey_Plex/ShowCase.html'
    context_object_name = 'carmake'
    ordering = ['-created_at']
    paginate_by = 6

    def get_queryset(self):
      return make1.objects.all()


class ShowDetail(DetailView):

    model = model1
    template_name = 'Hey_Plex/details2.html'




def search(request):

        q = request.GET.get('q')

        if q:
            carmake = PostDocument.search().query("match", car_make=q)
        else:
            carmake = ''

        return render(request, 'Hey_Plex/ShowCase.html', {'carmake': carmake})


def logout_user(request):
    logout(request)
    # messages.success(request, 'You have been successfully logged out')
    return redirect('login')
    # Redirect to a success page.
def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Successfully Registered'))
                # Redirect to a success page.
            return redirect('ShowCase')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()

    context = { 'form': form , 'profile_form': profile_form}
    return render(request, 'Hey_Plex/signup.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        p_form = EditProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()

            messages.success(request, ('Profile changed successfully'))
                
            return redirect('ShowCase')
    else:
        form = EditProfileForm(instance=request.user)
        p_form = EditProfile(instance=request.user.profile)


    context = { 'form' :form,
                'p_form' :  p_form
                }

    return render(request, 'Hey_Plex/edit_profile.html', context )

def change_password (request):

    if request.method == 'POST':
        form = PasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)

            messages.success(request, ('Password changed successfully'))
                # Redirect to a success page.
            return redirect('change_password')
    else:
        form = PasswordForm(user=request.user)

    context = { 'form' :form }

    return render(request, 'Hey_Plex/change_password.html', context )

def add_feedback_submission(request):
    # if request.method == 'POST':
        username =request.POST['username']
        email= request.POST['email']
        category = request.POST['category']
        message = request.POST['message']


        add_materials1 = feedback(username=username,email=email,category=category, message= message)


        add_materials1.save()
        return render(request, 'Hey_Plex/feedback1.html', {})


def bookings(request):
    if request.method == 'POST':
        fullname=request.POST['fullname']
        car_price = request.POST['car_price']
        car_make1 = request.POST['car_make1']
        car_model1 = request.POST['car_model1']
        phonenumber = request.POST['phonenumber']
        pickupdate = request.POST['pickupdate']
        days = request.POST['days']
        user = request.POST['user']
        amount = int((int(car_price)*int(days)))
        code = 254
        number_code = str(code)+str(phonenumber)
        # lipa_na_mpesa(phonenumber,amount)


        add1 = booking(fullname=fullname,car_price=car_price,phonenumber=number_code,car_make1=car_make1,car_model1=car_model1,
                    pickupdate=pickupdate,days=days,amount=amount, user=user)
        add1.save()
        # messages.success(request, ('Booking successful.We will contact you soon'))
        # print('id')
        return redirect('bookingtable')
    return render(request, 'Hey_Plex/details1.html', {})

def pay(request,booking_id,phone,amount):
    the_booking =booking.objects.get(pk=booking_id) 
    context = {'booking':the_booking}
    if request.method == 'POST':
        lipa_na_mpesa(phone,amount)
        return redirect('verify', book_id = booking_id)
    return render(request,'Hey_Plex/pay.html', context)

def verify(request, book_id):
    if request.method == 'POST':
        trans_id= request.POST.get('trans_id')
        count = LNMonline.objects.values_list('Result_Code').filter(Mpesa_Receipt_Number = trans_id).filter(Result_Code=0).count()
        if count == 1:
            # transaction = LNMonline.objects.get(Mpesa_Receipt_Number=trans_id,Result_Code=0)
            # required_code = 0
            the_booking =booking.objects.get(pk=book_id)
            # if str(transaction) == str(required_code):
            the_booking.paid = True
            the_booking.save()
            return redirect('end')
            
        else:
            messages.success(request, ('The Transaction ID entered does not match with any'))
            return redirect('verify', book_id = book_id)
    return render(request, 'Hey_Plex/verify.html', {})