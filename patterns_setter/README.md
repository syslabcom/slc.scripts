#patterns_setter.py

This script provides a web service which generates a bundle.js file based on the parameters of a GET request.

the URL HOST:PORT/set/patt will display a html page where patterns can be selected to be included in the bundle.js file.

Please perform the following steps:

1. check out an go to the patterns_setter directory
2. create a virtualenv
3. $ bin/easy_install pyramid
4. check out a copy of Patternslib/Patterns in a location of your choice
5. go to the patterns_setter directory
6. open patterns_setter.cfg in an editor and change the path to the patterns repository if needed
7. bin/python patterns_setter.py (optionally you can specify a hostname and a port on which the server should listen with --host and --port respectively (defaults to  localhost:8080)


