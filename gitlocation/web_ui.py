"""Display Git URLs in the Browse Source section."""

import re

from genshi.builder import tag
from trac.core import *
from trac.config import Option
from trac.web import IRequestFilter
from trac.web.chrome import add_ctxtnav

def prepend_ctxtnav(req, elm_or_label, href):
    """Prepend an entry to the current page's ctxtnav bar.
    
    add_ctxtnav(), sadly, always appends to the right side of the (right-aligned by default) context nav, changing the onscreen locations of the links people are already used to.
    """
    elm = tag(tag.label(elm_or_label, for_='rev'), ' ',
              tag.input(type='text', id='rev', readonly='readonly',
                        value=href, size=len(href)))
    req.chrome.setdefault('ctxtnav', []).insert(0, elm)

class BrowserLinkAdder(Component):
    implements(IRequestFilter)

    git_base_url = Option('git', 'repository_url',
                          doc="base URL of git repository")
    pattern = re.compile(r'/browser(/.*|$)')

    def url(self):
        return self.git_base_url.rstrip(u'/')

    ### IRequestFilter methods
    
    def pre_process_request(self, req, handler):
        """Do nothing."""
        return handler
    
    def post_process_request(self, req, template, data, content_type):
        """Stick the Git Location link in the contextual nav when applicable."""
        match = self.pattern.match(req.path_info)
        if match:
            prepend_ctxtnav(req, 'Git location', self.url())
        return template, data, content_type
