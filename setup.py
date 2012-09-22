from setuptools import setup, find_packages

setup(
    name='lyrical_page',
    version='1.6.0',
    description='Website content system based on a mashup of ideas from the Django contrib flatpage appp, joomla!, and many years of systems development..',
    author='Will LaShell',
    author_email='wlashell@lyrical.net',
    url='http://www.lyrical.net/projects/lyrical_page/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
