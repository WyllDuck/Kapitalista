from django.shortcuts import render

"""
'data' <LIST> == Percentage of people with the same ""grades"" AND ""income""
    - The lists inside the main list are ordered in the same order as "bar_labels"
    - The values inside the secondary lists are ordered in the same order as "x_labels"
'x_labels' <STRING> == The desire interval of grades in the subject
'bar_labels' <STRING> == The desire incomes that the end-user wants to check
'title' <STRING> == Name of the university subject that the end-user wants to check

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
            'bar_labels': "5000-10000, 10000-12500, 12500-15000, 15000-20000, 20000-30000,+ 30000",
            'title': 'TMM (Theory in Machines and Mechanism)'})
"""
def graph_1 (request):
    return render(request, "graph_view/graph_1.html", 
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
            'bar_labels': "5000-10000, 10000-12500, 12500-15000, 15000-20000, 20000-30000,+ 30000",
            'title': 'TMM (Theory in Machines and Mechanism)'})




"""
'data' <LIST> == Average timestamp to have the engineering degree separated by income
    - The values in the list are in the same order as the different incomes in 'bar_labels'
'bar_labels' <STRING> == The desire incomes that the end-user wants to check

FORMAT EXAMPLE:

        {'data': [6.5, 5.7, 5.4, 5.1, 4.7, 4.3],
            'bar_labels': "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000"})
"""
def graph_2 (request):
    return render(request, "graph_view/graph_2.html", 
        {'data': [6.5, 5.7, 5.4, 5.1, 4.7, 4.3],
            'bar_labels': "5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000"})




"""
'data' <LIST> == Grades of Students with same income over the subjects of all the quarters
'x_labels' <STRING> == The desire quarters that the end-user wants to check
'line_labels' <STRING> ==  The desire incomes that the end-user wants to check

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
            'line_labels': '5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000'})
"""
def graph_3 (request):
    return render(request, "graph_view/graph_3.html",
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
            'line_labels': '5000-10000,10000-12500,12500-15000,15000-20000,20000-30000,+ 30000'})




"""
Note: This view is a general view of the three graphic at the same time for a given postal code
"""
def general (request):
    return render(request, "graph_view/general_analysis.html")
    
