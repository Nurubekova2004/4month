from django.shortcuts import render
import datetime
def about_us(request):
    return render(request, 'about_us.html')


def date_now(request):
    date = datetime.datetime.now()
    return render(request, 'date_now.html', {'date':date})