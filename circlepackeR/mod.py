import bs4

file = 'test.html'
with open(file) as f:
    txt = f.read()
    soup = bs4.BeautifulSoup(txt)
    html_txt = str(soup)
    html_txt = html_txt.replace('pointer-events: none', 'pointer-events: all')
    html_txt = html_txt.replace('.on("click", function(d) { if (focus !== d) zoom(d), d3.event.stopPropagation(); });',
                '.on("click", function(d) { if (d3.select(this).classed("node--leaf")) {window.open("https://www.google.com/search?q=" + d.name);} else{if (focus !== d) zoom(d), d3.event.stopPropagation(); }});')    

with open("modified.html", "w") as f:    
    f.write(html_txt)