"""
app.py – Main entry point for the WebLog Analytics Dashboard.
Flattened structure for stable deployment.
"""

import os
import sys
import dash
import dash_bootstrap_components as dbc

# Import flattened components
from dash_layout import build_layout
from dash_callbacks import register_callbacks

# ─── App Initialisation ──────────────────────────────────────────────────────
# Create the Dash instance
dash_app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.CYBORG,
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css",
    ],
    suppress_callback_exceptions=True,
    eager_loading=True,
    title="AI Analytics",
    meta_tags=[
        {"name": "viewport",
         "content": "width=device-width, initial-scale=1"},
        {"name": "description",
         "content": "Interactive web server log analytics dashboard built with Dash."},
    ],
)

# ─── Layout & Callbacks ──────────────────────────────────────────────────────
dash_app.layout = build_layout()
register_callbacks(dash_app)

# ─── Gunicorn Deployment ─────────────────────────────────────────────────────
# Expose the Flask server for Gunicorn
# 'gunicorn app:app' will look for 'app' in this file
app = dash_app.server

# ─── Dev server ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    dash_app.run(debug=True, host="0.0.0.0", port=port)
