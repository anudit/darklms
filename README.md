# Dark theme for Moodle LMS

## Installation 
### 1<sup>st</sup> Method

1. Install the [Tampermonkey Chrome Extension](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)

2. Install the script from [Greasy Fork](https://greasyfork.org/en/scripts/382637-dark-lms) (alternatively, insert a new Userscript into TamperMonkey and copy and paste in the [script](tampermonkey.js)).

3. With the Tampermonkey Script enabled, simply open LMS.

### 2<sup>nd</sup> Method

1. Create a new Bookmark and copy and paste the folowing code in the address field.

    `
    javascript: (function() {
        if (window.addCss !== undefined) {
            window.addCss();
        } else {
            var ss = document.createElement('link');
            ss.rel = "stylesheet";
            ss.type = "text/css";
            ss.href = "https://gitcdn.xyz/repo/anuditnagar/darklms/master/darklms.min.css";
            document.head.appendChild(ss);
        }
    })();
    `


2. Click on the Bookmark to turn of the lights
