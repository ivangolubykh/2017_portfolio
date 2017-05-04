"use strict";

// Плавная прокрутка кнопки "вверх":
$(document).ready(function(){
    $("#scroll_up_button").hide();
    $(function () {
        $(window).scroll(function () {
            if ($(this).scrollTop() > 100) {
//            Через сколько пикселе йплявится кнопка
                $('.scroll_up_button').fadeIn();
            } else {
                $('.scroll_up_button').fadeOut();
            }
        });
        $('.scroll_up_button a').click(function () {
            $('body,html').animate({
                scrollTop: 0
            }, 400);
            return false;
        });
    });
});
