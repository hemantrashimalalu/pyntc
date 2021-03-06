from setuptools import find_packages, setup
import sys

name = 'pyntc'
version = '0.0.7'
packages = find_packages()
package_data = {'pyntc': ['templates/*.template', 'devices/tables/jnpr/*.yml']}

install_requires = [
    'requests>=2.7.0',
    'jsonschema',
    'future',
    'netmiko',
    'paramiko',
    'pynxos>=0.0.3',
    'coverage',
    'mock>=1.3',
    'textfsm',
    'terminal',
    'f5-sdk',
    'bigsuds',
]

dependency_links = []

author = 'Network To Code'
author_email = 'ntc@networktocode.com'
url = 'https://github.com/networktocode/pyntc'
download_url = 'https://github.com/networktocode/pyntc/tarball/0.0.6'
description = 'A multi-vendor library for managing network devices.'

if sys.version_info.major >= 3:
    install_requires.append('pyeapi==9.9.9')
    dependency_links.append(
        'https://github.com/arista-eosplus/pyeapi/tarball/develop#egg=pyeapi-9.9.9'
      )
else:
    install_requires.append('pyeapi')
    install_requires.append('junos-eznc')

setup(name=name,
      version=version,
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      dependency_links=dependency_links,
      url=url,
      download_url=download_url,
      author=author,
      author_email=author_email,
      description=description,
)
