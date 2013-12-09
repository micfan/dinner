// dinner.js
// ~~~~~~~~~
// Micheal Fan, 2015-03-23

// 配置Vue变量标签
Vue.config.delimiters = ["[", "]"];

Vue.directive('disable', function (value) {
    this.el.disabled = !!value;
});
/*
$.ajax({
  url: url,
  type: 'post',
  dataType: 'json',
  data: pdata,
  success: function(response) {
    data.message = response.detail;
  }
});
*/

var test = new Vue({
  el: '#test0',
  data: {
    selected: false
  },
  methods: {
        onClick: function (e) {
            // console.log(e.target.tagName) // "A"
            // console.log(e.targetVM === this) // true
            // e是原生的DOM事件对象
            // this 指向该ViewModel实例
            var self = this;
            var url = '/dinner/';  // todo: js动态URL
            var pdata = {
              selected: Number(this.selected),
              cal_id: 84
            };
            // todo: jQuery.Ajax能利用Http StatusCode吗?
            // todo: Loading菊花。。
            $.post(url, pdata, function(response) {
              if (response.ec === 0) {
                self.selected = !self.selected;
                $('#order_count').html(response.data);
              } else {
                // todo: 显示错误提示
                ///
                ///
              }
            }, 'json');
        }
    }
});
