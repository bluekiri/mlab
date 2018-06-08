

$(function(){
    //Groups
    $(document).on("click", ".group", function () {
         var id = $(this).data('id');
          $.ajax({
              type: "GET",
              url: window.location.pathname+window.location.search+"groups",

              success: function(response) {
                groups = JSON.parse(response);
                $(".modal-body #workerId")[0].innerHTML= id;
                $('#groupPicker').empty();
                $.each(groups, function(i, p) {
                    var pickerElement = $('<option></option>').val(p).html(p)
                    pickerElement[0].dataset.id=p[0]
                    $('#groupPicker').append(pickerElement);
                });
              },

              error: function(err) {
                console.log(err);
              }
        });
});


//Worker
$(document).on("click", ".sendChangeModelOnWorker", function () {
    var selector = $('#selectpicker')[0];
    var model_id = selector.options[selector.selectedIndex].dataset["id"];
    var host_name= $(".modal-body #hostName")[0].innerHTML
    $.ajax({
          type: "POST",
          url: window.location.pathname+window.location.search+"change_model",
          dataType: "json",
          data:{
            "model_id":model_id,
            "host_name":host_name
          },
          success: function(data) {
            window.location.href = data["go"];
          },
          error: function(err) {
            console.log(err);
          }
        });
});
// listener

$('input:checkbox').change(function(){
    var checked = $(this).is(':checked')
    var host = $(this).data('id');

    $.ajax({
          type: "POST",
          url: window.location.pathname+window.location.search+"enable_auto_publisher",
          dataType: "json",
          data:{
            "enable": checked,
            "host_name": host
          },
          success: function(data) {
            window.location.href = data["go"];
          },
          error: function(err) {
            console.log(err);
          }
        });
});

//


$(document).on("click", ".change", function () {
     var id = $(this).data('id');
      $.ajax({
          type: "GET",
          url: window.location.pathname+window.location.search+"models",

          success: function(response) {
            list_of_models = JSON.parse(response);
            $(".modal-body #hostName")[0].innerHTML= id ;
            $('#selectpicker').empty();
            $.each(list_of_models, function(i, p) {
                var pickerElement = $('<option></option>').val(p[1]).html(p[1])
                pickerElement[0].dataset.id=p[0]
                $('#selectpicker').append(pickerElement);

            });
            $('#selectpicker').selectpicker('refresh');
          },

          error: function(err) {
            console.log(err);
          }
        });
});

function changeGroupOnHost(host, group) {
    $.ajax({
          type: "POST",
          url: window.location.pathname+window.location.search+"set_group",
          dataType: "json",
          data:{
            "group":group,
            "host_name":host
          },
          success: function(data) {
            window.location.href = data["go"];
          },
          error: function(err) {
            console.log(err);
          }
        });
}

$(document).on("click", ".createGroup", function () {
    var groupName= $('#groupNameInput')["0"].value;
    var hostName= $(".modal-body #workerId")[0].innerHTML
    changeGroupOnHost(hostName,groupName)
});

$(document).on("click", ".sendChangeGroup", function () {
    var selector = $('#groupPicker')[0];
    var groupName= selector.options[selector.selectedIndex].value;
    var hostName= $(".modal-body #workerId")[0].innerHTML
    changeGroupOnHost(hostName,groupName)
});

$(document).on("click", ".sendChangeModelByGroup", function () {
    var selector = $('#groupSelectPicker')[0];
    var modelId = selector.options[selector.selectedIndex].dataset["id"];
    var groupName= $(".modal-body #groupName")[0].innerHTML
    $.ajax({
          type: "POST",
          url: window.location.pathname+window.location.search+"change_group_model",
          dataType: "json",
          data:{
            "model_id":modelId,
            "group_name":groupName
          },
          success: function(data) {
            console.log("Model changed!")
            window.location.href = data["go"];
          },
          error: function(err) {
            console.log(err);
          }
        });
});

$(document).on("click", ".changeModelGroup", function () {
     var groupName = $(this).closest('.groupContainer')[0].id;
      $.ajax({
          type: "GET",
          url: window.location.pathname+window.location.search+"models",

          success: function(response) {
            list_of_models = JSON.parse(response);
            $(".modal-body #groupName")[0].innerHTML= groupName;
            $('#groupSelectPicker').empty();
            $.each(list_of_models, function(i, p) {
                var pickerElement = $('<option></option>').val(p[1]).html(p[1])
                pickerElement[0].dataset.id=p[0]
                $('#groupSelectPicker').append(pickerElement);
            });
            $('#groupSelectPicker').selectpicker('refresh');
          },

          error: function(err) {
            console.log(err);
          }
        });
});

function findAncestor (el, cls) {
    while ((el = el.parentElement) && !el.classList.contains(cls));
    return el;
}

});
