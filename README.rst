==============
dhcpstatus
==============

**dhcpstatus** is a pure python implementation of DHCPSTATUS (http://dhcpstatus.sourceforge.net/),
implementing most of its functionalities.

With subnet status operation, **dhcpstatus** will return IP details for each subnet. It will provide:
 1. IP range defined for the subnet
 2. Total number of IPs defined for use
 3. Count of free IPs in the subnet
 4. Count of used IPs in the subnet
 5. IPs leased out from each subnet


Usage **dhcpstatus** command : **dhcpstatus_subnet**)
------------------------------------------------------

**dhcpstatus** installation also comes with command style entry point **dhcpstatus_subnet**. You can run **dhcpstatus**
in standalone cli mode using binary **dhcpstatus_subnet**:

.. code:: bash

   $ dhcpstatus_subnet /path/to/dhcp_subnet.conf /path/to/dhcpd.lease

    Subnet               | Netmask              | IPs defined     | IPs in use      | IPs free
    10.24.250.64         | 255.255.255.192      |              59 |              10 | 49
    10.57.48.64          | 255.255.255.192      |              59 |               0 | 59
    10.198.139.128       | 255.255.255.128      |             123 |               0 | 123
    10.198.146.0         | 255.255.255.192      |              59 |               5 | 54
    10.198.157.128       | 255.255.255.192      |              59 |               7 | 52
    10.197.247.0         | 255.255.255.128      |             123 |              10 | 113
    10.198.147.128       | 255.255.255.192      |              59 |               0 | 59


**dhcpstatus** API usage
-------------------------

.. code:: python

    from dhcpstatus import *
    import pprint

    d=DHCPStatus('/path/to/dhcp_subnet.conf ', ' /path/to/dhcpd.lease')
    status = d.subnet_status()

    pprint.pprint(status)


OR

.. code:: python

    import dhcpstatus
    import pprint

    d=dhcpstatus.DHCPStatus('/path/to/dhcp_subnet.conf ', ' /path/to/dhcpd.lease')
    status = d.subnet_status()

    pprint.pprint(status)


And you can see output as:

.. code:: bash

    {('10.25.249.132', '10.25.249.190'): {'netmask': '255.255.255.192',
                                          'options': {'broadcast-address': '10.25.249.191',
                                                      'domain-name': '"some.domain.net"',
                                                      'domain-name-servers': '10.24.199.136,10.24.199.137',
                                                      'routers': '10.25.249.129'},
                                          'pool': {'failover': ('peer',
                                                                '"dhcp-failover"'),
                                                   'range': ('10.25.249.132',
                                                             '10.25.249.190')},
                                          'status': {'IPs': ['10.25.249.157',
                                                             '10.25.249.169',
                                                             '10.25.249.168',
                                                             '10.25.249.167',
                                                             '10.25.249.161',
                                                             '10.25.249.181',
                                                             '10.25.249.155',
                                                             '10.25.249.139',
                                                             '10.25.249.158',
                                                             '10.25.249.163',
                                                             '10.25.249.154',
                                                             '10.25.249.152',
                                                             '10.25.249.141',
                                                             '10.25.249.156',
                                                             '10.25.249.165',
                                                             '10.25.249.173',
                                                             '10.25.249.151',
                                                             '10.25.249.160',
                                                             '10.25.249.153',
                                                             '10.25.249.176',
                                                             '10.25.249.178',
                                                             '10.25.249.146',
                                                             '10.25.249.149',
                                                             '10.25.249.182',
                                                             '10.25.249.159',
                                                             '10.25.249.180',
                                                             '10.25.249.136',
                                                             '10.25.249.171',
                                                             '10.25.249.148',
                                                             '10.25.249.143',
                                                             '10.25.249.145'],
                                                     'IPs defined': 59,
                                                     'IPs free': 28,
                                                     'IPs in use': 31},
                                          'subnet': '10.25.249.128'},
     ('10.25.249.196', '10.25.249.254'): {'netmask': '255.255.255.192',
                                          'options': {'broadcast-address': '10.25.249.255',
                                                      'domain-name': '"some.domain.net"',
                                                      'domain-name-servers': '10.24.199.136,10.24.199.137',
                                                      'routers': '10.25.249.193'},
                                          'pool': {'failover': ('peer',
                                                                '"dhcp-failover"'),
                                                   'range': ('10.25.249.196',
                                                             '10.25.249.254')},
                                          'status': {'IPs': ['10.25.249.213',
                                                             '10.25.249.222',
                                                             '10.25.249.239',
                                                             '10.25.249.211',
                                                             '10.25.249.236',
                                                             '10.25.249.214',
                                                             '10.25.249.208',
                                                             '10.25.249.202',
                                                             '10.25.249.219',
                                                             '10.25.249.209',
                                                             '10.25.249.228',
                                                             '10.25.249.207',
                                                             '10.25.249.218',
                                                             '10.25.249.238',
                                                             '10.25.249.217',
                                                             '10.25.249.229',
                                                             '10.25.249.206',
                                                             '10.25.249.230',
                                                             '10.25.249.244',
                                                             '10.25.249.237',
                                                             '10.25.249.242',
                                                             '10.25.249.243',
                                                             '10.25.249.234',
                                                             '10.25.249.203',
                                                             '10.25.249.240',
                                                             '10.25.249.221',
                                                             '10.25.249.215',
                                                             '10.25.249.233',
                                                             '10.25.249.226'],
                                                     'IPs defined': 59,
                                                     'IPs free': 30,
                                                     'IPs in use': 29},
                                          'subnet': '10.25.249.192'}}


Installing **dhcpstatus**
----------------------------

.. code:: bash

    $ pip install dhcpstatus -r requirements.txt
