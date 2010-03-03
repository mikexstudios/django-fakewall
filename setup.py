from setuptools import setup, find_packages

setup(
    name = 'django_fakewall',
    packages = find_packages(),
    version = '1.0.0',
    description = 'Simple middleware that shows a "maintenance" page unless secret code is entered.',
    author = 'Michael Huynh',
    author_email = 'mike@mikexstudios.com',
    url = 'http://github.com/mikexstudios/django-fakewall',
    classifiers=[
        'Programming Language :: Python', 
        'Framework :: Django', 
        'License :: OSI Approved :: BSD License',
    ]
)

