import sys
import netaddr

from isc_dhcp_leases import Lease, IscDhcpLeases
from pydhcpdparser import parser


class DHCPDParser(object):
    def __init__(self, subnet_conf_path):
        with open(subnet_conf_path, 'r') as f:
            self.dhcpd_conf = parser.parse(f.read())

    def get_subnets(self):
        """Return only subnet details.
        Returns: {(low_addr, high_addr):{subnet_details}}
        """
        out = {}
        for conf in self.dhcpd_conf:
            if 'subnet' in conf:
                # This looks to be subnet block
                out[conf['pool']['range']] = conf
        return out


class DHCPDLease(object):
    def __init__(self, lease_file_path):
        self.leases = IscDhcpLeases(lease_file_path)


class DHCPStatus(object):
    """
    Class to return DHCP status:
    """
    def __init__(self, subnet_conf_path, dhcp_lease_path):
        self.dhcpd_parser = DHCPDParser(subnet_conf_path)
        self.dhcpd_lease = DHCPDLease(dhcp_lease_path)

    def subnet_status(self):
        """Returns subnet status with active IP lease information
        Subnet | Netmask | Low IP range | High IP range | Total IPs | IPs free | IPs in use | IPs | MACs
        """
        subnets = self.dhcpd_parser.get_subnets()
        for iprange in subnets:
            r = netaddr.IPRange(iprange[0], iprange[1])
            len_r = len(r)
            subnets[iprange]['status'] = {
                'IPs defined': len_r,
                'IPs in use': 0,
                'IPs free': len_r,
                'IPs': [],
                'MACs': []
            }

        active_leases = self.dhcpd_lease.leases.get_current()
        for mac, lease in active_leases.iteritems():
            for iprange in subnets:
                if lease.ip in netaddr.IPRange(iprange[0], iprange[1]):
                    subnets[iprange]['status']['IPs'].append(lease.ip)
                    subnets[iprange]['status']['MACs'].append(mac)
                    subnets[iprange]['status']['IPs in use'] = subnets[iprange]['status']['IPs in use'] + 1
                    subnets[iprange]['status']['IPs free'] = subnets[iprange]['status']['IPs free'] - 1

                    break

        return subnets


def main_subnet_status():
    """CLI way of invoking subnet status for DHCP"""
    status = DHCPStatus(sys.argv[1], sys.argv[2])
    subnet_states = status.subnet_status()
    print "{:20s} | {:20s} | {:20s} | {:20s} | {:15s} | {:15s} | {:15s} | {:20s} | {:20s}".format(
        "Subnet", "Netmask", "Low Address", "High Address",
        "IPs defined", "IPs free", "IPs in use", "IPs", "MACs")

    status_format = "{:20s} | {:20s} | {:20s} | {:20s} | {:15d} | {:15d} | {:15d} | {:20s} | {:20s}"
    for key, s in subnet_states.items():
        ip_list = s['status']['IPs']
        mac_list = s['status']['MACs']
        if ip_list == []:
            ip_list.append("-")
            mac_list.append("-")
        print status_format.format(
            s['subnet'], s['netmask'], s['pool']['range'][0], s['pool']['range'][1],
            s['status']['IPs defined'], s['status']['IPs free'], s['status']['IPs in use'],
            ip_list[0], mac_list[0]
        )

        for i in range(1, len(ip_list)):
            print "{:20s} | {:20s} | {:20s} | {:20s} | {:15s} | {:15s} | {:15s} | {:20s} | {:20s}".format(
                "", "", "", "", "", "", "", ip_list[i], mac_list[i])


if __name__ == "__main__":
    main_subnet_status()
