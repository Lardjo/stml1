/**
 * Created by konstantin on 07.12.13.
 */

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
})

$(document).on("click", ":submit", function(e){

    $.ajax({
        url: "/session/" + $(this).val(),
        type: "DELETE",
        success: $(document).ajaxStop(function(){
            window.location.reload();
        })
    });

});