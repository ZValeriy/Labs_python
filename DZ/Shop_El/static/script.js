jQuery(document).ready(function ($) {
   //разрешаем выводить данные
   var block = true;
   //номер страницы для вывода
   var page = 0;
   //скроллинг
   $(window).scroll(function () {
      if ($(window).height() + $(window).scrollTop() >= $(document).height() && block) {
         block = false;
         page++;
         $.ajax({
                type: 'GET',
                url: 'pagination/' + page,
                success: function (list) {
            stopLoading();
            if (list == '') {
               block = false;
            } else {
               $('.product').append(list);
               block = true;
            }
                }
            });
            startLoading();
        }
   });
   //старт анимация ajax
   function startLoading() {
      $('.loading').fadeIn(300);
   }
   //конец анимации ajax
   function stopLoading() {
      $('.loading').fadeOut();
   }
});