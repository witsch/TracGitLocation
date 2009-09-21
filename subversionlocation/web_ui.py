"""Display Subversion URLs in the Browse Source section."""

import re

from genshi.builder import tag
from trac.core import *
from trac.config import Option
from trac.web import IRequestFilter
from trac.web.chrome import add_ctxtnav

def prepend_ctxtnav(req, elm_or_label, href, title=None):
    """Prepend an entry to the current page's ctxtnav bar.
    
    add_ctxtnav(), sadly, always appends to the right side of the (right-aligned by default) context nav, changing the onscreen locations of the links people are already used to.
    """
    elm = tag.a(elm_or_label, href=href, title=title)
    req.chrome.setdefault('ctxtnav', []).insert(0, elm)

class BrowserLinkAdder(Component):
    implements(IRequestFilter)

    svn_base_url = Option('svn', 'repository_url',
                          doc="base URL of svn repository")
    pattern = re.compile(r'/browser(/.*|$)')

    def url(self, path):
        return u'/'.join((self.svn_base_url.rstrip(u'/'), path.lstrip(u'/')))

    ### IRequestFilter methods
    
    def pre_process_request(self, req, handler):
        """Do nothing."""
        return handler
    
    def post_process_request(self, req, template, data, content_type):
        """Stick the Subversion Location link in the contextual nav when applicable."""
        match = self.pattern.match(req.path_info)
        if match:
            prepend_ctxtnav(req, 'Subversion Location', self.url(match.group(1)), title="This location in the Subversion repository")
        return template, data, content_type
