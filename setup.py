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
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    keywords='bootstrap,django',
    author='tzangms',
    author_email='tzangms@gmail.com',
    url='http://github.com/polyconseil/django-bootstrap-form',
    license='MIT',
    test_suite='runtests.runtests',
    install_requires = [
        "django>=1.5",
    ],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
)
