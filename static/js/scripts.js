$(function() {
    $('#btnSubmit').click(function() {
        $.redirect(
            '/subscribers/',
            {'inputApiKey': $("#inputApiKey").val(),
             'inputUsername': $("#inputUsername").val(),
             'inputList': $("#inputList").val()
            },
            'POST'
        );
    });
});

/*
$(function() {
    $('button').click(function() {
        $.ajax({
            url: '/delete_subscriber/' + $.param({"inputUsername": $(this).attr('id')}),
            type: 'DELETE',
            data: {'inputUsername': $(this).attr('id')},
            headers: {'inputUsername': $(this).attr('id')},
            success: function(result) {
                console.log(response);
        }
});
    });
});*/


$(function() {
    $('#btnSubmitSubscriber').click(function() {
        $.redirect(
            '/add_subscriber/',
            {'inputName': $("#inputName").val(),
             'inputMail': $("#inputMail").val()
            },
            'PUT'
        );
    });
});
