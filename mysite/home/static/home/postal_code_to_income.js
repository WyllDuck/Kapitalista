function postal_code_to_income() {

    var postal_code = document.getElementById("postal_code_income_input").value;

    url = "{% url 'home:postal_code' %}".replace('0', postal_code);

    if (postal_code >= 0 && postal_code <= 99999) {
        $.ajax({
                type: "GET",
                url: 'http://127.0.0.1:8000/postal_code',
                data: { 'postal_code': postal_code }
            })
            .done(function(response) {

                // Removing the current data
                $("#income_AJAX").html("");

                // Adding new data
                $('#income_AJAX').append(response);
            });
    }
};