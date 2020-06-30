import setuptools

setuptools.setup(
    name='rstvalidator',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
