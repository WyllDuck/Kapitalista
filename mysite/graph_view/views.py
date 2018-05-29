from django.shortcuts import render
import numpy as np

"""
INPUT:
postal_code <STRING> == The type of postal code we are going to use for the data treatment
Note: postal_ code = 'HOME' or 'SCHOOL'

    FORMAT EXAMPLE: postal_code = 'HOME'

subject_code <INT : 6 digits> == The subject that the end-user wants to see

    FORMAT EXAMPLE: subject_code = 240011 (Equivalent to: 'Àlgebra Lineal' )

OUTPUT:
'data' <LIST> == List of list: [Income, Average Grade]
'title_graph' <STRING> == The title
'linear_regression' <STRING> == The linear regression of the list of points 'data'

HTML RENDER VARIABLES : title_graph_5
PANDAS VARIABLES: data_graph_5; linear_regression

FORMAT EXAMPLE:

        {'data_graph_5': [[0, 67],[1, 88],[2, 77],[3, 93],[4, 85],[5, 91],[6, 71],[7, 78],[8, 93],[9, 80],[10, 82],[0, 75],[5, 80],[3, 90],[1, 72],[5, 75],[6, 68],[7, 98],[3, 82],[9, 94],[2, 79],[2, 95],[2, 86],[3, 67],[4, 60],[2, 80],[6, 92],[2, 81],[8, 79],[9, 83],[3, 75],[1, 80],[3, 71],[3, 89],[4, 92],[5, 85],[6, 92],[7, 78],[6, 95],[3, 81],[0, 64],[4, 85],[2, 83],[3, 96],[4, 77],[5, 89],[4, 89],[7, 84],[4, 92],[9, 98]],
            'title_graph_5': get_name(int(subject_code)),
            'linear_regression': 'x^2 + x + 1'})
"""

def graph_5_AJAX(request):

    from logic.subjects_list import verify_code, get_name
    from logic.codigo import reg_lineal
    
    try:
        subject_code = int(request.GET['subject'])
    except:
        subject_code = 0
    
    postal_code = str(request.GET['postal_code'])
    
    if verify_code(subject_code) and postal_code in ['HOME', 'SCHOOL']:
        v = reg_lineal(subject_code, 'SCHOOL' == postal_code)
        nt = v[2]
        rent = v[3]
        s = str(round(v[0], 7)) + ' X + ' + str(round(v[1], 3))
        Mat = list()
        for i in range(len(nt)):
            if not str(rent[i]) == 'nan' and not str(nt[i]) == 'nan':
                Mat.append([round(float(rent[i]), 1), round(float(nt[i]), 1)])
            if i >= 1500: 
                break

        return render(request, "graph_view/includes/scatter_chart.html",
            {'data_graph_5': Mat[:1500],
            'title_graph_5': get_name(int(subject_code)),
            'linear_regression': s})
    else:
        return render(request, "graph_view/none.html")

"""
INPUT:
postal_code <STRING> == The type of postal code we are going to use for the data treatment
    Note: postal_ code = 'HOME' or 'SCHOOL'

    FORMAT EXAMPLE: postal_code = 'HOME'

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

HTML RENDER VARIABLES : subject_code; title_graph_1
PANDAS VARIABLES: data_graph_1; x_labels_graph_1; bar_labels_graph_1

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
            'title_graph_1': 'TMM (Theory in Machines and Mechanism)'
            'subject': subject_code,}
"""

def graph_1_AJAX(request):
    
    from logic.codigo import graf1

    from logic.subjects_list import verify_code, get_name
    
    try:
        subject_code = int(request.GET['subject'])
    except:
        subject_code = 0
    
    postal_code = str(request.GET['postal_code'])
    
    if verify_code(subject_code) and postal_code in ['HOME', 'SCHOOL']:
        return render(request, "graph_view/includes/stacked_bar_chart.html",
        {'data_graph_1':
           graf1(subject_code,'SCHOOL'== postal_code),
            'x_labels_graph_1': "0-1,1-2,2-3,3-4,4-5,5-6,6-7,7-8,8-9,9-10",
            'bar_labels_graph_1': "x_labels, 5000-13500, 13500-18000, 18000-20000, 20000-23000, 23000-30000,+ 30000",
            'title_graph_1': get_name(int(subject_code)),
            'subject': subject_code})
    else:
        return render(request, "graph_view/none.html")


def graph_1 (request):

    from logic.subjects_list import get_input_var_defaut
    return render(request, "graph_view/graph_1.html", {'subjects_jinja': get_input_var_defaut()})



"""
INPUT:
postal_code <STRING> == The type of postal code we are going to use for the data treatment
    Note: postal_ code = 'HOME' or 'SCHOOL'

subject_code <INT : 6 digits> == The subject that the end-user wants to see (Navbar returns 'None')

    FORMAT EXAMPLE: subject_code = 240011 (Equivalent to: 'Àlgebra Lineal' )

top_bottom <STRING>: If the user wants to check the top ('TOP') or the bottom ('BOTTOM')
percent <FLOAT>: The top or bottom percent the end-user wants to check

OUTPUT:
'data' <LIST> == How many people in each span of top or bottom percent for a given subject
'x_labels' <STRING> == The incomes we send to the end-user (Decision made by the backend server)

HTML RENDER VARIABLES: top_bottom; percent; subject
PANDAS VARIABLES: data_graph_6; x_labels_graph_6

FORMAT EXAMPLE:

      {'data_graph_6': [ 10, 12, 33, 32, 11, 2],
            'x_labels_graph_6': "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000",
            'top_bottom': top_bottom.capitalize(),
            'percent': percent * 100,
            'subject': get_name(int(subject_code))
        })
"""
def graph_6_AJAX (request):

    from logic.codigo import peores, mejores
    
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
    
    if(top_bottom == 'TOP'):
        Mat = mejores(subject_code, percent, 'SCHOOL' == postal_code)
    else:
        Mat = peores(subject_code, percent, 'SCHOOL' == postal_code)
    
    s = str()
    for i in range (6):
        if(i != 5):
            s = s + str(Mat[1][i]) + '-' + str(Mat[1][i+1]) + ','
        else:
            s = s + '+' + str(Mat[1][i])
    
    if percent != 0 and verify_code(subject_code) and postal_code in ['HOME', 'SCHOOL'] and top_bottom in ['TOP', 'BOTTOM']:
        return render(request, "graph_view/includes/renta_column.html",
        {'data_graph_6': Mat[0],
            'x_labels_graph_6': s,
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
subjects_list <STRING> == The subjects that the end-user wants to see (Navbar returns 'Default')
postal_code <STRING> == The type of postal code we are going to use for the data treatment
    Note: postal_ code = 'HOME' or 'SCHOOL'

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
'x_labels' <STRING> == The desire subjects that the end-user wants to check
'column_labels' <STRING> == The desire incomes that the end-user wants to check

HTML RENDER VARIABLES : incomes; incomes_input; tabulated_incomes; rest; subjects_jinja; current_subjects; subjects_js
PANDAS VARIABLES: data_graph_4; x_labels_graph_4; column_labels_graph_4

FORMAT EXAMPLE:

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
"""

def graph_3 (request, incomes, subjects_list, postal_code):
    
    from logic.codigo import medias

    if incomes == 'Default':
        incomes = "10_15a15_18a18_21a21_25aREST"

    if subjects_list == 'Default':
        subjects_list = '240011a240012a240013'

    # Parse incomes variable and subjects_list variable:
    parser_html, parser_pandas, rest = urlParser(incomes)
    subjects_list_pandas, subjects_list = urlParserSubjects(subjects_list)

    # Subjects list:
    from logic.subjects_list import get_input_var_defaut, get_input_var_without_list_code, get_input_var_for_list_code, get_name
        
   # If variables are well written do this:
    if parser_pandas != None and subjects_list_pandas != None and postal_code in ['HOME', 'SCHOOL']: 

        try: 
            v_franjas = [0]*2*len(parser_pandas)
            s = str()
        
            for i in range(len(parser_pandas)):
                v_franjas[2*i] = parser_pandas[i][0]
                v_franjas[2*i+1] = parser_pandas[i][1]
        
            for i in range (len(v_franjas)//2):
                if(i != (len(v_franjas)/2)-1):
                    s = s + str(v_franjas[2*i]) + '-' + str(v_franjas[2*i+1]) + ','
                else:
                    s = s + str(v_franjas[2*i]) + '-' + str(v_franjas[2*i+1]) 
            
            if(rest):
                v_franjas.append(max(v_franjas))
                v_franjas.append(max(max(v_franjas)+1,60000))
                s = s + ',' + '+ ' + str(max(v_franjas[:-1]))

            x_labels = str()
            for i in range(len(subjects_list_pandas)):
                x_labels += str(get_name(subjects_list_pandas[i]))
                if i != len(subjects_list_pandas) - 1:
                    x_labels += ','
            x_labels = 'Incomes,' + x_labels

            data = medias(subjects_list_pandas, v_franjas, 'SCHOOL' == postal_code)
            data = [list(i) for i in list(zip(*data))]

            return render(request, "graph_view/graph_3.html",
                {'data_graph_4': data,
                    'x_labels_graph_4': x_labels,
                    'column_labels_graph_4': s,

                    # Things for processing HTML and JAVASCRIPT
                    'incomes': parser_html,
                    'incomes_input': parser_html[:-1] if (rest and parser_html != 'None') else parser_html,
                    'tabulated_incomes': parser_pandas,
                    'rest': 1 if rest else 0,
                    'subjects_jinja': get_input_var_without_list_code(subjects_list_pandas),
                    'current_subjects': get_input_var_for_list_code (subjects_list_pandas),
                    'subjects_js': subjects_list
                    })

        except:
            return render(request, "graph_view/graph_3_none.html",
            {   'incomes': parser_html,
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
Parse the url of "graph_3" in other to know which data to analyse with pandas
and display it to the end-user
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