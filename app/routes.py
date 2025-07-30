from flask import render_template, request
from signals.signal_engine import get_signals

def configure_routes(app):
    @app.route('/')
    def index():
        signals = get_signals()
        return render_template('index.html', signals=signals)