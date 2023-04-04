
// set time for disapearing django-flash-message
  setTimeout(function () {
    let messages = document.getElementById('flash-msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 1500);
  
  
  