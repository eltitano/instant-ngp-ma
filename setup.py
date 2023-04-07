from setuptools import setup, find_packages
import os

# Get all .so files in build folder
#build_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'build'))
#print(build_folder)
#lib_files = [os.path.join('build', f) for f in os.listdir(build_folder) if f.endswith('.so')]
#print(lib_files)

setup(name='instant_ngp',
      version='1.0.0',
      url='https://github.com/NVlabs/instant-ngp',
      author='Thomas Mueller and Alex Evans and Christoph Schied and Alexander Keller',
      packages=find_packages(),
      #entry_points={
      #    'console_scripts': [
      #        'instant_ngp=instant_ngp.scripts.run:main'
      #    ]
      #},
	  package_data={'instant_ngp': ['build/*.so'],'':['*.txt']},
      install_requires=["setuptools"],
      #long_description=long_description,
      long_description_content_type='text/markdown'
      )
