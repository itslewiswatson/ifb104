#----------------------------------------------------------------
#
# Image Scraper
#
# This is an extension of the "Image Finder" exercise, so you
# will need to have completed that one before beginning this.
#
# In the previous exercise you created a program that found
# and printed the URLs of images in Wikipedia pages.  Here
# you will extend that program so that it produces a whole new
# web page containing just the extracted images without the
# surrounding text.
#
# As per the steps below, you will follow the same process
# for finding images, but instead of printing the URLs
# you will create an HTML file that, when opened in a web
# browser, displays the images found.  The HTML code you
# generate should have a structure like the following:
#
# <!DOCTYPE html>
# <html>
#
#     <head>
#         <title>HELPFUL_TITLE</title>
#     </head>
# 
#     <body>
#         <img src="IMAGE_URL">
#         ... etc
#     </body>
#
# </html>
#


#-----
# Import the necessary URL and RE functions
from urllib.request import urlopen
from re import findall

#-----
# Here are some web pages to try, each of which is a Wikipedia
# page, so we can assume they have a fairly consistent structure.
# As well as large images, you will also discover the images for
# small icons, as well as single pixel meta-data images hidden in
# the page.  (Jack Benny's Wikipedia entry has lots of pictures,
# so is a good test.)
url1 = 'http://en.wikipedia.org/wiki/Jack_Benny'
url2 = 'http://en.wikipedia.org/wiki/QUT'
url3 = 'http://en.wikipedia.org/wiki/Flags'
url4 = 'http://en.wikipedia.org/wiki/Robby_the_Robot'
url5 = 'http://en.wikipedia.org/wiki/Baby_Huey'
url6 = 'http://en.wikipedia.org/wiki/Superman'

#-----
# Step 1. Get a link to the web page from the server, using one
# of the URLs above
web_page = urlopen(url1)

#-----
# Step 2. Extract the web page's content as a character string
html_code = web_page.read().decode("UTF-8")

#----
# Step 3. Close the connection to the web server
web_page.close()

#-----
# Step 4. Extract the Wikipedia page's title (see the
# lecture demos for an example of doing this, but be
# warned that not all Wikipedia pages format the
# title in the same way)
wiki_title = findall('<h1.*>(.+)</h1>', html_code)[0]

#-----
# Step 5. Open the output HTML file for writing (ideally using the
# Wikipedia page's title as the basis for the filename) and
# print a message telling the user the name of the file you're
# creating
filename = wiki_title.replace(' ', '_') + '_Images.html'
print('Creating HTML file:', filename)
html_file = open(filename, 'w')
print('Open it in a web browser to see the result')

#-----
# Step 6. Write the HTML head part into the file
html_file.write('''<!DOCTYPE html>
<html>

    <head>
        <title>TITLE</title>
    </head>

'''.replace('TITLE', wiki_title + ' Images'))

#-----
# Step 7. Write the HTML body, with an image tag for
# each image found in the input web page
html_file.write('''    <body>
''')

# Find all of the image addresses in the web document
image_urls = findall('<img.* src="([^"]+)".*>', html_code)

# Add a markup for each image to our document
for url in image_urls:
    # Ensure that the URL begins with 'https:' (because not
    # all of the image URLs in Wikipedia have this prefix)
    if url.startswith('//'):
        url = 'https:' + url
    elif url.startswith('/static'):
        url = 'https://en.wikipedia.org' + url
    html_file.write('        <img src="' + url + '">\n')
    
html_file.write('''    </body>

</html>''')

#-----
# Step 8. Close the output file (and have a look at it
# in your favourite web browser)
html_file.close()
