import os
from distutils.core import setup

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == "":
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

package_dir = "hub"

packages = []
for dirpath, dirnames, filenames in os.walk(package_dir):
    # ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith("."):
            del dirnames[i]
    if "__init__.py" in filenames:
        packages.append(".".join(fullsplit(dirpath)))


setup(name='django-hub-apps',
    version='0.0.2',
    description='Django Hub Apps',
    #long_description = read('README.rst'),
    author='Sjoerd Arendsen',
    url='https://github.com/hub-nl/django-hub-apps',
    install_requires=('djutils', 'django-taggit', 'bleach', 'django-mptt', 'django-autoslug', 'south',),
    packages=packages)