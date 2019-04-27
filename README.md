# Dark theme for Moodle LMS

## Installation 
### 1<sup>st</sup> Method

1. Install the [TaperMonkey Chrome Extension](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)

2. Insert a new Userscript into TaperMonkey and copy and paste in the [script](tapermonkey.js).

3. With TaperMonkey Script enabled simply open LMS.

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


2. Click on the Bookmark to turn of the lights.

## Usage

1. With TaperMonkey enabled, navigate to any official Android Documentation, here is an [example](http://developer.android.com/reference/android/database/sqlite/SQLiteQueryBuilder.html).

