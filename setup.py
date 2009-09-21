from setuptools import find_packages, setup

setup(
    name='TracGitLocation',
    version='1.0',
    author='Andreas Zeidler',
    author_email='az@zitc.de',
    url='http://trac-hacks.org/wiki/GitLocationPlugin',
    classifiers = [
        'Framework :: Trac',
        'Development Status :: 4 - Production/Beta',
        'Environment :: Web Environment',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    description='Provide links to the actual URLs of Git-dwelling items',
    license='GPL',
    keywords='trac plugin git',
    packages=find_packages(exclude=['*.tests*']),
    install_requires=['Trac>=0.11', 'Genshi>=0.5'],
    entry_points = {'trac.plugins': ['gitlocation = gitlocation']}
)
