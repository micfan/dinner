"use strict";

$(function () {

  function toggleBookStatus($el) {
    // todo: 动态URL
    var url = '/dinner/';
    var hasBooked = $el.hasClass('has_booked') ? 1 : 0;
    var data = {
      has_booked: hasBooked,
      cal_id: $el.attr('cal-id')
    };
    $.post(url, data, function(response) {
      if (response.ec === 0) {
        $el.toggleClass('has_booked');
        $('#order_count').html(response.data);
      } else {
        // todo: page.error(response.message)
      }
    });
  }

  (function main() {
    // todo: 登录跳转
    $('.is-changeable').on('click', function() {
      toggleBookStatus($(this));
    });

  })();
});

