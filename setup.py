from setuptools import find_packages
from setuptools import setup

try:
    with open('.version') as f:
        VERSION = f.readline().strip()
except IOError:
    VERSION = 'unknown'

setup(
    name='create',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    url='https://www.ocf.berkeley.edu/',
    author='Open Computing Facility',
    author_email='help@ocf.berkeley.edu',
    install_requires=[
        # Celery 3.1.19 has a bug with Redis UNIX sockets that breaks create:
        # https://github.com/celery/celery/issues/2903
        'celery[redis]<3.1.18',
        'irc',
        'ocflib',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': {
            'create-worker = create.worker:main',
            'create-ircbot = create.ircbot:main',
            'approve = create.approve:main',
        },
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
