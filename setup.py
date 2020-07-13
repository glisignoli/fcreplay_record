from setuptools import setup
setup(name='fcreplay-record',
      version='0.1',
      description='Fcreplay-record python code',
      url='http://github.com/glisignoli/fcreplay-record',
      author='Gino Lisignoli',
      author_email='glisignoli@gmail.com',
      license='GPL3',
      packages=['fcreplay-record'],
      entry_points = {
          'console_scripts': [
              'fcreplay-record=fcreplay-record.record:console',
          ]
      },
      install_requires = [
          'pyscreenshot',
          'Pillow',
      ],
      zip_safe=False)