/**
 * Created by konstantin on 07.12.13. Version 1.0.5
 */

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
})

$(document).on("click", ".session-delete:submit", function(){

    $.ajax({
        url: "/session/" + $(this).val(),
        type: "DELETE",
        success: function() {
            window.location.reload();
        }
    });
});

$(document).on("click", ".bookmark:submit", function(){

    $.ajax({
        type: "POST",
        success: function() {
            window.location.reload();
        }
    });
});

$(document).on("click", ".remove-bookmark:submit", function(){

    $.ajax({
        type: "POST",
        data: {match:  $(this).val()},
        success: function() {
            window.location.reload();
        }
    });
});

var $container  = $('#ib-container'),
    $articles   = $container.find('a'),
    timeout;

$articles.on( 'mouseenter', function() {

    var $article    = $(this);
    clearTimeout( timeout );
    timeout = setTimeout( function() {

        if( $article.hasClass('active') ) return false;

        $articles.not($article).removeClass('active').addClass('blur').children('span').fadeOut(400);

        $article.removeClass('blur').addClass('active').children('span').fadeIn(400);

    }, 100 );

});

$container.on( 'mouseleave', function() {

    clearTimeout( timeout );
    $articles.removeClass('active blur').children('span').fadeOut(400);

});