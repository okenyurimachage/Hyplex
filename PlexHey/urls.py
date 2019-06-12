from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CoupesListView,ShowCase,ShowDetail,CoupesDetailView,HatchListView,HatchDetailView,convertibleDetailView,convertibleListView,sedanDetailView,sedanListView,mpvDetailView,mpvListView,suvDetailView,suvListView,crossoverDetailView,crossoverListView


urlpatterns = [


    path('search/', views.search),
    path('Coupes/<int:pk>/',CoupesDetailView.as_view(), name='details1'),
    path('hatchback/<int:pk>/',HatchDetailView.as_view(), name='details1'),
    path('convertible/<int:pk>/', convertibleDetailView.as_view(), name='convertible'),
    path('sedan/<int:pk>/', sedanDetailView.as_view(), name='sedan'),
    path('mpv/<int:pk>/', mpvDetailView.as_view(), name='mpv'),
    path('suv/<int:pk>/', suvDetailView.as_view(), name='suv'),
    path('Crossover/<int:pk>/', crossoverDetailView.as_view(), name='crossover'),
    path('home/', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('', views.details, name='details'),
    path('logout/', views.logout_user, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('ShowCase/',ShowCase.as_view(), name='ShowCase'),
    path('ShowCase/<int:pk>/',ShowDetail.as_view(context_object_name='model1'),name='details2'),
    path('ShowCase/Coupe/', CoupesListView.as_view(), name='Coupes'),
    path('ShowCase/hatchback/', HatchListView.as_view(), name='hatchback'),
    path('ShowCase/convertibles/', convertibleListView.as_view(), name='convertible'),
    path('ShowCase/sedan/', sedanListView.as_view(), name='sedan'),
    path('ShowCase/MPV/', mpvListView.as_view(), name='mpv'),
    path('ShowCase/SUV/', suvListView.as_view(), name='suv'),
    path('ShowCase/Crossover/', crossoverListView.as_view(), name='crossover'),
    path('bookingtable/', views.bookingtable, name='bookingtable'),
    path('add_form_submission/', views.add_feedback_submission, name='add_feedback_submission'),
    path('bookingdetails/', views.bookings, name='bookings'),
    path('Hey_Plex/password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('Hey_Plex/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),  name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('pay/<pk>', views.pay, name="pay"),

]


