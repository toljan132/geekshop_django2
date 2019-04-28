window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;

        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value,
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });

         $.ajax({
            url: "/basket/",
            success: function (data) {
            	data = $(data).find('#top_basket_list');
                $('#top_basket_list').html(data);
            }
        });

        event.preventDefault();
    });
};
