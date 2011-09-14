from setuptools import setup, find_packages


setup(name='django-bootstrap-form',
    author='Matt Austin', author_email='mail@mattaustin.me.uk',
    url='https://github.com/MattAustin/django-bootstrap-form',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django'],
    )

