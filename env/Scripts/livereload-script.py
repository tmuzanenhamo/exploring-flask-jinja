#!"c:\users\tmuza\downloads\jinja\jinja examples\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'livereload==2.6.2','console_scripts','livereload'
__requires__ = 'livereload==2.6.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('livereload==2.6.2', 'console_scripts', 'livereload')()
    )
