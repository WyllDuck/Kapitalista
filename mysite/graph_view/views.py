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

        {'data':
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
            'x_labels': "0-1,1-2,2-3,3-4,4-5,5-6,6-7,7-8,8-9,9-10",
            'bar_labels': "x_labels, 5000-10000, 10000-12500, 12500-15000, 15000-20000, 20000-30000,+ 30000",
            'title': 'TMM (Theory in Machines and Mechanism)',
            'subjects_jinja': subjects_jinja})
"""
def graph_1 (request, subject_code):

    from logic.subjects_list import get_input_var, get_current_subject, verify_code

    if verify_code(subject_code):
        return render(request, "graph_view/graph_1.html",
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
            'current_subject': get_current_subject(int(subject_code))})

    else:
        return render(request, "graph_view/error.html")






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

       {'data': [6.5, 5.7, 5.4, 5.1, 4.7, 4.3],
           'bar_labels': "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000",
           'incomes': parser_html,
           'incomes_input': parser_html[:-1] if (rest and parser_html != 'None') else parser_html,
           'tabulated_incomes': parser_pandas,
           'rest': 1 if rest else 0 })
"""
def graph_2 (request, incomes):
    # Parse incomes variable:
    parser_html, parser_pandas, rest = urlParser(incomes)

    return render(request, "graph_view/graph_2.html",
        {'data_graph_2': [6.5, 5.7, 5.4, 5.1, 4.7, 4.3],
            'bar_labels_graph_2': "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000",
            'incomes': parser_html,
            'incomes_input': parser_html[:-1] if (rest and parser_html != 'None') else parser_html,
            'tabulated_incomes': parser_pandas,
            'rest': 1 if rest else 0 })




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

         {'data':
            [[5, 5.5, 6.7, 6.1, 5.5, 4.5],
             [5.6, 6.0, 7.0, 6.6, 6.5, 4.6],
             [5.8, 6.1, 6.8, 6.3, 7.1, 5.0],
             [5.5, 4.8, 6.5, 6.4, 7.2, 4.5],
             [5.7, 5.9, 6.4, 6.3, 7.6, 6.0],
             [6.0, 6.5, 6.0, 6.0, 6.5, 4.9],
             [6.1, 6.0, 6.6, 6.0, 6.3, 5.1],
             [5.6, 6.3, 6.7, 5.7, 6.1, 5.4]],
             'x_labels': 'Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8',
             'line_labels': '5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000',
             'incomes': parser_html,
             'incomes_input': parser_html[:-1] if (rest and parser_html != 'None') else parser_html,
             'tabulated_incomes': parser_pandas,
             'rest': 1 if rest else 0 })
"""
def graph_3 (request, incomes):
    # Parse incomes variable:
    parser_html, parser_pandas, rest = urlParser(incomes)

    return render(request, "graph_view/graph_3.html",
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
            'rest': 1 if rest else 0 })




"""
Note: This view is a general view of the three graphic at the same time for a given postal code
"""
def general (request, postal_code):

    return render(request, "graph_view/general_analysis.html",{
        'data_graph_1':
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
        'data_graph_2': [6.5, 5.7, 5.4, 5.1, 4.7, 4.3],
        'bar_labels_graph_2': "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000",
        'data_graph_3':
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
        'postal_code': postal_code,
        'location': 'PS Sant Joan 154 6º2'})




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
