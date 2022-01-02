from setuptools import setup, find_packages

setup(
    name='richterator',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['main'],
    install_requires=[
        'Click'
    ],
    entry_points={
        'console_scripts':[
            'richterator=main:cli',
        ]
    }        
)