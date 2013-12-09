* build global webpage
* start apps
* build django models
* use twwiter bower manage javascript files
* write basic test case
* seprate local settings from public's
* DEBUG = False, but 500 Error
* learn and accept Apple UX UI UE, is important


django_pipeline
------
Django 项目中，静态资源的管理要更复杂一些，要额外处理的事情包括：

Less / CoffeeScript 等自动编译成 CSS／JS
“压缩” CSS／JS 文件，以提高浏览器加载速度
合并零碎的 CSS／JS 文件，减少浏览器请求，降低服务器请求建立的频率
静态资源文件的版本化：浏览器会缓存静态文件，后台代码和静态资源都发生更新后，浏览器很可能从缓存提取过期的静态，导致页面显示异常
Django 静态资源管理利器 - django-pipeline 正是用来解决上述问题

-----
http://yeoman.io/ --> Grunt build system, Bower manage javascrpt libs.
