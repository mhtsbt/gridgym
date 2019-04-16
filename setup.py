from setuptools import setup

setup(name='gridgym',
      version='0.1',
      description='OpenAI gym environments for tabular RL',
      url='http://github.com/mhtsbt/gridgym',
      author='Matthias Hutsebaut',
      license='MIT',
      install_requires=['gym'],
      packages=['gridgym', 'gridgym.envs'],
      zip_safe=False)
