from django.http import HttpResponse

def index(request):
    return HttpResponse("Salam,burada suallarıza cavab tapa bilərsiniz.")
