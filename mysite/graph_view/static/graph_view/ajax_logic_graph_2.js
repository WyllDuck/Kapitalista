document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('input[name="top_bottom"]').onchange = changeEventHandler_1;
}, false);

function changeEventHandler_1(event) {
    if (event.target.value == 'top') {
        document.getElementById('top_bottom_TOP').style.display = "none";
        document.getElementById('top_bottom_BOTTOM').style.display = "block";
        this.value = 'bottom';
    } else if (event.target.value == 'bottom') {
        document.getElementById('top_bottom_TOP').style.display = "block";
        document.getElementById('top_bottom_BOTTOM').style.display = "none";
        this.value = 'top';
    };
    AJAX_refresh()
};

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('input[name="postal_code"]').onchange = changeEventHandler_2;
}, false);

function changeEventHandler_2(event) {
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

    var top_bottom = document.getElementById('top_bottom_checkbox').value
    top_bottom = top_bottom.toUpperCase()

    var percent = document.getElementById('percent').value

    $.ajax({
            type: "GET",
            url: "graph_6_AJAX",
            data: { 'subject': subject, 'postal_code': postal_code, 'percent': percent, 'top_bottom': top_bottom }
        })
        .done(function(response) {

            // Removing the current data
            $("#chart_6").html("");

            // Adding new data
            $('#chart_6').append(response);
        });
};