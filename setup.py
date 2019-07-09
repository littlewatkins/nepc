from setuptools import setup
from nepc.util import config

HOME = config.userHome()

setup(

    name='nepc',

    version='0.1',

    description='Access and explore the NEPC database.',
    long_description=('Access and explore the NRL Evaluated Plasma ' +
                      'Chemistry database.'),

    authors='Paul Adamson, Darr...',
    author_email='paul.adamson@nrl.navy.mil, ...',

    license='',

    packages=['nepc.util', 'nepc.methods'],

    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]

)
