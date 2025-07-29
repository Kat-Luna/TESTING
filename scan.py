from flask import Blueprint, render_template

scan_bp = Blueprint('scan', __name__, url_prefix='/scan')

@scan_bp.route('/')
def scan():
    return render_template('scan.html')
