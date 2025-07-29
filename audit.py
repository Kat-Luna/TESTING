# models/audit.py

from . import db
import requests

class AuditResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    findings = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<AuditResult {self.url}>"

def run_scan(url):
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
