document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('input[name="postal_code"]').onchange = changeEventHandler;
}, false);

function changeEventHandler(event) {
    if (event.target.value == 'home') {
        document.getElementById('postal_label_home').style.display = "none";
        document.getElementById('postal_label_school').style.display = "block";
        this.value = 'school';
    } else if (event.target.value == 'school') {
        document.getElementById('postal_label_home').style.display = "block";
        document.getElementById('postal_label_school').style.display = "none";
        this.value = 'home';
    };
    AJAX_refresh()
};


function AJAX_refresh() {

    var subject = document.getElementById('subject').value;
    subject = subject.split(':')[0]

    var postal_code = document.getElementById('postal_code_checkbox').value
    postal_code = postal_code.toUpperCase()

    $.ajax({
            type: "GET",
            url: "graph_1_AJAX",
            data: { 'subject': subject, 'postal_code': postal_code }
        })
        .done(function(response) {

            // Removing the current data
            $("#chart_1").html("");

            // Adding new data
            $('#chart_1').append(response);
        });

    $.ajax({
            type: "GET",
            url: "graph_5_AJAX",
            data: { 'subject': subject, 'postal_code': postal_code }
        })
        .done(function(response) {

            // Removing the current data
            $("#chart_5").html("");

            // Adding new data
            $('#chart_5').append(response);
        });
};