from setuptools import setup, find_packages

setup(name='instant_ngp',
      version='1.0.0',
      url='https://github.com/NVlabs/instant-ngp',
      author='Thomas Mueller and Alex Evans and Christoph Schied and Alexander Keller',
      packages=find_packages('./instant_ngp'),
      package_dir={'': './instant_ngp'},
      #entry_points={
      #    'console_scripts': [
      #        'instant_ngp=instant_ngp.scripts.run:main'
      #    ]
      #},
      #include_package_data=True,
      # package_data={
      #    'instant_ngp': ['instant_ngp/build/*.so', 'instant_ngp/build/*.pdy']
      # },
      install_requires=["setuptools"],
      #long_description=long_description,
      long_description_content_type='text/markdown'
      )
