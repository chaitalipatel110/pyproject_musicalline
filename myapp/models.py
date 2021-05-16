from django.db import models
from django.db.models.deletion import SET_NULL


class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=6)


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    profile_pic = models.ImageField(blank=True)
    address = models.ForeignKey(Address, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MusicalStoreHome(models.Model):
    logotext1 = models.CharField(max_length=255,null=True)
    logotext2 = models.CharField(max_length=255, null=True)
    text1 = models.CharField(max_length=255,null=True)
    text2 = models.CharField(max_length=255,null=True)
    text3 = models.CharField(max_length=255,null=True)
    text4 = models.CharField(max_length=255,null=True)
    text5 = models.CharField(max_length=255,null=True)
    text6 = models.CharField(max_length=255, null=True)
    title1 = models.CharField(max_length=255, null=True)
    title2 = models.CharField(max_length=255, null=True)
    title3 = models.CharField(max_length=255, null=True)
    title4 = models.CharField(max_length=255, null=True)
    subtitle1 = models.CharField(max_length=255,null=True)
    subtitle2 = models.CharField(max_length=255,null=True)
    subtitle3 = models.CharField(max_length=255,null=True)
    subtitle4 = models.CharField(max_length=255,null=True)
    subdesc1 = models.CharField(max_length=255,null=True)
    subdesc2 = models.CharField(max_length=255,null=True)
    subdesc3 = models.CharField(max_length=255,null=True)
    subdesc4 = models.CharField(max_length=255,null=True)
    img1 = models.ImageField(blank=True)
    img2 = models.ImageField(blank=True)
    img3 = models.ImageField(blank=True)
    img4 = models.ImageField(blank=True)
    text7 = models.CharField(max_length=5255, null=True)
    copyrighttext = models.CharField(max_length=255,null=True)
    btntext1 = models.CharField(max_length=255,null=True)
    btntext2 = models.CharField(max_length=255,null=True)
    btntext3 = models.CharField(max_length=255,null=True)
    btntext4 = models.CharField(max_length=255,null=True)
    btntext5 = models.CharField(max_length=255,null=True)
    btntext6 = models.CharField(max_length=255,null=True)
    btntext7 = models.CharField(max_length=255, null=True)
    btntext8 = models.CharField(max_length=255, null=True)
    status = models.BooleanField(null=True)
    userid = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.logotext1} {self.logotext2} {self.text1} {self.text2} {self.text3} {self.text4} {self.text5} {self.text6} {self.title1} {self.title2} {self.title3} {self.title4} {self.subdesc1} {self.subdesc2} {self.subdesc3} {self.subdesc4} {self.img1} {self.img2} {self.img3} {self.img4} {self.text7} {self.copyrighttext} {self.btntext1} {self.btntext2} {self.btntext3} {self.btntext4} {self.btntext5} {self.btntext6} {self.btntext7} {self.btntext8} {self.status} {self.userid}"

class MusicalStoreReg(models.Model):
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=255, null=True)
    img = models.ImageField(upload_to='media', blank=True)
    status = models.BooleanField(null=True)
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.email} {self.mobile} {self.img} {self.username} {self.password} {self.created} {self.updated}"

class MusicalStoreInstrument(models.Model):
    title = models.CharField(max_length=255, null=True)
    subtitle = models.CharField(max_length=255, null=True)
    img = models.ImageField(blank=True)
    desc = models.TextField(null=True)
    price = models.IntegerField(null=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.title} {self.subtitle} {self.img} {self.desc} {self.price} {self.created} {self.updated}"

class MusicalStoreAboutus(models.Model):
    title = models.CharField(max_length=255, null=True)
    desc1 = models.TextField(null=True)
    desc2 = models.TextField(null=True)
    desc3 = models.TextField(null=True)
    desc4 = models.TextField(null=True)
    img = models.ImageField(blank=True)


    def __str__(self):
        return f"{self.title} {self.desc1} {self.desc1} {self.desc2} {self.desc3} {self.desc4} {self.img}"

class MusicalStoreContactus(models.Model):
    name = models.CharField(max_length=255, null=True)
    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True)
    address3 = models.CharField(max_length=255, null=True)
    img = models.ImageField(blank=True)
    number = models.IntegerField(null=True)
    email = models.CharField(max_length=255,null=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.name} {self.address1} {self.address2} {self.address3} {self.img} {self.number} {self.email} {self.created} {self.updated}"
