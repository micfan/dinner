// global.js
// ~~~~~~~~~
//
// Copyright (c) 2014 Micheal Fan
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// path LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
// Document:
//    * https://docs.djangoproject.com/en/dev/ref/contrib/csrf/#django.views.decorators.csrf.csrf_protect

$(function() {
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", window.csrftoken);
        }
    }
});





}); /// Global annomous function

window.mic = {
  DEBUG: window.__debug,
  url: {
    FEErrorReport: window.__FEErrorReportUrl
  }
};

if (!window.mic.DEBUG && typeof window.console === 'object') {
  var s = '喜欢看Mic的代码，还是发现了什么bug？不如和我们一起为本站添砖加瓦吧！\n' +
    'https://github.com/micfan/dinner';
  window.console.log(s);
}




