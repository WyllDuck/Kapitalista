function selector (){
  var subject = document.getElementById('subject').value;
  subject = subject.split(':')[0]
  document.location.href = String(subject);
}
