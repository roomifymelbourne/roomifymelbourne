# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import UserForm, EnquiryForm

def home(request):
    if request.method == 'POST':
        if 'contact' in request.POST:
            # Handle Enquiry form submission
            whatsapp_number = request.POST.get('contact')
            enquiry = EnquiryForm(whatsapp=whatsapp_number)
            enquiry.save()

            return JsonResponse({'success': True, 'message': 'Enquiry Submitted Successfully'})

        # Handle other form data submission (UserForm)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        rent = request.POST.get('rent')
        university = request.POST.get('university')
        city = request.POST.get('city')

        # Save the data to the UserForm model
        user = UserForm(
            name=name,
            mail=email,
            phno=phone,
            rent=rent,
            city=city,
            university=university
        )
        user.save()

        return JsonResponse({'success': True, 'message': 'Submitted Successfully'})

    return render(request, 'home.html')


def tandc(request):
    return render(request,"tandc.html")





