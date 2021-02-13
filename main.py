import csv
import urllib.parse

# this function creates a library list,
# with all "books" inside
def make_library(file):
    library = []
    with open(file, 'r') as file:
        reader = csv.reader(file)
        runs = 0

        column_names = []
        for row in reader:
            # add a row containing the first line of the csv: Book Id,Title,Author,etc etc
            if runs == 0:
                column_names = row
            runs += 1
            # make a book dictionary containing all data of a specific book.
            book = dict(zip(column_names, row))
            library.append(book)
    # remove the collum names from the library
    library.pop(0)
    # return the library with all the books
    return library


# find all the unread books
def unread_titles_in_library(library):
    search_terms = []

    # loop over each book, and add them if they are unread
    for book in library:
        if int(book['Read Count']) < 1:
            search_terms.append(book['Title'])
    return search_terms


# find only the books not read
def titles_in_library(library):
    search_terms = []

    for book in library:
        search_terms.append(book['Title'])
    return search_terms


# the standard file name: change it if it suits you
library = make_library('goodreads_library_export.csv')

# remove unread_ to get the links for read books aswell
titlesToSearch = unread_titles_in_library(library)

# loop over the titles and generate a pirate bay url for each book
search_result_urls = []
for title in titlesToSearch:
    pirateBayEbookLink = r"https://www.thepiratebay.org/search.php?q=" + urllib.parse.quote_plus(title) + "&cat=601"
    search_result_urls.append(pirateBayEbookLink)
# loop over links and save those with a result found
for link in search_result_urls:
    print(link)
