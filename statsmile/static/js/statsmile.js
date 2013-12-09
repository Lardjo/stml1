/**
 * Created by konstantin on 07.12.13. Version 1.0.5
 */

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
})

$(document).on("click", ":submit", function(e){

    $.ajax({
        url: "/session/" + $(this).val(),
        type: "DELETE",
        success: function() {
            window.location.reload();
        }
    });

});