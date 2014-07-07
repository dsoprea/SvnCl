import setuptools
import os.path

import svncl

app_path = os.path.dirname(svncl.__file__)

with open(os.path.join(app_path, 'resources', 'README.rst')) as f:
      long_description = f.read()

with open(os.path.join(app_path, 'resources', 'requirements.txt')) as f:
      install_requires = list(map(lambda s: s.strip(), f.readlines()))

setuptools.setup(
      name='svncl',
      version=svncl.__version__,
      description="Generate changelog text for Subversion commits since the last tag.",
      long_description=long_description,
      classifiers=[],
      keywords='subversion svn changelog',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/SvnCl',
      license='GPL 2',
      packages=setuptools.find_packages(exclude=['dev']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      package_data={
          'svncl': ['resources/README.rst',
                    'resources/requirements.txt',
                    'resources/scripts/*'],
      },
      scripts=[
          'svncl/resources/scripts/svncl',
      ],
)
