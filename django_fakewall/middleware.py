from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

class FakewallMiddleware(object):
    def process_request(self, request):
        #Check for cases where we will allow access:
        if not settings.FAKEWALL_MODE:
            return None
        if request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            return None

        #Now see if user has invoked bypass code:
        bypass_code = request.GET.get('bypass', False)
        if bypass_code == settings.FAKEWALL_BYPASS_CODE:
            request.session['fakewall_bypass_code'] = bypass_code
        elif bypass_code == 'unset':
            delattr(request.session, 'fakewall_bypass_code')
        
        #If bypass code is set, then we don't show maintenance page.
        if request.session.get('fakewall_bypass_code', False):
            return None
        
        #Otherwise, show maintenance page:
        return render_to_response('django_fakewall/fakewall.html', {},
                                  context_instance = RequestContext(request))
        
