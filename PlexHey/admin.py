from django.contrib import admin
from django.contrib.auth.models import User
from .models import feedback, Profile, car,model1, make1,booking
from django.contrib.auth.models import User, Group
import csv
from django.http import HttpResponse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from mpesa.models import LNMonline




# export as csv class


class ExportCsvMixin:

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
         row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected"


admin.site.unregister(Group)


# feedback admin


class feedbackAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['username', 'email', 'category' ,'message', 'read','created_at', 'updated_at']
    readonly_fields = ['username', 'email', 'category', 'message', 'created_at', 'updated_at']
    list_filter = ['created_at','read']
    list_editable = ['read']
    list_per_page = 10

    actions = ["export_as_csv"]

    def has_add_permission(self, request):
        return False


admin.site.register(feedback, feedbackAdmin)


# profile admin


# class profileAdmin(admin.ModelAdmin, ExportCsvMixin):
#
#
#
#
#    actions = ["export_as_csv"]
#
#    def has_add_permission(self, request):
#        return False
#
#
# admin.site.register(Profile, profileAdmin)
class ProfileInline(admin.StackedInline):
        model = Profile
        can_delete = False
        verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# Re-register UserAdmin


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# make admin


class make1Admin(admin.ModelAdmin, ExportCsvMixin):

   date_hierarchy = 'created_at'
   list_display = ['car_make','description','make_image','created_at','updated_at']
   list_filter  = ['created_at']
   search_fields = ['car_make']

   list_per_page = 10

   actions = ["export_as_csv"]



admin.site.register(make1, make1Admin)


# model admin



class model1Admin(admin.ModelAdmin, ExportCsvMixin):
   list_display = [ 'car_model' , 'car_make', 'car_price', 'car_image', 'car_capacity','model_year','fuel_type', 'created_at', 'updated_at' ]
   list_filter = ['created_at']
   search_fields = ['car_model']

   list_per_page = 10

   actions = ["export_as_csv"]



admin.site.register(model1,model1Admin)


# car admin


class carAdmin(admin.ModelAdmin, ExportCsvMixin):
   list_display = [ 'car_make' , 'car_model','number_plate','assigned', 'created_at', 'updated_at' ]
   list_editable = ['assigned']
   list_filter = ['created_at']
   search_fields = ['number_plate']

   list_per_page = 10

   actions = ["export_as_csv"]

admin.site.register(car,carAdmin)


#
class bookingAdmin(admin.ModelAdmin, ExportCsvMixin ):
    list_display = ['fullname', 'phonenumber', 'car_make1', 'car_model1', 'pickupdate','car_price', 'days','user','created_at']
    readonly_fields = ['fullname', 'phonenumber', 'car_make1', 'car_model1','car_price', 'pickupdate', 'days','user','created_at']
    list_filter = ['created_at']
    search_fields = ['fullname']
    list_per_page = 10

    actions = ["export_as_csv"]

    def has_add_permission(self, request):
        return False


class LNMonlineAdmin(admin.ModelAdmin):

    date_hierarchy = 'Transaction_Date'
    list_display = ['Phone_Number', 'Mpesa_Receipt_Number', 'Amount', 'Transaction_Date',]
    readonly_fields = ['Merchant_Request_ID','Checkout_Request_ID','Result_Code','Result_Description',
                       'Phone_Number', 'Mpesa_Receipt_Number', 'Amount', 'Transaction_Date', ]
    list_filter = ['Transaction_Date']

    def has_add_permission(self, request):
        return False

admin.site.register(booking,bookingAdmin)
admin.site.register(LNMonline,LNMonlineAdmin)
