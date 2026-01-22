import re
import requests

def scan_domain(domain):
    findings = []
    try:
        resp = requests.get(f"http://{domain}", timeout=5)
        if resp.status_code == 200:
            text = resp.text
            # Regex patterns for secrets
            patterns = {
                "AWS Key": r"AKIA[0-9A-Z]{16}",
                "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
                "JWT Token": r"eyJ[A-Za-z0-9_\-]+?\.[A-Za-z0-9_\-]+?\.[A-Za-z0-9_\-]+",
                "Generic Token": r"[A-Za-z0-9]{32,}"
            }
            for name, pat in patterns.items():
                matches = re.findall(pat, text)
                if matches:
                    findings.append({name: matches})
    except Exception as e:
        findings.append({"error": str(e)})
    return findings
