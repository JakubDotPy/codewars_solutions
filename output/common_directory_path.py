"""Kata - Common directory path

completed at: 2024-09-05 12:19:57
by: Jakub Červinka

Returns the commom directory path for specified array of full filenames.
```
 @param {array} pathes
 @return {string}
```
Examples:
 ```
   ['/web/images/image1.png', '/web/images/image2.png']  => '/web/images/'
   ['/web/assets/style.css', '/web/scripts/app.js',  'home/setting.conf'] => ''
   ['/web/assets/style.css', '/.bin/mocha',  '/read.me'] => '/'
   ['/web/favicon.ico', '/web-scripts/dump', '/webalizer/logs'] => '/'
```
(c)RSS
"""

import os

def get_common_directory_path(paths): 
    try:
        common_path = os.path.commonpath(paths)        
        common_path_with_sep = common_path + os.sep
    
        # Check if all paths start with the common path + separator
        if all(p.startswith(common_path_with_sep) for p in paths):
            return common_path_with_sep

        return common_path
        
    except ValueError:
        return ''
