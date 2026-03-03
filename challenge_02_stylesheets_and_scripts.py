
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="styles.css">
    <title>My Page</title>
</head>
<body>
    <h1>Hello</h1>
    <script src="app.js"></script>
</body>
</html>
"""

# 👇 WRITE IT HERE
stylesheet = "main.min.css"
script_file = "bundle.js"

css_start = html.find("styles.css")
if css_start == -1:
    raise ValueError("styles.css not found")
css_end = css_start + len("styles.css")

html = (
    html[:css_start] +
    stylesheet +
    html[css_end:]
)

js_start = html.find("app.js")
if js_start == -1:
    raise ValueError("app.js not found")
js_end = js_start + len("app.js")

html = (
    html[:js_start] +
    script_file +
    html[js_end:]
)

print(html)