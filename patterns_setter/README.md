This script provides a web service which generates a build.js file based on the parameters of a GET request. The parameters determine which patterns shall be included.

Example:
localhost:8080/set/patt?pat/focus=on&pat/legend=on

will create a build.js file which includes the patterns "focus" and "legend".

Please perform the following steps:

1. check out
2. check out a copy of Patternslib / Patterns
3. open the script in an editor and set patterns_dir=/path/to/Patterns/repository
4. change server_port if needed