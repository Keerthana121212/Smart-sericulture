try:
    from flask import Flask, render_template, request
except Exception as e:
    raise RuntimeError("Flask is not installed or not available in the active environment; install it with 'pip install flask' and ensure the correct virtual environment is activated.") from e

from silk_worm import pred_silkworm_diseases
