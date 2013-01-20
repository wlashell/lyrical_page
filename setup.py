import os

from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='lyrical_page',
    version='2.0.0p2',
    description='Website content system based on a mashup of ideas from the Django contrib flatpage appp, joomla!, and many years of systems development..',
    author='Will LaShell',
    author_email='wlashell@lyrical.net',
    license='Apache Software License',
    long_description=README,
    url='http://www.lyrical.net/projects/lyrical_page/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
