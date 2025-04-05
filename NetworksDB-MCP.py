from fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("networksdb")

NETWORKSDB_ENDPOINT = 'https://networksdb.io'
api_key = os.getenv("NETWORKSDB_API_KEY")
if not api_key:
    raise ValueError("NETWORKSDB_API_KEY environment variable is required")

def make_request(path: str, params: dict = {}):
    try:
        response = requests.post(
            f'{NETWORKSDB_ENDPOINT}{path}', 
            headers={'X-Api-Key': api_key}, 
            data=params,
            timeout=30.0
        )
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        return {"error": "Request timed out"}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def key_info():
    """Get information about your NetworksDB API key and usage statistics."""
    return make_request('/api/key')

@mcp.tool()
def ip_info(ip: str = None):
    """Get information about an IP address."""
    return make_request('/api/ip-info', {'ip': ip} if ip else {})

@mcp.tool()
def ip_geo(ip: str = None):
    """Get geolocation information for an IP address."""
    return make_request('/api/ip-geo', {'ip': ip} if ip else {})

@mcp.tool()
def org_search(query: str):
    """Search for organizations by name."""
    return make_request('/api/org-search', {'search': query})

@mcp.tool()
def org_info(id: str):
    """Get information about an organization."""
    return make_request('/api/org-info', {'id': id})

@mcp.tool()
def org_networks(id: str, ipv6: bool = False):
    """Get networks belonging to an organization."""
    params = {'id': id}
    if ipv6:
        params['ipv6'] = True
    return make_request('/api/org-networks', params)

@mcp.tool()
def asn_info(asn: str):
    """Get information about an ASN."""
    return make_request('/api/asn-info', {'asn': asn})

@mcp.tool()
def asn_networks(asn: str, ipv6: bool = False):
    """Get networks belonging to an ASN."""
    params = {'asn': asn}
    if ipv6:
        params['ipv6'] = True
    return make_request('/api/asn-networks', params)

@mcp.tool()
def dns(domain: str):
    """Get DNS records for a domain."""
    return make_request('/api/dns', {'domain': domain})

@mcp.tool()
def reverse_dns(ip: str):
    """Get reverse DNS records for an IP address."""
    return make_request('/api/reverse-dns', {'ip': ip})

@mcp.tool()
def mass_reverse_dns(start: str, end: str = None):
    """Get reverse DNS records for a range of IP addresses or CIDR."""
    if end:
        params = {'ip_start': start, 'ip_end': end}
    else:
        params = {'cidr': start}
    return make_request('/api/mass-reverse-dns', params)

if __name__ == "__main__":
    mcp.run(transport="stdio") 