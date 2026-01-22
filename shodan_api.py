import shodan

API_KEY = "YOUR_SHODAN_API_KEY"  # Replace with your key

def search_host(domain):
    results = []
    try:
        api = shodan.Shodan(API_KEY)
        host = api.search(domain)
        for match in host['matches']:
            results.append({
                "ip": match.get("ip_str"),
                "port": match.get("port"),
                "data": match.get("data")[:100]  # snippet
            })
    except Exception as e:
        results.append({"error": str(e)})
    return results
