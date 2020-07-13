from setuptools import setup
setup(name='fcreplay_record',
      version='0.1',
      description='Fcreplay_record python code',
      url='http://github.com/glisignoli/fcreplay_record',
      author='Gino Lisignoli',
      author_email='glisignoli@gmail.com',
      license='GPL3',
      packages=['fcreplay_record'],
      package_data={'fcreplay_record': [
          'data/*',
      ]},
      entry_points = {
          'console_scripts': [
              'fcreplay_record=fcreplay_record.record:console'
          ]
      },
      install_requires = [
          'pyscreenshot',
          'Pillow',
      ],
      zip_safe=False)