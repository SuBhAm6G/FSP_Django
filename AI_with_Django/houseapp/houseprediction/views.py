from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import joblib

model = joblib.load('D:\\CSBS_SubhamDhar_13031124055\\AI_with_Django\\house_model.pkl')

# Create your views here.
@login_required(login_url='/admin/login/')
def predict_fun(request):
    if request.method == 'POST':
        area = float(request.POST.get('area'))
        bedrooms = float(request.POST.get('bedrooms'))
        bathrooms = float(request.POST.get('bathrooms'))
        age = float(request.POST.get('age'))
        price = model.predict([[area, bedrooms, bathrooms, age]])
        predicted_price = f'{float(price[0]):.2f}'

        return render(request, 'prediction.html', {'pred': predicted_price})
    else:
        return render(request, 'prediction.html')
