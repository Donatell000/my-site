from django.http import HttpResponse


def message_welcome(request):
    return HttpResponse("Делитесь своими мыслями!")

