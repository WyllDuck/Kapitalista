function incrementValue(tab) {
    var value = parseInt(document.getElementById(tab).value, 10);
    value = isNaN(value) ? 0 : value;
    value = value + 100;
    document.getElementById(tab).value = value;
}

function decrementValue(tab) {
    var value = parseInt(document.getElementById(tab).value, 10);
    value = isNaN(value) ? 0 : value;
    if (value <= 0) {
        value = 0;
    } else {
        value = value - 100;
    }
    document.getElementById(tab).value = value;
}

function verify() {

    var income_from = Number(document.getElementById("income_from").value);
    var income_to = Number(document.getElementById("income_to").value);

    var incomes = $('#tabulated_incomes').data().other;

    if (income_from >= income_to || income_from >= 60000 || income_to >= 60000) {
        document.getElementById("alert_1").style.display = "block";
        document.getElementById("alert_2").style.display = "none";
        return false
    } else if (Array_subArray(incomes, Array(income_from, income_to))) {
        document.getElementById("alert_2").style.display = "block";
        document.getElementById("alert_1").style.display = "none";
        return false
    } else {
        document.getElementById("alert_1").style.display = "none";
        document.getElementById("alert_2").style.display = "none";
        return true
    }
}

function Array_subArray(array, subarray) {
    for (var i = 0; i < array.length; i++) {
        if (String(array[i]) === `${subarray[0]},${subarray[1]}`) {
            return true
        }
    }
    return false
}

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
};


function add_subject() {

    // Get other variables:
    var rest = Number($('#_rest').data().other);
    var incomes = $('#tabulated_incomes').data().other;

    if (incomes === 'None') {
        incomes = new Array()
    }

    // Add subject:
    var subjects_list = String($('#subjects_js').data().other);
    if (subjects_list === 'None') {
        subjects_list = new Array()
    } else {
        var subjects_list = subjects_list.split('a')
    }

    if (subjects_list.length <= 4) {
        var newValue = document.getElementById('add_subject').value
        var newValue = newValue.split(':')[0]
        subjects_list.push(newValue)
        var subjects_list = subjects_list.join('a')
    } else {
        return
    }

    var income_url = get_income_url(incomes, rest)
    var postal_code = document.querySelector('input[name="postal_code"]').value.toUpperCase()
    go_to_url(income_url, subjects_list, postal_code)

}

function remove_subject() {

    // Get other variables:
    var rest = Number($('#_rest').data().other);
    var incomes = $('#tabulated_incomes').data().other;

    if (incomes === 'None') {
        incomes = new Array()
    }

    // Remove subject:
    var subjects_list = String($('#subjects_js').data().other);
    if (subjects_list === 'None') {
        return
    } else {
        var subjects_list = subjects_list.split('a')
    }

    if (subjects_list.length != 1) {
        var newValue = document.getElementById('remove_subject').value
        var newValue = newValue.split(':')[0]

        // Get the value you want to remove
        var index = subjects_list.indexOf(newValue);
        if (index > -1) {
            subjects_list.splice(index, 1);
        } else {
            return
        }

        var subjects_list = subjects_list.join('a')
    } else {
        subjects_list = 'None'
    }

    var income_url = get_income_url(incomes, rest)
    var postal_code = document.querySelector('input[name="postal_code"]').value.toUpperCase()
    go_to_url(income_url, subjects_list, postal_code)

}


function add() {

    if (verify()) {
        var incomes = $('#tabulated_incomes').data().other;

        if (incomes === 'None') {
            incomes = new Array()
        }

        // Get values from HTML:
        var income_from = Number(document.getElementById("income_from").value);
        var income_to = Number(document.getElementById("income_to").value);
        var value = new Array(income_from, income_to);

        var rest = document.getElementById("rest").checked

        incomes.push(value)

        // Get values form HTML subjects:
        var subjects_list = String($('#subjects_js').data().other);

        var income_url = get_income_url(incomes, rest)
        var postal_code = document.querySelector('input[name="postal_code"]').value.toUpperCase()
        go_to_url(income_url, subjects_list, postal_code)

    }
}

function remove(value) {

    // Get values from HTML incomes:
    var rest = Number($('#_rest').data().other);
    var incomes = $('#tabulated_incomes').data().other;
    var remove = document.getElementById('remove').value;

    if (incomes.length == 1) {
        rest = true
    }

    if (incomes === 'None') {
        incomes = new Array()
    }

    if (remove !== 'Default select') {
        var remove = remove.split('-')
    } else {
        return
    }

    for (i = 0; i < incomes.length; i++) {
        if (String(incomes[i]) === String(remove)) {
            incomes.splice(i, 1)
        }
    }

    // Get values form HTML subjects:
    var subjects_list = String($('#subjects_js').data().other);

    var income_url = get_income_url(incomes, rest)
    var postal_code = document.querySelector('input[name="postal_code"]').value.toUpperCase()
    go_to_url(income_url, subjects_list, postal_code)
}


// Change Url Function:
function get_income_url(incomes, rest) {

    var url = '';
    for (var i = 0; i < incomes.length; i++) {
        // unit_1
        if (String(incomes[i][0]).substr(-3) === '000') {
            var unit_1 = String(incomes[i][0]).slice(0, -3)
        } else {
            var unit_1 = `${ String(incomes[i][0]).slice(0, -3) }k${ String(incomes[i][0]).substr(-3) }`
        }

        // unit_2
        if (String(incomes[i][1]).substr(-3) === '000') {
            var unit_2 = String(incomes[i][1]).slice(0, -3)
        } else {
            var unit_2 = `${ String(incomes[i][1]).slice(0, -3) }k${ String(incomes[i][1]).substr(-3) }`
        }

        if (i != incomes.length - 1) {
            var span = `${unit_1}_${unit_2}a`
        } else if (i == incomes.length - 1 && !rest) {
            var span = `${unit_1}_${unit_2}`
        } else if (i == incomes.length - 1 && rest) {
            var span = `${unit_1}_${unit_2}a`
        }
        url += span
    }
    if (rest) {
        url += 'REST'
    }
    return url
}

function go_to_url(income_url, subjects_list, postal_code) {
    var host = window.location.host;

    // Get path and formating path:    
    var path = window.location.pathname;
    path = path.slice(1, path.length - 1)
    path = path.split('/')

    // Changing values path:
    path[2] = income_url
    path[3] = subjects_list
    path[4] = postal_code
    path = path.join('/')

    // Go to the new URL
    document.location.href = window.location.protocol + '//' + host + '/' + path
}