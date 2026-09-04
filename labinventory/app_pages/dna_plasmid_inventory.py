import json
import os

import streamlit as st
import streamlit.components.v1 as components


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates", "cell_template.html")


try:
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        html_template = f.read()

    final_html = html_template.replace("Cell Line Inventory", "DNA Plasmid Inventory")
    final_html = final_html.replace(
        "ATCC cell lines ordered for the LNP delivery programs, grouped by project. Select a card for the full record.",
        "DNA plasmid inventory for the lab. Add plasmid records to the data source to populate this page.",
    )
    final_html = final_html.replace(
        "search name, catalog #, organism, tissue, feature...",
        "search plasmid name, backbone, resistance, catalog #...",
    )
    final_html = final_html.replace(
        "const DATA = {DATA_PLACEHOLDER};",
        f"const DATA = {json.dumps([])};",
    )
    final_html = final_html.replace("nothing matches that search", "No DNA plasmid records yet")

    components.html(final_html, height=1000, scrolling=False)
except Exception as e:
    st.error(f"An error occurred while loading the DNA plasmid inventory: {e}")
