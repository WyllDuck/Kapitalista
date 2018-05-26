from django.shortcuts import render

"""
INPUT:
subject_code <INT : 6 digits> == The subject that the end-user wants to see (Navbar returns 'None')

FORMAT EXAMPLE: subject_code = 240011 (Equivalent to: 'Àlgebra Lineal' )

OUTPUT:
'data' <LIST> == Percentage of people with the same ""grades"" AND ""income""
    - The lists inside the main list are ordered in the same order as "bar_labels"
    - The values inside the secondary lists are ordered in the same order as "x_labels"
'x_labels' <STRING> == The desire interval of grades in the subject
'bar_labels' <STRING> == The desire incomes that the end-user wants to check

            ""Note: The first label is allways the x_labels""

'title' <STRING> == Name of the university subject that the end-user wants to check

HTML RENDER VARIABLES : subjects_jinja

FORMAT EXAMPLE:

        {'data_graph_1':
           [[ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2]],
            'x_labels_graph_1': "0-1,1-2,2-3,3-4,4-5,5-6,6-7,7-8,8-9,9-10",
            'bar_labels_graph_1': "x_labels, 5000-10000, 10000-12500, 12500-15000, 15000-20000, 20000-30000,+ 30000",
            'title_graph_1': 'TMM (Theory in Machines and Mechanism)',
            'subjects_jinja': get_input_var(int(subject_code)),
            'current_subject': get_current_subject(int(subject_code))}
"""

def graph_5_AJAX(request):

    from logic.subjects_list import verify_code, get_name
    
    try:
        subject_code = int(request.GET['subject'])
    except:
        subject_code = 0
    
    postal_code = str(request.GET['postal_code'])    

    if verify_code(subject_code) and postal_code in ['HOME', 'SCHOOL']:
        return render(request, "graph_view/includes/scatter_chart.html",
            {'data_graph_5': [[0, 67],[1, 88],[2, 77],[3, 93],[4, 85],[5, 91],[6, 71],[7, 78],[8, 93],[9, 80],[10, 82],[0, 75],[5, 80],[3, 90],[1, 72],[5, 75],[6, 68],[7, 98],[3, 82],[9, 94],[2, 79],[2, 95],[2, 86],[3, 67],[4, 60],[2, 80],[6, 92],[2, 81],[8, 79],[9, 83],[3, 75],[1, 80],[3, 71],[3, 89],[4, 92],[5, 85],[6, 92],[7, 78],[6, 95],[3, 81],[0, 64],[4, 85],[2, 83],[3, 96],[4, 77],[5, 89],[4, 89],[7, 84],[4, 92],[9, 98]],
            'title_graph_5': get_name(int(subject_code)),
            'linear_regression': 'x^2 + x + 1'})
    else:
        return render(request, "graph_view/none.html")


def graph_1_AJAX(request):

    from logic.subjects_list import verify_code, get_name
    
    try:
        subject_code = int(request.GET['subject'])
    except:
        subject_code = 0
    
    postal_code = str(request.GET['postal_code'])
    
    if verify_code(subject_code) and postal_code in ['HOME', 'SCHOOL']:
        return render(request, "graph_view/includes/stacked_bar_chart.html",
        {'data_graph_1':
           [[ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 13, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2],
            [ 10, 12, 33, 32, 11, 2]],
            'x_labels_graph_1': "0-1,1-2,2-3,3-4,4-5,5-6,6-7,7-8,8-9,9-10",
            'bar_labels_graph_1': "x_labels, 5000-10000, 10000-12500, 12500-15000, 15000-20000, 20000-30000,+ 30000",
            'title_graph_1': get_name(int(subject_code)),
            'subject': subject_code})
    else:
        return render(request, "graph_view/none.html")


def graph_1 (request):

    from logic.subjects_list import get_input_var_defaut
    return render(request, "graph_view/graph_1.html", {'subjects_jinja': get_input_var_defaut()})



"""
INPUT:
incomes <STRING> == The incomes that the end-user wants to see (Navbar returns 'Default')

FORMAT EXAMPLE:
    exemple_1:
        incomes = 5_10a20_30a10_12k5a12k5_15a15_20aREST
        (Equivalent to: "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000")

    exemple_2: (REST no included)
        incomes = 5_10a10_12k5a12k5_15a15_20a20_30
        (Equivalent to: "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000")

Note:   If parser_html or parser_pandas have ""None"" values an error occured during the parsing mecanism or the
        url hasn't been well written

OUTPUT:
'data' <LIST> == Average timestamp to have the engineering degree separated by income
    - The values in the list are in the same order as the different incomes in 'bar_labels'
'bar_labels' <STRING> == The desire incomes that the end-user wants to check

HTML RENDER VARIABLES : incomes, incomes_input, tabulated_incomes, rest

FORMAT EXAMPLE:

       {'data_graph_2': [6.5, 5.7, 5.4, 5.1, 4.7, 4.3],
            'bar_labels_graph_2': "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000",
            'incomes': parser_html,
            'incomes_input': parser_html[:-1] if (rest and parser_html != 'None') else parser_html,
            'tabulated_incomes': parser_pandas,
            'rest': 1 if rest else 0 }
"""
def graph_6_AJAX (request):

    from logic.subjects_list import verify_code, get_name  

    try:
        subject_code = int(request.GET['subject'])
    except:
        subject_code = 0
    
    postal_code = str(request.GET['postal_code'])
    top_bottom = str(request.GET['top_bottom'])

    try:
        percent = float(request.GET['percent'])
    except:
        percent = 0

    if percent != 0 and verify_code(subject_code) and postal_code in ['HOME', 'SCHOOL'] and top_bottom in ['TOP', 'BOTTOM']:
        return render(request, "graph_view/includes/renta_column.html",
        {'data_graph_6': [ 10, 12, 33, 32, 11, 2],
            'x_labels_graph_6': "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000",
            'top_bottom': top_bottom.capitalize(),
            'percent': percent * 100,
            'subject': get_name(int(subject_code))
        })

    else:
        return render(request, "graph_view/none.html")


def graph_2 (request):

    from logic.subjects_list import get_input_var_defaut        
    return render(request, "graph_view/graph_2.html", {'subjects_jinja': get_input_var_defaut()})



"""
INPUT:
incomes <STRING> == The incomes that the end-user wants to see (Navbar returns 'Default')

FORMAT EXAMPLE:
    exemple_1:
        incomes = 5_10a10_12k5a12k5_15a15_20a20_30aREST
        (Equivalent to: "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000")

    exemple_2: (REST no included)
        incomes = 5_10a10_12k5a12k5_15a15_20a20_30
        (Equivalent to: "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000")

Note:   If parser_html or parser_pandas have ""None"" values an error occured during the parsing mecanism or the
        url hasn't been well written

OUTPUT:
'data' <LIST> == Grades of Students with same income over the subjects of all the quarters
'x_labels' <STRING> == The desire quarters that the end-user wants to check
'line_labels' <STRING> ==  The desire incomes that the end-user wants to check

HTML RENDER VARIABLES : incomes, incomes_input, tabulated_incomes, rest

FORMAT EXAMPLE:

        {'data_graph_3':
           [[5, 5.5, 6.7, 6.1, 5.5, 4.5],
            [5.6, 6.0, 7.0, 6.6, 6.5, 4.6],
            [5.8, 6.1, 6.8, 6.3, 7.1, 5.0],
            [5.5, 4.8, 6.5, 6.4, 7.2, 4.5],
            [5.7, 5.9, 6.4, 6.3, 7.6, 6.0],
            [6.0, 6.5, 6.0, 6.0, 6.5, 4.9],
            [6.1, 6.0, 6.6, 6.0, 6.3, 5.1],
            [5.6, 6.3, 6.7, 5.7, 6.1, 5.4]],
            'x_labels_graph_3': 'Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8',
            'line_labels_graph_3': '5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000',
            'incomes': parser_html,
            'incomes_input': parser_html[:-1] if (rest and parser_html != 'None') else parser_html,
            'tabulated_incomes': parser_pandas,
            'rest': 1 if rest else 0 }
"""

def graph_3 (request, incomes, subjects_list, postal_code):

    if incomes == 'Default':
        incomes = "5_10a10_15a15_18a18_21a21_25aREST"

    if subjects_list == 'Default':
        subjects_list = '240011a240012a240013'

    # Parse incomes variable and subjects_list variable:
    parser_html, parser_pandas, rest = urlParser(incomes)
    subjects_list_pandas, subjects_list = urlParserSubjects(subjects_list)

    # Subjects list:
    from logic.subjects_list import get_input_var_defaut, get_input_var_without_list_code, get_input_var_for_list_code

    # If variables are well written do this:
    if parser_pandas != None and subjects_list_pandas != None and postal_code in ['HOME', 'SCHOOL']: 
        return render(request, "graph_view/graph_3.html",
            {'data_graph_4':
            [[4.8, 6.5, 6.4, 7.2, 4.5],
                [5.9, 6.4, 6.3, 7.6, 6.0],
                [6.5, 6.0, 6.0, 6.5, 4.9],
                [6.0, 6.6, 6.0, 6.3, 5.1],
                [6.3, 6.7, 5.7, 6.1, 5.4]],
                'x_labels_graph_4': "Incomes,Àlgebra Lineal,Càlcul I,Mecànica Fonamental,Química,Fonaments d'Informàtica",
                'column_labels_graph_4': '10000-12500,12500-15000,15000-20000,20000-30000,+ 30000',

                # Things for processing HTML and JAVASCRIPT
                'incomes': parser_html,
                'incomes_input': parser_html[:-1] if (rest and parser_html != 'None') else parser_html,
                'tabulated_incomes': parser_pandas,
                'rest': 1 if rest else 0,
                'subjects_jinja': get_input_var_without_list_code(subjects_list_pandas),
                'current_subjects': get_input_var_for_list_code (subjects_list_pandas),
                'subjects_js': subjects_list
                })

    # If variables are NOT well written do this:    
    else:
        return render(request, "graph_view/graph_3_none.html",
            {   'incomes': parser_html,
                'incomes_input': parser_html[:-1] if (rest and parser_html != 'None') else parser_html,
                'tabulated_incomes': parser_pandas,
                'rest': 1 if rest else 0,
                'subjects_jinja': get_input_var_defaut(),
                'current_subjects': ['Default select'],
                'subjects_js': subjects_list
                })
        

    
"""
Parse the url of "graph_2" and "graph_1" know to which data to analyse with pandas
and display to the end-user
"""
def urlParser (incomes):
    rest = False

    # Looking for 'REST':
    if incomes.endswith('aREST'):
        incomes = incomes.replace('aREST', '')
        rest = True

    parser_pandas = list()
    parser_html = list()

    try:
        incomes = incomes.split('a')
        for item in incomes:
            in_from, in_to = item.split('_')

            # For Pandas analys
            income = [float(in_from.replace('k','.')) * 1000, float(in_to.replace('k','.')) * 1000]

            if income in parser_pandas:
                return 'None', None, False

            parser_pandas.append(income)

            if income[0] > income[1]:
                return 'None', None, False
            if income[1] > 60000:
                return 'None', None, False                

        # For HTML view:
        parser_pandas.sort()
        for income in parser_pandas:
            string = '{}-{}'.format(int(income[0]), int(income[1]))
            parser_html.append(string)

        if rest:
            _rest = max(item[1] for item in parser_pandas)
            parser_html.append('+ {}'.format(int(_rest)))

    except:
        return 'None', None, False

    return parser_html, parser_pandas, rest



# Get list of subjects:
def urlParserSubjects (subjects_list):

    from logic.subjects_list import verify_code

    subjects_list_original = subjects_list

    try:
        subjects_list = subjects_list.split('a')
        list(int(subject) for subject in subjects_list)

        # Checking for bad codes: 
        for suject_code in subjects_list:
            if not verify_code(suject_code):
                return None, 'None'

        # Checking is the end-user has selected more than 5 subjects
        if len(subjects_list) > 5:
            return None, 'None'

        # Checking is the end-user has written to subjects that are the same
        for i in range(len(subjects_list)):
            subjects_list_copy = subjects_list.copy()
            subjects_list_copy.pop(i)
            if subjects_list[i] in subjects_list_copy:
                return None, 'None'          
        
        return subjects_list, subjects_list_original

    except:
        return None, 'None'