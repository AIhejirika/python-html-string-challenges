# STEP 1: Base HTML template (MUST be first)
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Page</title>
</head>
<body>
    <h1>Welcome</h1>
</body>
</html>
"""

# STEP 2: Variables
page_title = "My Awesome Portfolio"
page_lang = "fr"

# STEP 3: Replace title (with count)
updated_html = html_template.replace(
    "<title>My Page</title>",
    f"<title>{page_title}</title>",
    1
)

# STEP 4: Replace lang attribute (with count)
updated_html = updated_html.replace(
    'lang="en"',
    f'lang="{page_lang}"',
    1
)

# STEP 5: Print result
print(updated_html)