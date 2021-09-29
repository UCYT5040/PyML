import pyml
index = pyml.Page("Index")
title = pyml.CustomCompenent("<h1>Hello</h1>")
index.add_component(title)
index.set_style("h1 { color: blue; }")
print(index.generate_raw_html())