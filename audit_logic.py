import requests

def run_scan(url):
    """Simulate a vulnerability scan. You can later integrate real scanners here."""
    findings = []

    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        headers = response.headers

        if "Server" in headers:
            server = headers["Server"].lower()
            if "apache" in server or "nginx" in server:
                findings.append("Server info exposed in headers.")

        if "X-Powered-By" in headers:
            findings.append("X-Powered-By header reveals technologies used.")

        if status_code >= 400:
            findings.append(f"Site returned error code: {status_code}")

    except Exception as e:
        findings.append(f"Scan failed: {str(e)}")

    return findings
