from setuptools import setup, find_packages
import os

version = '1.0b1'


setup(name='zeam.form.plone',
      version=version,
      description="Plone integration for Zeam Form",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),

      classifiers=[
        "Framework :: Zope2",
        "Framework :: Plone",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='grok form framework plone',
      author='Sylvain Viollon',
      author_email='thefunny@gmail.com',
      url='http://pypi.python.org/pypi/zeam.form.plone',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['zeam', 'zeam.form'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Products.statusmessages',
          'five.grok',
          'martian',
          'megrok.pagetemplate',
          'setuptools',
          'zeam.form.base',
          'zeam.form.ztk',
          'zope.i18n',
          'zope.i18nmessageid',
          'zope.interface',
          ],
      )
