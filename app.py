import sys
import os

# Ensure the project root directory is in sys.path
# This allows 'from dashboard.app import server' to work regardless of how the app is started.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    # Import the Flask server from the dashboard app
    from dashboard.app import server as app
except ImportError as e:
    # Fallback/Debug for deployment environments
    print(f"ImportError: {e}")
    print(f"Python Path: {sys.path}")
    print(f"Current Directory: {os.getcwd()}")
    print(f"Base Directory: {BASE_DIR}")
    if os.path.exists(os.path.join(BASE_DIR, "dashboard")):
        print("Dashboard directory found.")
        if os.path.exists(os.path.join(BASE_DIR, "dashboard", "__init__.py")):
            print("__init__.py found in dashboard.")
        else:
            print("__init__.py MISSING in dashboard.")
    else:
        print("Dashboard directory NOT found.")
    raise e

if __name__ == "__main__":
    # Import the Dash app instance for local running
    from dashboard.app import app as dash_app
    port = int(os.environ.get("PORT", 8050))
    dash_app.run(debug=True, host="0.0.0.0", port=port)

