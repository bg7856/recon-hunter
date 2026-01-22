import argparse
import json
import os
from modules import crawler, secret_scanner, shodan_api, crtsh_api

def main():
    parser = argparse.ArgumentParser(description="Recon Hunter - Automated Recon & Secret Hunter")
    parser.add_argument("target", help="Target domain")
    args = parser.parse_args()

    print(f"[+] Starting recon on {args.target}")

    subs = crawler.find_subdomains(args.target)
    print(f"[+] Found {len(subs)} subdomains")

    secrets = secret_scanner.scan_domain(args.target)
    print(f"[+] Found {len(secrets)} potential secrets")

    shodan_results = shodan_api.search_host(args.target)
    print(f"[+] Shodan results: {len(shodan_results)} entries")

    crt_results = crtsh_api.get_certificates(args.target)
    print(f"[+] crt.sh results: {len(crt_results)} certificates")

    report = {
        "target": args.target,
        "subdomains": subs,
        "secrets": secrets,
        "shodan": shodan_results,
        "crtsh": crt_results
    }

    os.makedirs("output", exist_ok=True)
    with open("output/report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("[+] Report saved to output/report.json")

if __name__ == "__main__":
    main()
