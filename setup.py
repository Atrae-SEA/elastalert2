# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup


base_dir = os.path.dirname(__file__)
setup(
    name='elastalert2',
    version='2.15.0',
    description='Automated rule-based alerting for Elasticsearch',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jertel/elastalert2",
    setup_requires='setuptools',
    license='Apache 2.0',
    project_urls={
        "Documentation": "https://elastalert2.readthedocs.io",
        "Source Code": "https://github.com/jertel/elastalert2",
        "Discussion Forum": "https://github.com/jertel/elastalert2/discussions",
    },
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': ['elastalert-create-index=elastalert.create_index:main',
                            'elastalert-test-rule=elastalert.test_rule:main',
                            'elastalert=elastalert.elastalert:main']},
    packages=find_packages(exclude=["tests"]),
    package_data={'elastalert': ['schema.yaml', 'es_mappings/**/*.json']},
    python_requires='>=3.9',
    install_requires=[
        'apscheduler>=3.10.4,<4.0',
        'aws-requests-auth>=0.4.3',
        'boto3>=1.29.6',
        'cffi>=1.16.0',
        'croniter>=2.0.1',
        'elasticsearch==7.10.1',
        'envparse>=0.2.0',
        'exotel==0.1.5',
        'Jinja2>=3.1.2',
        'jira>=3.5.2',
        'jsonpointer>=2.4',
        'jsonschema>=4.20.0',
        'prettytable>=3.9.0',
        'prison>=0.2.1',
        'prometheus_client>=0.19.0',
        'python-dateutil>=2.8.2',
        'PyYAML>=6.0.1',
        'py-zabbix>=1.1.7',
        'requests>=2.31.0',
        'sortedcontainers>=2.4.0',
        'statsd-tags==3.2.1.post1',
        'stomp.py>=8.1.0',
        'tencentcloud-sdk-python>=3.0.1038',
        'texttable>=1.7.0',
        'twilio>=8.10.2',
        'tzlocal==2.1'
    ]
)
