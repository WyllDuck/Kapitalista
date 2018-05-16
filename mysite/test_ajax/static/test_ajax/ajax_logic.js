function AJAX_refresh() {

    var subject = document.getElementById('subject').value;
    subject = subject.split(':')[0]

    $.ajax({
            type: "GET",
            url: "graph_1_AJAX",
            data: { 'subject': subject }
        })
        .done(function(response) {

            // Removing the current data
            $("#chart_1").html("");

            // Adding new data
            $('#chart_1').append(response);
        });
};