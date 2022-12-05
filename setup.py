from setuptools import find_packages, setup

setup(
    name='fraser_gehrig',
    packages=find_packages(include=['fraser_gehrig']),
    version='0.1.0',
    description='',
    author='Gabriel Dennis, Harry Goodman',
    license='MIT',
    install_requires=["pandas", "bs4", "requests", "numpy"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
