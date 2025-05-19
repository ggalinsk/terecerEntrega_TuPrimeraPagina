from django.shortcuts import render , redirect
from .forms import SurfClassForm, MembershipForm, ProductsForm
from .models import SurfClass, MembershipPlan, Products

# Create your views here.
def index(request):
    return render(request, 'EscuelaDeSurf/index.html')

def create_surf_class(request):
    if request.method == 'POST':
        form = SurfClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = SurfClassForm()
    return render(request, 'EscuelaDeSurf/form_surfclass.html', {'form': form})

def create_membership_plan(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = MembershipForm()
    return render(request, 'EscuelaDeSurf/form_membership.html', {'form': form})

def create_Products(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = ProductsForm()
    return render(request, 'EscuelaDeSurf/form_Products.html', {'form': form})

def list_surf_clases(request):
    clases = SurfClass.objects.all()
    return render(request, 'EscuelaDeSurf/list_surf_clases.html', {'clases': clases})

def list_membership_plans(request):
    planes = MembershipPlan.objects.all()
    return render(request, 'EscuelaDeSurf/list_membership_plans.html', {'planes': planes})

def list_products(request):
    productos = Products.objects.all()
    return render(request, 'EscuelaDeSurf/list_products.html', {'productos': productos})

def buscar_clase(request):
    query = request.GET.get('query')
    resultados = []

    if query:
        resultados = SurfClass.objects.filter(titulo__icontains=query)

    return render(request, 'EscuelaDeSurf/index.html', {'clases_buscadas': resultados})