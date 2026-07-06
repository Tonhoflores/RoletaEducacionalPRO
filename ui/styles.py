# ==========================================
# CORES
# ==========================================

BACKGROUND = "#16213E"
PANEL = "#1F4068"

BUTTON = "#00A8E8"
BUTTON_HOVER = "#0096D6"

TEXT = "#FFFFFF"

APP_STYLE = f"""
QWidget {{
    background-color: {BACKGROUND};
    color: {TEXT};
    font-family: "Segoe UI";
    font-size: 11pt;
}}

QFrame {{
    background-color: {PANEL};
    border-radius: 12px;
}}

QPushButton {{
    background-color: {BUTTON};
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px;
    font-size: 14px;
    font-weight: bold;
}}

QPushButton:hover {{
    background-color: {BUTTON_HOVER};
}}

QLabel {{
    color: white;
}}
"""