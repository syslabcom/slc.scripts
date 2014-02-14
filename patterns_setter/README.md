This script provides a web service which generates a build.js file based on the parameters of a GET request. The parameters determine which patterns shall be included.

Example:
localhost:8081/set/patt?pat/focus=on&pat/legend=on

will create a build.js file which includes the patterns "focus" and "legend".

The script uses "make" and relies on a local copy off the "Patterns" repository. Please set patterns_dir=/path/to/Patterns in the script.