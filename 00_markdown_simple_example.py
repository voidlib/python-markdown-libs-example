import time

from bs4 import BeautifulSoup

from markdown_content import markdown_content

import markdown


def convert_and_save_markdown_with_toc_markdown_lib(markdown_content, file_name):
    """
    Convert Markdown to HTML with TOC using markdown library, format the HTML, and save to a file.
    """
    print(f"Markdown library:")

    # 1. Simple convert without extra (Do not output)
    html_content = markdown.markdown(markdown_content)

    # 2. Conversion with TOC extension
    html_content = markdown.markdown(markdown_content, extensions=['toc'])

    # Use BeautifulSoup to format HTML code
    soup = BeautifulSoup(html_content, 'html.parser')
    formatted_html = soup.prettify()

    print(f"{formatted_html}")

    # Save HTML result to file
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"HTML content with TOC successfully saved to {file_name} using markdown library.")

import markdown2


def convert_and_save_markdown_with_toc_markdown2_lib(markdown_content, file_name):
    """
    Convert Markdown to HTML with TOC using markdown2 library, format the HTML, and save to a file.
    """
    print(f"Markdown2 library:")

    # 1. Simple convert without extra (Do not output)
    html_content = markdown2.markdown(markdown_content)

    # 2. Conversion with TOC extra
    html_content = markdown2.markdown(markdown_content, extras=["toc"])

    # Use BeautifulSoup to format HTML code
    soup = BeautifulSoup(html_content, 'html.parser')
    formatted_html = soup.prettify()

    print(f"{formatted_html}")

    # Save HTML result to file
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"HTML content with TOC successfully saved to {file_name} using markdown2 library.")

# Display the differences between the two libraries
print("""Comparing "markdown" library and "markdown2" library:\n""")

# Display the differences between the two libraries
print("="*40)
print("Using markdown library:")
print("="*40)
convert_and_save_markdown_with_toc_markdown_lib(markdown_content, 'converted_html/markdown_example_with_toc.html')

print("\n" + "="*40)
print("Using markdown2 library:")
print("="*40)
convert_and_save_markdown_with_toc_markdown2_lib(markdown_content, 'converted_html/markdown2_example_with_toc.html')
