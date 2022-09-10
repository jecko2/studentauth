from django.shortcuts import render
from django.views import View
from coreorder.forms.forms import InitialOrderForm
from coreorder.models import InitialCalOrder
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.


class HomeView(View):
    def get(self, request):
        form = InitialOrderForm()
        return render(request, "core/home.html", {"form": form})
    
    def post(self, request):
        form = InitialOrderForm(request.POST)
    
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            return HttpResponse(get_final_price(request))
        return HttpResponse(form.errors.as_json())
    
    
def add_number_of_pages(request):
    page = InitialCalOrder.objects.filter(student=request.user).latest()
    if page is not None:
        page = InitialCalOrder.objects.all()[0]
        page.pages += 1
        page.save()
        return redirect("order:home")

def subtract_number_of_pages(request):
    page = InitialCalOrder.objects.all()
    if page.exists():
        page = InitialCalOrder.objects.all()[0]
        page.pages -= 1
        if page.pages == 0:
            return redirect("order:home")
        page.save()
        return redirect("order:home")
    
    

def get_final_price(request):
    
    instance = InitialCalOrder.objects.filter(student=request.user).latest()
    if instance is not None:
        return instance.price
    return None
