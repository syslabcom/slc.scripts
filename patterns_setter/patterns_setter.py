from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import json
import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--host', dest='host', default='localhost')
parser.add_argument('--port', dest='port', default=8080)
args = parser.parse_args()

host = args.host
print "the host " + host + " has the type " + str(type(host))
try:
    port = int(args.port)
    print 'the port is: ' + str(port)
except ValueError:
    print "Port number must be an integer!"
    exit()
working_dir = os.getcwd() + "/"

config = open(working_dir + "patterns_setter.cfg",'rb')
config.readline()
patterns_dir = os.getcwd() + '/' + config.readline().strip()
if patterns_dir[-1] != "/":
    patterns_dir = patterns_dir + "/"

print patterns_dir

TPL_head = """/* Patterns bundle configuration.
*
* This file is used to tell r.js which Patterns to load when it generates a
* bundle. This is only used when generating a full Patterns bundle, or when
* you want a simple way to include all patterns in your own project. If you
* only want to use selected patterns you will need to pull in the patterns
* directly in your RequireJS configuration.
*/

define([
    "jquery",
    "registry",
    "parser",
    "htmlparser",
    "depends_parse",
    "dependshandler",
"""

TPL_tail = """
], function($, registry) {
    window.patterns = registry;
    $(function () {
        registry.init();
    });
    return registry;
});
"""

CONFMAP = {
'pat/ajax': 'ajax',
'pat/autofocus': 'autofocus',
'pat/autoscale': 'autoscale',
'pat/autosubmit': 'autosubmit',
'pat/autosuggest': 'autosuggest',
'pat/breadcrumbs': 'breadcrumbs',
'pat/bumper': 'bumper',
'pat/carousel': 'carousel',
'pat/checkedflag': 'checkedflag',
'pat/checklist': 'Checklist',
'pat/chosen': 'chosen',
'pat/collapsible': 'collapsible',
'pat/depends': 'depends',
'pat/edit-tinymce': 'edit-tinymce',
'pat/equaliser': 'equaliser',
'pat/expandable':'expandable',
'pat/focus': 'focus',
'pat/formstate': 'formstate',
'pat/forward': 'forward',
'pat/fullcalendar': 'fullcalendar',
'pat/gallery': 'gallery',
'pat/image-crop': 'image-crop',
'pat/inject': 'inject',
'pat/input-change-events': 'input-change-events',
'pat/legend': 'legend',
'pat/less': 'less',
'pat/menu': 'menu',
'pat/modal': 'modal',
'pat/markdown': 'markdown',
'pat/modal': 'modal',
'pat/modernizr': 'modernizr',
'pat/navigation': 'navigation',
'pat/placeholder': 'placeholder',
'pat/prefixfree': 'prefixfree',
'pat/skeleton': 'skeleton',
'pat/slides': 'slides',
'pat/slideshow-builder': 'slideshow-builder',
'pat/sortable': 'sortable',
'pat/stacks': 'stacks',
'pat/store': 'store',
'pat/subform': 'subform',
'pat/switch': 'switch',
'pat/toggle': 'toggle',
'pat/tooltip': 'tooltip',
'pat/url': 'url',
'pat/validate': 'validate',
'pat/zoom': 'zoom'
}


def set_patts(request):

    if len(request.GET.keys())==0:
        data = open('index.html','rb').read()
        mResponse = Response(data)
        mResponse.headers['content-type'] = 'text/html'
        return mResponse
           
    custom_config = "\n"                                 # string that contains all the patterns that are to be included
    
    for key in request.GET.keys():                       # parse query string for patterns and add them
        if key.startswith('pat/'):
            custom_config += '    "' + CONFMAP[key] + '",\n'

    if len(custom_config) > 1:
        custom_config = custom_config[:-2] + "\n"

    config = TPL_head + custom_config + TPL_tail         # write patterns.js
    data = open(patterns_dir + 'src/' + 'patterns.js', 'wb')
    data.write(config)
    data.close()

    os.chdir(patterns_dir)                              # run make
    subprocess.call(["make"])
    os.chdir(working_dir)
        
    data = open(patterns_dir + 'bundle.js', 'rb').read() # create response with bundle.js as attachment
    mResponse = Response(data)
    mResponse.headers['content-type'] = 'application/javascript'
    mResponse.headers['content-disposition'] = 'attachment;filename=bundle.js'    

    return mResponse

if __name__ == '__main__':              # set up pyramid
    config = Configurator()
    config.add_route('set', '/set/{name}')
    config.add_view(set_patts, route_name='set')
    app = config.make_wsgi_app()
    server = make_server(host, port, app)
    server.serve_forever()
