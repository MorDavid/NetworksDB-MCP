# NetworksDB-MCP

## Model Context Protocol (MCP) Server for NetworksDB

NetworksDB-MCP is a powerful integration that brings the capabilities of Model Context Protocol (MCP) Server to NetworksDB, enabling natural language queries for network intelligence, IP geolocation, organization details, and DNS information.

> 🌐 **Seamless Network Intelligence with AI!**  
> Query network data, track organizations, and analyze IP infrastructure using natural language.

## 🔍 What is NetworksDB-MCP?

NetworksDB-MCP combines the power of:

* **NetworksDB**: Comprehensive database for IP, organization, and network intelligence
* **Model Context Protocol (MCP)**: An open protocol for creating custom AI tools
* **Natural Language Processing**: Convert plain English queries into NetworksDB API calls

## ✨ Features

* **Natural Language Interface**: Query network data using plain English
* **Comprehensive Analysis Categories**:
  * 🔑 API Key management and usage tracking
  * 🌐 IP address information and geolocation
  * 🏢 Organization search and infrastructure mapping
  * 🔢 ASN information and network relationships
  * 📝 DNS and reverse DNS intelligence
  * 🔍 Mass reverse DNS for network ranges

## 📋 Prerequisites

* NetworksDB API key
* Python 3.8 or higher
* MCP Client

## 🔧 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/mordavid/NetworksDB-MCP.git
    cd NetworksDB-MCP
    ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the MCP Server
    ```bash
    "mcpServers": {
        "NetworksDB-MCP": {
            "command": "python",
            "args": [
                "<Your_Path>\\NetworksDB-MCP.py"
            ],
            "env": {
                "NETWORKSDB_API_KEY": "<Your_API_Key>"
            }
        }
    }
   ```

## 🚀 Usage

Example queries you can ask through the MCP:

* "Find all information about IP 8.8.8.8"
* "Search for organizations named Google"
* "Get geolocation for IP 1.1.1.1"
* "Show me DNS records for example.com"
* "Find all networks owned by Microsoft"
* "Get reverse DNS for IP range 192.168.1.0/24"

Core commands:
- `key_info` - Get API key info and usage stats
- `ip_info` - Get IP address details
- `ip_geo` - Get IP geolocation
- `org_search` - Search organizations
- `org_info` - Get org details
- `org_networks` - List networks owned by org
- `asn_info` - Get ASN information
- `asn_networks` - List networks for ASN
- `dns` - Get DNS records
- `reverse_dns` - Get reverse DNS for IP
- `mass_reverse_dns` - Bulk reverse DNS lookup

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

* The NetworksDB team for providing comprehensive network intelligence APIs
* The MCP community for advancing AI-powered tooling

---

_Note: This is not an official NetworksDB product. NetworksDB-MCP is a community-driven integration between NetworksDB and MCP._
