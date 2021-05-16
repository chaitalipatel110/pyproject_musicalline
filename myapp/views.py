from django.shortcuts import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from myapp.models import Person, MusicalStoreHome, MusicalStoreReg, MusicalStoreInstrument, MusicalStoreContactus, MusicalStoreAboutus
from myapp.forms import FirstNameForm, MusicalstoreRegform
from django.http import response
from django.template.response import SimpleTemplateResponse
from django.views.generic.edit import FormView
from django.shortcuts import render


def home(request, **kwargs):
    return HttpResponse("Hello")

def get_current_time(request):
    current_time = datetime.now()
    timezone = request.GET.get('timezone')

    the_data = {
        'current_time': current_time,
        'timezone': timezone
    }

    response = SimpleTemplateResponse('current_time.html', the_data)
    return response

class PersonInfoMixin:

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        person = Person.objects.get(pk=pk)
        context  = {
            'person': person
        }
        return context


class PersonInfo(TemplateView):

    template_name = 'person.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        person = Person.objects.get(pk=pk)
        context['person'] = person
        return context

    def post(self, request, **kwargs):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        context = self.get_context_data(**kwargs)
        person = context['person']
        person.first_name = first_name
        person.last_name = last_name
        person.email = email
        person.save()

        return redirect('people-list')


class PersonListView(ListView):
    template_name = 'person_list.html'
    model = Person

class AllEmails(View):

    def get(self, request):
        emails = Person.objects.all().values_list('email', flat=True)
        return response.JsonResponse(data=list(emails), safe=False)

class MusicalStoreHomeView(TemplateView):

    template_name = 'musical_store_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        context['Title'] = 'Home'
        return context


class MusicalStoreRegAddView(TemplateView):

    template_name = 'musical_store_reg.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        context['Reg'] = MusicalStoreReg.objects.all()
        return context

    def post(self, request, **kwargs):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        img = request.FILES['img']
        status = 0
        username = request.POST['username']
        password = request.POST['password']
        created = datetime.now()
        updated = datetime.now()

        post = MusicalStoreReg()

        post.firstname = firstname
        post.lastname = lastname
        post.email = email
        post.mobile = mobile
        post.img = img
        post.status = status
        post.username = username
        post.password = password
        post.created = created
        post.updated = updated

        post.save()

        return redirect('musical_store_home')

class MusicalStoreRegEditView(TemplateView):

    template_name = 'musical_store_reg.html'

    def get_context_data(self, **kwargs):
        if self.request.session['userid'] != '':
            userid = self.request.session['userid']
        else:
            userid = 6
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        context['Reg'] = MusicalStoreReg.objects.get(id=userid)
        return context

    def post(self, request, **kwargs):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        img = request.FILES['img']
        status = 1
        username = request.POST['username']
        password = request.POST['password']
        created = datetime.now()
        updated = datetime.now()

        context = self.get_context_data(**kwargs)
        post = context['Reg']

        post.firstname = firstname
        post.lastname = lastname
        post.email = email
        post.mobile = mobile
        post.img = img
        post.status = status
        post.username = username
        post.password = password
        post.created = created
        post.updated = updated

        post.save()

        return redirect('musical_store_home')

class MusicalStoreRegView(TemplateView):

    template_name = 'musical_store_reg.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        context['Reg'] = MusicalStoreReg.objects.all()
        context['Title'] = 'Registration Form'
        return context

class MusicalStoreRegShow(TemplateView):

    template_name = 'musical_store_reg_show.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        if self.request.session['userid'] != '':
            userid = self.request.session['userid']
        else:
            userid = 6
        context['Reg'] = MusicalStoreReg.objects.get(id=userid)
        context['Title'] = 'Profile'
        return context

class MusicalStoreInstrumentView(TemplateView):

    template_name = 'musical_store_instrument.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        context['Instrument'] = MusicalStoreInstrument.objects.all()
        context['Title'] = 'Instruments'
        return context


class MusicalStoreInstrumentDetail(TemplateView):

    template_name = 'musical_store_instrument_detail.html'

    def get_context_data(self, **kwargs):

        id = kwargs.get('id')
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        context['Instrumentdetail'] = MusicalStoreInstrument.objects.get(id=id)
        context['Title'] = 'Instruments Detail'
        return context

class MusicalStoreAboutusView(TemplateView):

    template_name = 'musical_store_aboutus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        context['Aboutus'] = MusicalStoreAboutus.objects.all()
        context['Title'] = 'About Us'
        return context

class MusicalStoreContactusView(TemplateView):

    template_name = 'musical_store_contactus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        context['Contactus'] = MusicalStoreContactus.objects.all()
        context['Title'] = 'Contact Us'
        return context

class MusicalStoreLoginView(TemplateView):

    template_name = 'musical_store_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        context['Title'] = 'Login'
        return context


class MusicalStoreLoginAddView(TemplateView):

    template_name = 'musical_store_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        return context

    def post(self, request, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        status = request.POST['status']

        post = MusicalStoreReg.objects.get(username=username, password=password)
        post.status = status
        post.save()

        request.session['userid'] = post.id

        return redirect('musical_store_home')

class MusicalStoreLogoutView(TemplateView):

    template_name = 'musical_store_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Home'] = MusicalStoreHome.objects.all()
        return context

    def post(self, request, **kwargs):
        status = 0
        if request.session['userid'] != '':
            userid = request.session['userid']
        else:
            userid = 6
        post = MusicalStoreReg.objects.get(id=userid)
        post.status = status
        post.save()

        if request.session['userid'] != '':
            del request.session['userid']

        return redirect('musical_store_home')

