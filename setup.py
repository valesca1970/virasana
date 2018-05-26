from setuptools import find_packages, setup

setup(
    name='virasana',
    description='AJNA_MOD Visao computacional e Aprendizado de Maquina na Vigilancia Aduaneira',
    version='0.0.1',
    url='https://github.com/IvanBrasilico/virasana',
    license='GPL',
    author='Ivan Brasilico',
    author_email='brasilico.ivan@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Celery',
        'defusedxml',
        'Flask',
        'Flask-BootStrap',
        'Flask-Login',
        'Flask-cors',
        'Flask-nav',
        'Flask-session',
        'Flask-wtf',
        'matplotlib',
        'pymongo',
        'pandas',
        'pillow',
        'raven',
        'redis',
        'requests'
    ],
    dependency_links=[
        'git+https://github.com/IvanBrasilico/ajna_commons.git#egg=ajna_commons-0.0.1'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite="tests",
    package_data={
    },
    extras_require={
        'dev': [
            'alembic',
            'autopep8',
            'bandit',
            'coverage',
            'flake8',
            'flake8-quotes',
            'flake8-docstrings',
            'flake8-todo',
            'flask-webtest',
            'isort',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'pytest-mock',
            'radon',
            'testfixtures',
            'tox'
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.6',
    ],
)
