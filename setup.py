from setuptools import setup, find_packages
from bootstrapform.meta import VERSION

setup(
    name='django-bootstrap-form',
    version=str(VERSION),
    description="django-bootstrap-form",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords='bootstrap,django',
    author='tzangms',
    author_email='tzangms@gmail.com',
    url='http://github.com/tzangms/django-bootstrap-form',
    license='MIT',
    test_suite='runtests.runtests',
    install_requires=[
        "django>=2.2",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
