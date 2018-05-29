from django.shortcuts import render

def index (request):
    return render( request, "home/home.html")

def conclusion (request):
    return render( request, "home/conclusion.html")

def postal_code_AJAX (request):

    from logic.codigo import codigo_p

    try: 
        postal_code = int(request.GET['postal_code'])
        postal_code = '{:>05d}'.format(postal_code)

        # Get income for a given postal code:
        income = codigo_p(int(postal_code))

        if not income:
            return render( request, "home/includes/postal_code_not_find.html",{'postal_code': postal_code})
        else:
            return render( request, "home/includes/postal_code.html",{'postal_code': postal_code, 'income': income})

    except:
        return render( request, "home/includes/postal_code_not_find.html",{
        'postal_code': postal_code
    })
