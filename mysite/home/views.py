from django.shortcuts import render

def index (request):
    return render( request, "home/home.html")

def conclusion (request):
    return render( request, "home/conclusion.html")

def postal_code_AJAX (request):
    try: 
        postal_code = int(request.GET['postal_code'])
        postal_code = '{:>05d}'.format(postal_code)

        return render( request, "home/includes/postal_code.html",{
        'postal_code': postal_code,
        'income': 25000
    })

    except:
        return render( request, "home/includes/postal_code_not_find.html",{
        'postal_code': postal_code
    })
