from django.shortcuts import render

# Create your views here.

def graph_1_AJAX(request):

    import random as rd
    from logic.subjects_list import verify_code
    subject_code = int(request.GET['subject'])

    if verify_code(subject_code):
        return render(request, "test_ajax/graph_1_AJAX.html",
        {'data_graph_1':
           [[ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, rd.randrange(3,100), 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2]],
            'x_labels_graph_1': "0-1,1-2,2-3,3-4,4-5,5-6,6-7,7-8,8-9,9-10",
            'bar_labels_graph_1': "x_labels, 5000-10000, 10000-12500, 12500-15000, 15000-20000, 20000-30000,+ 30000",
            'title_graph_1': 'TMM (Theory in Machines and Mechanism)',
            'subject': subject_code})

    else:
        return render(request, "test_ajax/ºerror.html")




def graph_1 (request):

    from logic.subjects_list import get_input_var_defaut
    return render(request, "test_ajax/graph_1.html", {'subjects_jinja': get_input_var_defaut(),'current_subject': 'Default'})