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

    if (income_from >= income_to || income_from > 60000 || income_to > 60000) {
        document.getElementById("alert_1").style.display ="block";
        document.getElementById("alert_2").style.display ="none";
        return false
    } else if (Array_subArray(incomes, Array(income_from, income_to))){
        document.getElementById("alert_2").style.display ="block";
        document.getElementById("alert_1").style.display ="none";
        return false
    } else {
        document.getElementById("alert_1").style.display ="none";
        document.getElementById("alert_2").style.display ="none";
        return true
    }
}

function Array_subArray(array, subarray){
    for (var i = 0; i < array.length; i++){
        if (String(array[i]) === `${subarray[0]},${subarray[1]}`){
          return true
        }
    } return false
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('input[name="postal_code"]').onchange = changeEventHandler;
}, false);

function changeEventHandler(event) {
    if (event.target.value == 'home') {
        document.getElementById('postal_label_home').style.display ="none";
        document.getElementById('postal_label_school').style.display ="block";
        this.value = 'school';
    } else if (event.target.value == 'school') {
        document.getElementById('postal_label_home').style.display ="block";
        document.getElementById('postal_label_school').style.display ="none";
        this.value = 'home';
    };
};

function add(){

    if (verify()){
      var incomes = $('#tabulated_incomes').data().other;

      if (incomes === 'None'){
        incomes = new Array()
      }

      // Get values from HTML:
      var income_from = Number(document.getElementById("income_from").value);
      var income_to = Number(document.getElementById("income_to").value);
      var value = new Array(income_from, income_to);

      var rest = document.getElementById("rest").checked

      incomes.push(value)
      var url = '';
      for (var i = 0; i < incomes.length; i++) {
          // unit_1
          if (String(incomes[i][0]).substr(-3) === '000'){
              var unit_1 = String(incomes[i][0]).slice(0, -3)
          } else {
              var unit_1 = `${ String(incomes[i][0]).slice(0, -3) }k${ String(incomes[i][0]).substr(-3) }`
          }

          // unit_2
          if (String(incomes[i][1]).substr(-3) === '000'){
              var unit_2 = String(incomes[i][1]).slice(0, -3)
          } else {
              var unit_2 = `${ String(incomes[i][1]).slice(0, -3) }k${ String(incomes[i][1]).substr(-3) }`
          }

          if (i != incomes.length - 1){
              var span = `${unit_1}_${unit_2}a`
          } else if (i == incomes.length - 1 && !rest) {
              var span = `${unit_1}_${unit_2}`
          } else if (i == incomes.length - 1 && rest) {
              var span = `${unit_1}_${unit_2}a`
          }
          url += span
      }
      if (rest){
          url += 'REST'
      }
      document.location.href = url
    }
}

function remove(value){

    // Get values from HTML:
    var rest = Number($('#_rest').data().other);
    var incomes = $('#tabulated_incomes').data().other;
    var remove = document.getElementById('remove').value;

    if (remove !== 'Default select'){
        var remove = remove.split('-')
    } else {
        return
    }

    for (var i = 0; i < incomes.length; i++){
        if (String(incomes[i]) === String(remove)){
          incomes.splice(i, 1)
        }
    }

    var url = '';
    for (var i = 0; i < incomes.length; i++) {
        // unit_1
        if (String(incomes[i][0]).substr(-3) === '000'){
            var unit_1 = String(incomes[i][0]).slice(0, -3)
        } else {
            var unit_1 = `${ String(incomes[i][0]).slice(0, -3) }k${ String(incomes[i][0]).substr(-3) }`
        }

        // unit_2
        if (String(incomes[i][1]).substr(-3) === '000'){
            var unit_2 = String(incomes[i][1]).slice(0, -3)
        } else {
            var unit_2 = `${ String(incomes[i][1]).slice(0, -3) }k${ String(incomes[i][1]).substr(-3) }`
        }

        if (i != incomes.length - 1){
            var span = `${unit_1}_${unit_2}a`
        } else if (i == incomes.length - 1 && !rest) {
            var span = `${unit_1}_${unit_2}`
        } else if (i == incomes.length - 1 && rest) {
            var span = `${unit_1}_${unit_2}a`
        }
        url += span
    }
    if (rest){
        url += 'REST'
    }
    document.location.href = url
}
