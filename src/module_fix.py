import subprocess, sys

subprocess.call([
    sys.executable,
    "-m", "pip",
    "install", "--user",
    " cherrypy"])

# Mako
# CherryPy