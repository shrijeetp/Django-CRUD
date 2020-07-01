from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from myapp.models import CustomerRegModel
from myapp.serializers import CustomerSerializers


def coustomerView(request):
    context = {}
    query_results = CustomerRegModel.objects.all()
    context['query_results'] = query_results

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST['lastname']
        Gender = request.POST.get('Gender')
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        repass = request.POST['repass']
        CustomerRegModel.objects.create(
            firstname=firstname,
            lastname=lastname,
            Gender=Gender,
            phone=phone,
            address=address,
            email=email,
            password=password,
            repass=repass
        )
        return render(request, 'customerlog.html', context)
    else:
        return render(request, "customerlog.html",context)



class Customer_view_(ModelViewSet):
    queryset = CustomerRegModel.objects.all()
    serializer_class = CustomerSerializers
