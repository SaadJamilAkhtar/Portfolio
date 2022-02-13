# regx for getting assets urls
"assets/([A-Z a-z 0-9 / . -]*)"
/images
# regx for changing it to static
"{% static 'assets/$1' %}"
/imgs

# Variables for template
1. page_title
2. site_title

# Blocks in template
1. body
2. script
3. style
4. dashboard [ for activating link]
5. services

# Page specific variables
## form.html
1. link
2. link_text