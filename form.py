import mechanize

br = mechanize.Browser()
br.open("http://new.showrss.info")

print br.title()
br.select_form(nr=0)
br["_token"] = 'Better Call Saul'
br.submit()

