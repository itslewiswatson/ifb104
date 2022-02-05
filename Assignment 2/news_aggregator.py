#
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10221131
#    Student name: Lewis Watson
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  News Feed Aggregator
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to aggregate RSS news feeds.
#  See the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.
#
# NB: You may NOT use any Python modules that need to be downloaded
# and installed separately, such as "Beautiful Soup" or "Pillow".
# Only modules that are part of a standard Python 3 installation may
# be used. 

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.  You may import other widgets
# from the Tkinter module provided they are ones that come bundled
# with a standard Python 3 implementation and don't have to
# be downloaded and installed separately.)
from tkinter import *

# Import a special Tkinter widget we used in our demo
# solution.  (You do NOT need to use this particular widget
# in your solution.  You may import other such widgets from the
# Tkinter module provided they are ones that come bundled
# with a standard Python 3 implementation and don't have to
# be downloaded and installed separately.)
from tkinter.scrolledtext import ScrolledText

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed one day).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----------------------------------------------------------
#
# A function to download and save a web document. If the
# attempted download fails, an error message is written to
# the shell window and the special value None is returned.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document or RSS Feed.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * lying - If True the Python function will hide its identity
#      from the web server. This can be used to prevent the
#      server from blocking access to Python programs. However
#      we do NOT encourage using this option as it is both
#      unreliable and unethical!
# * got_the_message - Set this to True once you've absorbed the
#      message about Internet ethics.
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'xhtml',
             save_file = True,
             char_set = 'UTF-8',
             lying = False,
             got_the_message = True):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        if lying:
            # Pretend to be something other than a Python
            # script (NOT RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent', 'Mozilla/5.0')
            if not got_the_message:
                print("Warning - Request does not reveal client's true identity.")
                print("          This is both unreliable and unethical!")
                print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError:
        print("Download error - Cannot find document at URL '" + url + "'\n")
        return None
    except HTTPError:
        print("Download error - Access denied to document at URL '" + url + "'\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to download " + \
              "the document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError:
        print("Download error - Unable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("Download error - Unable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#


# Type hinting
from typing import List, Dict


#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# HTML export template
html_block_pre = '''
<!-- Standard HTML boilerplate -->
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>New Electronic Way Stories (NEWS)</title>
        
        <!-- Our own custom styling -->
        <style>
            /* Entire document gets the same font */
			body {
				font-family: Arial, Helvetica, sans-serif;
			}

            /* Centre main fluid div */
            .content {
                display: table;
                margin-right: auto;
                margin-left: auto;    
            }

            /* Ensure width changes based on screen size (utilise all space on mobile) */
            @media only screen and (max-width: 768px) {
                .content {
                    width: 100%
                }
            }

            /* Ensure width changes based on screen size (less space for desktop/laptop) */
            @media only screen and (min-width: 769px) {
                .content {
                    width: 70%
                }
            }

            /* Move article div to left */
            .article {
                float: left;
            }

            /* Article's content should stand out */
            .article p {
                font-size: 18px;
            }

            /* Make sure the article's text is next to the image */
            .article-text {
                float: right !important;
            }

            /* Move the image to the left */
            .article img {
                float: left;
            }

            /* Force images to fit, behave and scale nicely */
            img {
                height: 40%;
                width: 30%;
                object-fit: contain;
                margin: 20px;
            }

            /* Remove default list styling */
            ul {
                padding: 0;
                list-style-type: none;
            }        
        </style>

        <!-- Make it easily viewable on mobile browsers -->
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <!-- Main div where everything lives -->
        <div class="content">

            <!-- Custom centered heading -->
            <div style="display: table; margin-right: auto; margin-left: auto;">
				<img src="http://photos.myjoyonline.com/photos/news/201811/500285510698_7451607283980.jpg" style="width: 90%;">
				<div class="heading">
					<h1>New Electronic Way Stories (NEWS)</h1>
				</div>
			</div>

            <!-- Separate content -->
            <hr>

            <!-- Begin unordered list of articles -->
            <ul>
'''

# HTML export template
html_block_post = '''
            </ul> <!-- Close unordered article list -->
        </div>
    </body>
</html>
'''

# Global encoding type
encoding_type = 'utf8'

# Database file
db_file_name = 'news_log.db'

# Name of the exported news file. To simplify marking, your program
# should produce its results using this file name.
news_file_name = 'news.html'

# Limit on number of news stories
news_stories_limit = 10

# Regex parser function suffix
regex_parser_suffix = '_regex_parser'

# List of news sources
news_sources = {
    'onion': {
        'name': 'The Onion',
        'link': 'https://www.theonion.com/rss',
        'file': 'the_onion',
        'static': True
    },
    'wired': {
        'name': 'Wired.com',
        'link': 'https://www.wired.com/feed',
        'file': 'wired',
        'static': True
    },
    'nyp': {
        'name': 'New York Post',
        'link': 'https://nypost.com/news/feed/',
        'file': 'nyp',
        'static': False
    },
    'motorsport': {
        'name': 'Motorsport.com',
        'link': 'https://www.motorsport.com/rss/all/news/',
        'file': 'motorsport',
        'static': False
    }
}

# Format for an article
# 
#   article = {
#       'headline': 'This is the article\'\s headline',
#       'photo': 'http://bad-news-site.com/image.png',
#       'description':'This is the description of an article',
#       'link': 'http://bad-news-site.com/selected-article',
#       'publisher': 'The Example Herald',
#       'published': '31 February 1973'
#   }

# ------------------------ UTILITY FUNCTIONS ------------------------ #

# Check whether an article is formatted correctly
def is_valid_article(article) -> bool:
    if (not isinstance(article, dict)):
        return False
    if (not 'headline' in article):
        return False
    if (not 'photo' in article):
        return False
    if (not 'description' in article):
        return False
    if (not 'link' in article):
        return False
    if (not 'publisher' in article):
        return False
    if (not 'published' in article):
        return False
    return True

# Call functions via their string names
def call_function(func: str, args: list):
    # If it exists in the global scope
    if func in globals():
        # Call function
        return globals()[func](*args)
    
    print('Fatal error: could not find specified function')
    return False

# Checks if a specified file exists and is accessible (ie r+w privileges)
def does_file_exist(file_name: str) -> bool:
    try:
        f = open(file_name, encoding=encoding_type)
        f.close()
    except IOError:
        return False
    except FileNotFoundError:
        return False
    return True

# Extract the inner content of a HTML tag (eg: <p>inner content</p>)
def find_html_inner(html: str, tag: str) -> list:
    return findall('<\s*' + tag + '[^>]*>(.*?)<\s*/\s*' + tag + '>', html)

# Extract the inner content of a HTML tag's attribute (eg: <div tag="inner content"></div>)
def find_html_attribute(html: str, tag: str, attribute: str) -> list:
    return findall('\<' + tag + '.+?' + attribute +'\=(?:\"|\')(.+?)(?:\"|\')(?:.+?)\>', html)

# Special cdata matching functionality
def find_cdata_content(html: str) -> list:
    return findall('\[CDATA\[(.*?)\]\]>', html)

# Remove new lines and anything that may interfere with regex
def clean_artifacts(html: str) -> str:
    html = html.strip()
    html = html.replace('\n', '')
    html = html.replace('\t', '')
    return html

# Strip HTML for humans
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

# ------------------------ DATABASE FUNCTIONALITY ------------------------ #

# Database variable
db = None

# Once-off-unique connection function
def db_connect():
    global db 
    try:
        db = connect(db_file_name)
    except Error:
        return False
    return True

# Connect at runtime
db_connect()

# Clear table of all data
def db_truncate():
    cur = db.cursor()
    cur.execute('DELETE FROM selected_stories')

# Insert a new article
def db_insert_headline(article: dict):
    if (not is_valid_article(article)):
        return
    
    # Prepare statement
    stmt = 'INSERT INTO selected_stories (headline, news_feed, publication_date) VALUES (?, ?, ?)'
    params = (article['headline'], article['publisher'], article['published'])

    # Execute SQL statement
    cur = db.cursor()
    cur.execute(stmt, params)
    db.commit()

# ------------------------ SITE REGEX PARSERS ------------------------ #

# The Onion
def onion_regex_parser(news_item: str, site_title: str) -> dict:
    article_title = find_html_inner(news_item, 'title')[0]
    outer_description = find_html_inner(news_item, 'description')[0]
    inner_description = find_html_inner(outer_description, 'p')[0]
    inner_description = striphtml(inner_description)
    image = find_html_attribute(outer_description, 'img', 'src')[0]
    date_published = find_html_inner(news_item, 'pubDate')[0]
    article_link = find_html_inner(news_item, 'link')[0]

    return {
        'headline': article_title,
        'photo': image,
        'description': inner_description,
        'link': article_link,
        'publisher': site_title,
        'published': date_published
    }

# Wired.com
def wired_regex_parser(news_item: str, site_title: str) -> dict:
    article_title = find_html_inner(news_item, 'title')[0]
    date_published = find_html_inner(news_item, 'pubDate')[0]
    article_link = find_html_inner(news_item, 'link')[0]
    description = find_html_inner(news_item, 'description')[0]
    photo = find_html_attribute(news_item, 'media:thumbnail', 'url')[0]
    publisher = find_html_inner(news_item, 'dc:publisher')[0]

    # More specific domain handling
    long_domain = findall('(?: |//|^)([A-Za-z0-9]{1,}\.[A-Za-z0-9]{1,10}\.?[A-Za-z]{1,}\.?[A-Za-z]{1,})(?: |/|$)', article_link)[0]
    short_domain = findall('\w+\.\w{2,3}$', long_domain)[0].capitalize()

    return {
        'headline': article_title,
        'photo': photo,
        'description': description,
        'link': article_link,
        'publisher': short_domain + ' (' + publisher + ')',
        'published': date_published
    } 

# New York Post
def nyp_regex_parser(news_item: str, site_title: str) -> dict:
    # Remove HTML special characters
    site_title = site_title.replace('&#124;', '|')
    site_title = site_title.replace('&#8216;', "'")

    article_title = find_html_inner(news_item, 'title')[0]
    image = find_html_attribute(news_item, 'enclosure', 'url')[0]
    date_published = find_html_inner(news_item, 'pubDate')[0]
    article_link = find_html_inner(news_item, 'link')[0]
    description = find_cdata_content(news_item)[0]

    return {
        'headline': article_title,
        'photo': image,
        'description': description,
        'link': article_link,
        'publisher': site_title,
        'published': date_published,
    }

# Motorsport.com
def motorsport_regex_parser(news_item: str, site_title: str) -> dict:
    image = find_html_attribute(news_item, 'enclosure', 'url')[0]
    article_link = find_html_inner(news_item, 'link')[0]
    headline = find_cdata_content(news_item)[0]
    date_published = find_html_inner(news_item, 'pubDate')[0]

    # Split at first sentence to avoid super long description
    description = find_cdata_content(news_item)[1].split('.')[0] + '.'

    return {
        'headline': headline,
        'photo': image,
        'description': description,
        'link': article_link,
        'publisher': site_title,
        'published': date_published,
    }

# Download articles at runtime (if required)
for source, news_source in news_sources.items():
    # Only download for static sources that do not currently exist
    if (not does_file_exist(news_source['file'] + '.xhtml')):
        if (news_source['static'] == True):
            download(url=news_source['link'], target_filename=news_source['file'])

# Main back-end function
def generate_articles_for_source(source: str, limit: int = news_stories_limit) -> List[dict]:
    # Don't generate articles if they are not wanted by user
    if (limit == 0):
        return []

    # Prohibit random edge cases but handle gracefully
    if (not news_sources[source]):
        print('Error: Source does not exist')
        return []

    # Download live versions
    if (news_sources[source]['static'] == False):
        result = download(url=news_sources[source]['link'], target_filename=news_sources[source]['file'])
        if (result == None):
            # Return a generic error that we can render
            return [{'error': 'Cannot access source ' + news_sources[source]['name']}]
    
    # Open file
    f = open(news_sources[source]['file'] + '.xhtml', encoding=encoding_type)
    
    # Read contents into memory
    rss_feed = f.read()

    # Close file handle to save memory
    f.close()

    rss_feed = clean_artifacts(rss_feed)

    # List of formatted articles
    articles = []

    # Extract news items
    news_items = find_html_inner(rss_feed, 'item')

    # Limit to the user-defined limit, or the default as defined
    news_items = news_items[0:(limit)]

    # Get the title of the site
    site_title = find_html_inner(rss_feed, 'title')[0]

    # Extract article attributes
    for news_item in news_items:
        # Common HTML symbols
        news_item = news_item.replace('&amp;', '&')
        news_item = news_item.replace('&#8217;', "'")
        news_item = news_item.replace('&#8216;', "'")
        news_item = news_item.replace('&amp;', '&')

        # Execute custom regex for each source to extract article
        article = call_function(source + regex_parser_suffix, [news_item, site_title])
        articles.append(article)

    return articles

# Generate all articles with respect to selections
def generate_articles(sources: dict) -> Dict[str, List[dict]]:
    articles = {} # Empty dictionary for all article types and their articles

    for source_name, qty in sources.items():
        if (not source_name in articles):
            articles[source_name] = []

        try:
            generated_articles = generate_articles_for_source(source_name, qty)
        except KeyError:
            generate_articles = []

        articles[source_name] = generated_articles
    
    return articles

# ------------------------ FRONT-END FUNCTIONALITY ------------------------ #

# GUI selected stories
selected_stories = None

# Current articles as selected
selected_stories_articles = None

# Generate HTML for all articles
def generate_articles_html(articles: List[dict]) -> str:
    # Empty articles so nothing is selected
    if (len(articles) == 0):
        return ''
    
    # Count number of valid articles
    valid_article_count = 0
    for article in articles:
        if (is_valid_article(article)):
            valid_article_count += 1
    if (valid_article_count == 0):
        return ''

    site = ''
    articles_html = ''
    for article in articles:
        site = article['publisher'] # Extract site info
        articles_html += generate_article_html(article) # Generate HTML from boilerplate

    return articles_html

# Generate HTML for each article
def generate_article_html(article: dict) -> str:
    if (not is_valid_article(article)):
        return ''

    # Return string with info inserted into
    return '''
                <!-- This is an article as a list item -->
                <li>
                    <div class="article">
                        <!-- Enclose this in another div for future proofness -->
                        <div class="article-text">

                            <!-- Article photo -->
                            <img alt="Article Image Goes Here" src="''' + article['photo'] + '''">

                            <!-- Allow user to navigate to original article in new tab -->
                            <a target="_blank" href="''' + article['link'] + '''"><h3>''' + article['headline'] + '''</h3></a>

                            <!-- Article's brief description -->
                            <p>''' + article['description'] + '''</p>

                            <!-- Display the publisher / article's origin -->
                            <p><strong>''' + article['publisher'] + '''</strong> => ''' + article['published'] + '''</p>
                        </div>
                    </div>
                </li>
    '''

# Calculate what the selected stories are from the GUI input
def calc_selected_stories() -> dict:
    global selected_stories
    selected_stories = {
        'onion': onion_variable.get(),
        'wired': wired_variable.get(),
        'nyp': nyp_variable.get(),
        'motorsport': motorsport_variable.get()
    }
    return selected_stories

# Shorthand article formatting for text box
def get_shorthand_article_string(article: dict) -> str:
    return article['headline']+ ' (' + article['publisher'] + ')' + '\n' + '[' + article['published'] + ']'

# Display list of shorthand selected sources
def display_selected_stories():
    global selected_stories
    global selected_stories_articles

    # Generate information that we need
    selected_stories = calc_selected_stories()
    selected_stories_articles = generate_articles(selected_stories) or {}

    text_articles.configure(state='normal') # Enable text to be changed
    text_articles.delete('1.0', END) # Clear the text box

    # Iterate to retrieve 
    for news_source, article_list in selected_stories_articles.items():
        for article in article_list:
            # Listen for a KeyError which would mean the article is an error
            try:
                article_string = get_shorthand_article_string(article)
            except KeyError:
                # Return error
                article_string = 'WARNING: Cannot retrieve articles for ' + news_sources[news_source]['name']
            
            text_articles.insert(END, article_string + '\n\n') # Append the above string            
    
    text_articles.configure(state=DISABLED) # Disable changing the text box

# Save displayed stories to the SQLite database
def save_selected_stories():
    global selected_stories_articles

    # No stories displayed - nothing to save
    if (selected_stories_articles == None):
        print('No stories selected')
        return

    # Save to database
    db_truncate()

    # Insert headlines
    for article_list in selected_stories_articles:
        for article in article_list:
            try:
                db_insert_headline(article)
            except KeyError:
                print('Not a valid article - cannot insert into db')

# Export selected articles to a .html file
def export_selected_stories():
    global selected_stories_articles

    # No stories displayed - nothing to export
    if (selected_stories_articles == None):
        print('No stories selected')
        return

    # Append to this content
    html_content = ''

    for news_source, article_list in selected_stories_articles.items():
        html_content += generate_articles_html(article_list)         

    # The entire HTML file with the content in the middle
    html_document = html_block_pre + html_content + html_block_post

    # Open and overwrite contents (+ create if not exist)
    exported_news_file = open(news_file_name, 'w', encoding=encoding_type)
    exported_news_file.write(html_document)
    exported_news_file.close()

# -------------------------- TK GUI -------------------------- #

window = Tk()
window.title('New Electronic Way Stories (NEWS)')

# Banner image
img_application_banner = PhotoImage(file='banner.gif')
lbl_img_banner = Label(image=img_application_banner)

# Article text content
text_articles = ScrolledText(window, height=20, width=45)
text_articles.insert(END, 'None')
text_articles.configure(state=DISABLED)

# Dropdowns & labels
option_menu_variables = range(0, 11) # Define range and use everywhere

onion_variable = IntVar(window)
onion_variable.set(0)
onion_menu = OptionMenu(window, onion_variable, *option_menu_variables)
onion_label = Label(window, text='The Onion (Static)')

wired_variable = IntVar(window)
wired_variable.set(0)
wired_menu = OptionMenu(window, wired_variable, *option_menu_variables)
wired_label = Label(window, text='Wired.com (Static)')

nyp_variable = IntVar(window)
nyp_variable.set(0)
nyp_menu = OptionMenu(window, nyp_variable, *option_menu_variables)
nyp_label = Label(window, text='New York Post (Live)')

motorsport_variable = IntVar(window)
motorsport_variable.set(0)
motorsport_menu = OptionMenu(window, motorsport_variable, *option_menu_variables)
motorsport_label = Label(window, text='Motorsport.com (Live)')

# Functional buttons
btn_display_selections = Button(window, text='Display Selected Stories', width=20, command=display_selected_stories)
btn_export_selections = Button(window, text='Export', width=15, command=export_selected_stories)
btn_save_selections = Button(window, text='Save', width=15, command=save_selected_stories)

# Grid
lbl_img_banner.grid(row=0, column=0, columnspan=4)
text_articles.grid(row=1, column=2, rowspan=4, columnspan=2)

onion_label.grid(row=1, column=0, sticky=W, padx=10)
onion_menu.grid(row=1, column=1)

wired_label.grid(row=2, column=0, sticky=W, padx=10)
wired_menu.grid(row=2, column=1)

nyp_label.grid(row=3, column=0, sticky=W, padx=10)
nyp_menu.grid(row=3, column=1)

motorsport_label.grid(row=4, column=0, sticky=W, padx=10)
motorsport_menu.grid(row=4, column=1)

btn_display_selections.grid(row=5, column=0, columnspan=2)
btn_export_selections.grid(row=5, column=2)
btn_save_selections.grid(row=5, column=3)

window.mainloop()