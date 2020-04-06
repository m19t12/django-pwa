from setuptools import setup, find_packages

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name='django-progressive',
    version='1.0.4',
    packages=['django_pwa', 'django_pwa.static.django_pwa', 'django_pwa.templates', 'django_pwa.templatetags'],
    package_data={"django_pwa.templates": ["*"],
                  "django_pwa.static.django_pwa": ["*"]},
    license='GPL License',
    description='Library for adding progressive web app functionality in your django project.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/m19t12/django-pwa',
    author='Manolis Tsoukalas',
    author_email='emmtsoukalas@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
