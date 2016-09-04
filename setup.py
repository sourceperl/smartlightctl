from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    license='MIT',
    url='https://github.com/sourceperl/smartlightctl',
    platforms='any',
    install_requires=required,
    py_modules=[
        'pySmartLightSmlC9'
    ],
    scripts=[
        'scripts/smartlightctl',
        'scripts/smartlightscan'
    ]
)
