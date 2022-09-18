from setuptools import setup, find_namespace_packages

setup(name='clean_folder2',
      version='2.0',
      description='Very useful code',
      url='https://github.com/NickGoit/Scripts',
      author='NickG',
      author_email='my.gryshyn@gmail.com',
      license='Free',
      packages=['clean_folder2'],
      entry_points={'console_scripts': ['clean-folder2=clean_folder2.clean2:main']}
)