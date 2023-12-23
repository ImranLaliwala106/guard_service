from django.contrib import admin
from cms.models import Service, Guard, Contact, Registration, About
# from cms.models import contact

class ServiceHeading(admin.ModelAdmin):
    list_display = ('admin_photo', 'serviceTitle', 'serviceDesc')

class guardHeading(admin.ModelAdmin):
    list_display = ('guard_photo', 'guardTitle', 'guardDesc')
    
class contactHeading(admin.ModelAdmin):
    list_display = ('cname', 'cemail', 'cphone')

class registrationHeading(admin.ModelAdmin):
    list_display = ('rname','runame', 'remail', 'rpass' )

class aboutHeading(admin.ModelAdmin):
    list_display = ('about_photo','aTitle', 'aDesc')

admin.site.register(Guard, guardHeading)
admin.site.register(Contact, contactHeading)
admin.site.register(Service, ServiceHeading)
admin.site.register(About, aboutHeading)
admin.site.register(Registration, registrationHeading)


# class contacthandle(admin.ModelAdmin):
#     list1 = ('fname', 'email', 'phone', 'msg')
# admin.site.register(contact, contacthandle)

# Register your models here.
