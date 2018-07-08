from setuptools import setup, find_packages


setup(
    name="cacheit-srv",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.2.1',
        'json-rpc==1.11.0',
    ],
    author="Dmitry Kolyagin",
    author_email="dmitry.kolyagin@gmail.com",
    scripts=['cacheit-srv.py'],
)
