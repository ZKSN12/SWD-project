$(document).ready(function() {
    $( "#createButton" ).click(function() {
        $.ajax({
            url: '',
            data: {
                text : $("#location").text(),
            },
            type: 'get',
            success: function(response){
                $("#text").append('<li>'+ $("#location").text() + '</li>')
            }
        });
    
    });

 });


