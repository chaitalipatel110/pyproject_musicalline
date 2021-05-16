from django.contrib import admin
from django.contrib.admin.decorators import register
from myapp.models import Person, Address, MusicalStoreHome, MusicalStoreReg, MusicalStoreInstrument, MusicalStoreContactus, MusicalStoreAboutus


""""@register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'postal_code')"""

@register(MusicalStoreHome)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('logotext1', 'logotext2', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'title1', 'title2', 'title3', 'title4', 'subtitle1', 'subtitle2', 'subtitle3', 'subtitle4', 'subdesc1', 'subdesc2', 'subdesc3', 'subdesc4', 'img1', 'img2', 'img3', 'img4', 'text7', 'copyrighttext', 'btntext1', 'btntext2', 'btntext3', 'btntext4', 'btntext5', 'btntext6', 'btntext7', 'btntext8', 'status', 'userid')

@register(MusicalStoreReg)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'mobile', 'img', 'status', 'username', 'password', 'created', 'updated')

@register(MusicalStoreInstrument)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'img', 'desc', 'price', 'created', 'updated')

@register(MusicalStoreAboutus)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc1', 'desc2', 'desc3', 'desc4', 'img')

@register(MusicalStoreContactus)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'address1', 'address2', 'address3', 'img', 'number', 'email', 'created', 'updated')
