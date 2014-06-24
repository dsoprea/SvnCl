import setuptools
import os.path

import svncl

app_path = os.path.dirname(svncl.__file__)

with open(os.path.join(app_path, 'resources', 'README.md')) as f:
      long_description = f.read()

with open(os.path.join(app_path, 'resources', 'requirements.txt')) as f:
      install_requires = map(lambda s: s.strip(), f)

setuptools.setup(
      name='restpipe',
      version=svncl.__version__,
      description="Generate changelog text between HEAD and the last tag.",
      long_description=long_description,
      classifiers=[],
      keywords='subversion svn changelog',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='',
      license='GPL 2',
      packages=setuptools.find_packages(exclude=['dev']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      package_data={
          'svncl': ['resources/README.md',
                    'resources/requirements.txt',
                    'resources/scripts/*'],
      },
      scripts=[
          'svncl/resources/scripts/svncl',
      ],
)