$(document).on("click", ".group", function () {
     var id = $(this).data('id');
      $.ajax({
          type: "GET",
          url: window.location.pathname+window.location.search+"groups",

          success: function(response) {
            groups = JSON.parse(response);
            $(".modal-body #clusterGroupName")[0].innerHTML= id;
            $('#groupPicker').empty();
            $.each(groups, function(i, p) {
                var pickerElement = $('<option></option>').val(p[1]).html(p[1])
                pickerElement[0].dataset.id=p[0]
                $('#groupPicker').append(pickerElement);
            });
          },

          error: function(err) {
            console.log(err);
          }
        });
});


$(document).on("click", ".sendChangeButton", function () {
    var selector = $('#selectpicker')[0];
    var model_id = selector.options[selector.selectedIndex].dataset["id"];
    var host_name= $(".modal-body #clusterName")[0].innerHTML
    $.ajax({
          type: "POST",
          url: window.location.pathname+window.location.search+"change_model",
          dataType: "json",
          data:{
            "model_id":model_id,
            "host_name":host_name
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




$(document).on("click", ".change", function () {
     var id = $(this).data('id');
      $.ajax({
          type: "GET",
          url: window.location.pathname+window.location.search+"models",

          success: function(response) {
            list_of_models = JSON.parse(response);
            $(".modal-body #clusterName")[0].innerHTML= id ;
            $('#selectpicker').empty();
            $.each(list_of_models, function(i, p) {
                var pickerElement = $('<option></option>').val(p[1]).html(p[1])
                pickerElement[0].dataset.id=p[0]
                $('#selectpicker').append(pickerElement);
            });
          },

          error: function(err) {
            console.log(err);
          }
        });
});
$(document).on("click", ".createGroup", function () {
    var groupName= $('#groupNameInput')["0"].value;
    var host_name= $(".modal-body #clusterGroupName")[0].innerHTML
    $.ajax({
          type: "POST",
          url: window.location.pathname+window.location.search+"set_group",
          dataType: "json",
          data:{
            "group":groupName,
            "host_name":host_name
          },
          success: function(data) {
            console.log("Group changed!")
            window.location.href = data["go"];
          },
          error: function(err) {
            console.log(err);
          }
        });
});

$(document).on("click", ".changeModelGroup", function () {
    var groupName= $('#groupNameInput')["0"].value;
    var host_name= $(".modal-body #clusterGroupName")[0].innerHTML
    $.ajax({
          type: "POST",
          url: window.location.pathname+window.location.search+"set_group",
          dataType: "json",
          data:{
            "group":groupName,
            "host_name":host_name
          },
          success: function(data) {
            console.log("Group changed!")
            window.location.href = data["go"];
          },
          error: function(err) {
            console.log(err);
          }
        });
});