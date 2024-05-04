from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        parcel_id = request.POST.get("parcel_id")
        mobile_number = request.POST.get("mobile_number")
        api_url = f'http://127.0.0.1:8000/status/{parcel_id}/'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return render(request, "status.html",{'data':data})
        else:
            return render(request,"index.html", {'message':'Failed to fetch the parcel status. Check Again!'})
        
    return render(request,'index.html')