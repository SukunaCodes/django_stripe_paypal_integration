from django.shortcuts import render

from payments.models import Donation


# Donation Page
def donation(request):
    donation = Donation.objects.get(id=2)
    context = {'donation': donation}
    return render(request, 'donation/my_donation.html', context=context)


# Successful payment
def successful_payment(request):
    return render(request, 'donation/payment_success.html')


# Failed payment
def failed_payment(request):
    return render(request, 'donation/payment_failed.html')
