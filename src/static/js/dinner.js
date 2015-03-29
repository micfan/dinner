// dinner.js
// ~~~~~~~~~
// Micheal Fan, 2015-03-23

// 配置Vue变量标签
/*Vue.config.delimiters = ["[", "]"];

Vue.directive('disable', function (value) {
    this.el.disabled = !!value;
});
*/
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

    $('.is-changeable').on('click', function() {
      toggleBookStatus($(this));
    });

  })();
});

