//modal function

$(document).ready(function(){
  $('.modal').modal();
});

$(document).ready(function(){
  $('form').submit(function(event){
    event.preventDefault()
    form = $("form")

    $.ajax({
      'url':'/ajax/rate_project/',
      'type':'POST',
      'data':form.serialize(),
      'dataType':'json',
      'success': function(data){
        alert(data['success'])
      },
    })
    $('#id_design').val('')
    $("#id_usability").val('')
    $("#id_content").val('')
  }) // End of submit event

}) // End of document ready function