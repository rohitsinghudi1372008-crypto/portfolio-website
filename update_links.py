with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_link = '<a href="#" class="project-link">View Project →</a>'
new_link = '<a href="https://github.com/rohitsinghudi1372008-crypto/academic-html-projects" target="_blank" class="project-link">View GitHub →</a>'

html = html.replace(old_link, new_link)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
