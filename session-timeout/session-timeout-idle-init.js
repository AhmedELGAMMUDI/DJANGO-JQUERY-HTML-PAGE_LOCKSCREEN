var SessionTimeout = function() { var i = function() { $.sessionTimeout({ title: screen_title, message: screen_info, redirUrl: "/Pages-Lockscreen/", logoutUrl: "login2.html", warnAfter: 600000, redirAfter: 615000, ignoreUserActivity: 0, countdownMessage: "{timer}" + ' ' + screen_time, countdownBar: !0 }) }; return { init: function() { i() } } }();
jQuery(document).ready(function() { SessionTimeout.init() });