# darklms
Dark theme for Moodle LMS

Bookmarklet Code

`
javascript: (function() {
    if (window.addCss !== undefined) {
        window.addCss();
    } else {
        var ss = document.createElement('link');
        ss.rel = "stylesheet";
        ss.type = "text/css";
        ss.href = "https://gitcdn.link/repo/anuditnagar/darklms/master/darklms.css";
        document.head.appendChild(ss);
    }
})();
`
