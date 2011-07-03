from setuptools import setup, find_packages

setup(
    name='lyrical_page',
    version='1.1.0',
    description='A jazzy skin for the Django Admin-Interface.',
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
