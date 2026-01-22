import requests

def get_certificates(domain):
    results = []
    try:
        url = f"https://crt.sh/?q={domain}&output=json"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            for entry in data[:10]:  # limit for demo
                results.append({
                    "issuer": entry.get("issuer_name"),
                    "common_name": entry.get("common_name"),
                    "entry_timestamp": entry.get("entry_timestamp")
                })
    except Exception as e:
        results.append({"error": str(e)})
    return results
