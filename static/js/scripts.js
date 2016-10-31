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

