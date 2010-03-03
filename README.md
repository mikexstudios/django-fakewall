django-fakewall by Michael Huynh (mike@mikexstudios.com)

Purpose:
-------

A very simple app containing a middleware file that checks to see if a
"maintenance mode" setting flag has been set. If True, then shows the
mainteance page to everyone visiting the site unless a secret bypass
code has been entered.

Tested:
------

Django 1.1.1 and Django 1.2 b1.

How to use
----------

1.  Place the directory 'django_fakewall' somewhere in your path. You can do this
    by running setup.py or installing through pip.

2.  Edit settings.py and add `django_fakewall.middleware.FakewallMiddleware` to 
    your `MIDDLEWARE_CLASSES`.

3.  Add the following settings to settings.py:
        #############################
        # django-fakewall settings: #
        #############################
        
        #Turns the maintenance mode fakewall on if True, off if False (default).
        FAKEWALL_MODE = True

        #The secret code that user enters as part of URL params to bypass the
        #fakewall:
        FAKEWALL_BYPASS_CODE = 'mycode' #change this to something secret


4.  A default fakewall template has been provided in 
    `templates/django_fakewall/fakewall.html`. If you would like to override this,
    create the same file in one of your apps using the same directory structure.

5.  Now when you visit your site, you should see the fakewall page. To bypass it,
    enter the bypass code as part of the URL like:
    `http://localhost:8000/?bypass=mycode`
    Then subsequent visits to your site will not need the bypass code anymore.

6.  To unset the bypass code, enter `unset` as the bypass code like:
    `http://localhost:8000/?bypass=unset`
    Then you should see the fakewall page again.

