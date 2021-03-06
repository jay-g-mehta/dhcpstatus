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
 6. MAC address of the host the IP is leased
 7. Hostname of the machine DHCP IP is leased to


Usage **dhcpstatus** command : **dhcpstatus_subnet**
------------------------------------------------------

**dhcpstatus** installation also comes with command style entry point **dhcpstatus_subnet**. You can run **dhcpstatus**
in standalone cli mode using binary **dhcpstatus_subnet**:

.. code:: bash

   $ dhcpstatus_subnet /path/to/dhcp_subnet.conf /path/to/dhcpd.lease

    Subnet               | Netmask              | Low Address          | High Address         | IPs defined     | IPs free        | IPs in use      | IPs                  | MACs                 | Hostname
    10.30.217.0          | 255.255.255.192      | 10.30.217.4          | 10.30.217.62         |              59 |              53 |               6 | 10.30.217.39         | 9c:b6:54:aa:78:c3    | host1
                         |                      |                      |                      |                 |                 |                 | 10.30.217.5          | 9c:b6:54:aa:88:9f    | host2
                         |                      |                      |                      |                 |                 |                 | 10.30.217.21         | 9c:b6:54:aa:8b:07    | host3
                         |                      |                      |                      |                 |                 |                 | 10.30.217.18         | 9c:b6:54:ab:b9:eb    | host4
                         |                      |                      |                      |                 |                 |                 | 10.30.217.56         | 9c:b6:54:ab:bb:2f    | host5
                         |                      |                      |                      |                 |                 |                 | 10.30.217.37         | 9c:b6:54:ab:bb:9b    | host6
    10.30.217.64         | 255.255.255.192      | 10.30.217.68         | 10.30.217.126        |              59 |              53 |               6 | 10.30.217.86         | 9c:b6:54:aa:8f:7b    | host7
                         |                      |                      |                      |                 |                 |                 | 10.30.217.100        | 9c:b6:54:73:60:41    | host8
                         |                      |                      |                      |                 |                 |                 | 10.30.217.83         | 9c:b6:54:aa:8b:93    | host9
                         |                      |                      |                      |                 |                 |                 | 10.30.217.114        | 9c:b6:54:aa:8b:0f    | host10
                         |                      |                      |                      |                 |                 |                 | 10.30.217.101        | 9c:b6:54:aa:8e:bf    | host11
                         |                      |                      |                      |                 |                 |                 | 10.30.217.117        | 9c:b6:54:aa:8b:03    | host12
    10.30.241.160        | 255.255.255.248      | 10.30.241.164        | 10.30.241.166        |               3 |               3 |               0 | -                    | -                    | -
    10.30.221.64         | 255.255.255.192      | 10.30.221.68         | 10.30.221.126        |              59 |              54 |               5 | 10.30.221.99         | 70:10:6f:ca:94:74    | host13
                         |                      |                      |                      |                 |                 |                 | 10.30.221.78         | 70:10:6f:ca:90:2c    | host14
                         |                      |                      |                      |                 |                 |                 | 10.30.221.77         | 70:10:6f:ca:8f:2c    | host15
                         |                      |                      |                      |                 |                 |                 | 10.30.221.85         | 70:10:6f:ca:7d:f4    | host16
                         |                      |                      |                      |                 |                 |                 | 10.30.221.69         | 70:10:6f:ca:83:fc    | host17
    10.30.220.0          | 255.255.255.192      | 10.30.220.4          | 10.30.220.62         |              59 |              58 |               1 | 10.30.220.33         | 34:17:eb:e8:06:25    | host18


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

    {('10.30.217.4', '10.30.217.62'): {'netmask': '255.255.255.192',
                                       'option': {'broadcast-address': '10.30.217.63',
                                                  'domain-name': '"con.dcg02.paypalc3.net"',
                                                  'domain-name-servers': '10.190.18.19,10.190.18.20',
                                                  'routers': '10.30.217.1'},
                                       'pool': {'failover': ('peer',
                                                             '"phx04-dhcp-failover"'),
                                                'range': ('10.30.217.4',
                                                          '10.30.217.62')},
                                       'status': {'Hostname': ['host1',
                                                               'host2',
                                                               'host3',
                                                               'host4',
                                                               'host5',
                                                               'host6'],
                                                  'IPs': ['10.30.217.39',
                                                          '10.30.217.5',
                                                          '10.30.217.21',
                                                          '10.30.217.18',
                                                          '10.30.217.56',
                                                          '10.30.217.37'],
                                                  'IPs defined': 59,
                                                  'IPs free': 53,
                                                  'IPs in use': 6,
                                                  'MACs': ['9c:b6:54:aa:78:c3',
                                                           '9c:b6:54:aa:88:9f',
                                                           '9c:b6:54:aa:8b:07',
                                                           '9c:b6:54:ab:b9:eb',
                                                           '9c:b6:54:ab:bb:2f',
                                                           '9c:b6:54:ab:bb:9b']},
                                       'subnet': '10.30.217.0'},
    ('10.30.217.68', '10.30.217.126'): { 'netmask': '255.255.255.192',
                                         'option': {'broadcast-address': '10.30.217.127',
                                                    'domain-name': '"con.dcg02.paypalc3.net"',
                                                    'domain-name-servers': '10.190.18.19,10.190.18.20',
                                                    'routers': '10.30.217.65'},
                                         'pool': {'failover': ('peer',
                                                               '"phx04-dhcp-failover"'),
                                                  'range': ('10.30.217.68',
                                                            '10.30.217.126')},
                                         'status': {'Hostname': ['host13',
                                                                 'host14',
                                                                 'host15',
                                                                 'host16',
                                                                 'host17',
                                                                 'host18'],
                                                    'IPs': ['10.30.217.86',
                                                            '10.30.217.100',
                                                            '10.30.217.83',
                                                            '10.30.217.114',
                                                            '10.30.217.101',
                                                            '10.30.217.117',],
                                                    'IPs defined': 59,
                                                    'IPs free': 53,
                                                    'IPs in use': 6,
                                                    'MACs': ['9c:b6:54:aa:8f:7b',
                                                             '9c:b6:54:73:60:41',
                                                             '9c:b6:54:aa:8b:93',
                                                             '9c:b6:54:aa:8b:0f',
                                                             '9c:b6:54:aa:8e:bf',
                                                             '9c:b6:54:aa:8b:03']},
                                         'subnet': '10.30.217.64'},
    ('10.30.241.164', '10.30.241.166'): {'netmask': '255.255.255.248',
                                          'option': {'broadcast-address': '10.30.241.167',
                                                     'domain-name': '"con.dcg02.paypalc3.net"',
                                                     'domain-name-servers': '10.190.18.19,10.190.18.20',
                                                     'routers': '10.30.241.161'},
                                          'pool': {'failover': ('peer',
                                                                '"phx04-dhcp-failover"'),
                                                   'range': ('10.30.241.164',
                                                             '10.30.241.166')},
                                          'status': {'Hostname': [],
                                                     'IPs': [],
                                                     'IPs defined': 3,
                                                     'IPs free': 3,
                                                     'IPs in use': 0,
                                                     'MACs': []},
                                          'subnet': '10.30.241.160'}}


Installing **dhcpstatus**
----------------------------

.. code:: bash

    $ pip install dhcpstatus
