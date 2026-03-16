import markdown

# Read markdown file
with open("input.md", "r") as file:
    markdown_text = file.read()

# Convert markdown to HTML
html_output = markdown.markdown(markdown_text)

# Load HTML template
with open("template.html", "r") as file:
    template = file.read()

# Insert converted HTML into template
final_html = template.replace("{{content}}", html_output)

# Save final output
with open("output.html", "w") as file:
    file.write(final_html)

print("Styled HTML page generated!")