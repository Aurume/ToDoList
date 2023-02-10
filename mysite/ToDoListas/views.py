from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Model, Count, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_protect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin

from .models import Uzduotis
from .forms import UzduotisCreateUpdateForm, UzduotisApzvalgaForm


# Create your views here.

@login_required
def index(request):
    #num_uzduotys = Uzduotis.objects.count()
    #num_aktyvios = Uzduotis.objects.filter(status__exact='p').count()  # p=reikia padaryti
    # veikia patikrinus vartotoja ir ar jis prisijunges.
    num_aktyvios = Uzduotis.objects.filter(vartotojas=request.user, vartotojas__is_active=True, status__exact='p').count()


    context = {
    #     "num_uzduotys": num_uzduotys,
         "num_aktyvios": num_aktyvios,

     }
    return render(request, 'index.html', context=context)


def uzduotys(request):
    paginator = Paginator(Uzduotis.objects.all(), 7)
    page_number = request.GET.get('page')
    paged_uzduotys = paginator.get_page(page_number)
    context = {
        'uzduotys': paged_uzduotys
    }
    return render(request, 'uzduotys.html', context=context)
#
def uzduotis(request, uzduotis_id):
    uzduotis = get_object_or_404(Uzduotis, pk=uzduotis_id)
    return render(request, 'uzduotis.html', context={'uzduotis': uzduotis})



@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


# paziureti sita varianta jeigu reikes
#
# class ProductList(View):
#
#     def get(self, request, *args, **kwargs):
#         products = Product.objects.all()
#         context  = {'products':products}
#         return render(request, 'base/product_list.html', context)
#
#     def post(self, request, *args, **kwargs):
#         pass


class UzduotysList(ListView):
    model = Uzduotis
    context_object_name = 'uzduotys'
    paginate_by = 5
    template_name = 'uzduotys.html'



    # def get(self, request, *args, **kwargs):
    #     uzduotis = Uzduotis.objects.all()
    #     context = {'uzduotis': uzduotis}
    #     return render(request, 'uzduotis.html', context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['uzduotys'] = context['uzduotys'].filter(vartotojas=self.request.user)
    #     return context

    # def get_queryset(self):
    #     # user = get_object_or_404(User, username=self.kwargs.get('pavadinimas'))
    #     return Uzduotis.objects.filter(vartotojas=self.request.user)

class UzduotisDetail(FormMixin, DetailView):

    model = Uzduotis
    context_object_name = 'uzduotis'
    template_name = 'uzduotis.html'
    form_class = UzduotisApzvalgaForm

    def get_success_url(self):
        return reverse('uzduotis', kwargs={'pk': self.get_object().id})

      # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class VartotojoUzduotisList(LoginRequiredMixin, ListView):
    model = Uzduotis
    template_name = 'vartotojo_uzduotyss.html'
    paginate_by = 5
    context_object_name = "uzduotys"

    def get_queryset(self):
        return Uzduotis.objects.filter(vartotojas=self.request.user).order_by('-sukurta')

class VartotojoUzduotysList(LoginRequiredMixin, ListView):
    model = Uzduotis
    context_object_name = 'uzduotis'
    template_name = 'vartotojo_uzduotis.html'
    paginate_by = 7

    def get_queryset(self):
        return Uzduotis.objects.filter(vartotojas=self.request.user).order_by('-sukurta')

class VartotojoUzduotysDetail(LoginRequiredMixin, DetailView):
    model = Uzduotis
    template_name = 'vartotojo_uzduotis.html'
    #context_object_name = 'viena-uzduotis'

class UzduotisVartotojoCreate(LoginRequiredMixin, CreateView):
    model = Uzduotis
    #fields = '__all__'  # visi laukeliai iskart
    #fields = ['pavadinimas', 'aprasymas', 'terminas', 'status']
    success_url = "/ToDoListas/vartotojouzduotys/"
    #success_url = reverse_lazy('uzduotys')
    template_name = 'vartotojo_uzduotis_form.html'
    form_class = UzduotisCreateUpdateForm

    def form_valid(self, form):
        form.instance.vartotojas = self.request.user
        form.save()
        return super().form_valid(form)

class UzduotisVartotojoUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Uzduotis
    #fields = ['pavadinimas', 'aprasymas' 'terminas', 'status']
    #success_url = "/servisas/vartotojouzsakymai/"
    #success_url = reverse_lazy('uzduotis')
    template_name = 'vartotojo_uzduotis_form.html'
    form_class = UzduotisCreateUpdateForm

    def get_success_url(self):
         return reverse("uzduotis", kwargs={"pk": self.object.id})

    def form_valid(self, form):
         form.instance.vartotojas = self.request.user
         return super().form_valid(form)

    def test_func(self):
        uzduotis = self.get_object()
        return self.request.user == uzduotis.vartotojas


class UzduotisVartotojoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Uzduotis
    success_url = "/ToDoListas/vartotojouzduotys/"
    template_name = 'vartotojo_uzduotis_trinti.html'
    context_object_name = 'uzduotis'
    #success_url = reverse_lazy('uzduotys')

    # def get_success_url(self):
    #     return reverse("uzduotis", kwargs={"pk": self.kwargs['uzduotis_pk']})

    def test_func(self):
        uzduotis = self.get_object()
        return self.request.user == uzduotis.vartotojas




