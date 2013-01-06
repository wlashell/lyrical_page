=====
Lyrical Page
=====

Lyrical Page is a website development app for the Django framework. Roughly based
on the original Django flatpages contrib app with ideas pulled from a variety sources
across the internet.

The system is designed to be modular and compliment Django's philosophy of staying out
of the way of the developer. The code base has continued to evolve through real world use
in different types of websites.

Detailed documentation is a work in progress.

Quick start
-----------

1.  Add site_content, and site_seo to your INSTALLED_APPS in the following manner:

    INSTALLED_APPS = (
    ...
    'site_content',
    'site_seo',
    )

2.  If you are using the site_seo app, add the context processor to your settings file:

    TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    'site_seo.context_processors.site_seo',
    )

3.  Add the middleware classes to your settings file.  These middlware should be the last
    entries in your list/tuple.
    
    MIDDLEWARE_CLASSES = (
    ...
    'site_content.middleware.SitePageFallbackMiddleware',
    'site_seo.middleware.SiteSeoMiddleware',
    )

4.  Run 'python manage.py syncdb' to create new database tables and supplemental database
    actions.

5.  Log into the Django admin site and you can now add site_content site pages as you need.

Will LaShell <wlashell@lyrical.net>
