# Markdown Library Comparison Project

This project is designed to showcase different methods of processing\
Markdown content into HTML using Python libraries. I created this\
repository when I was choosing a library to use in my project and\
wanted to compare the two most popular options:
- `markdown`: a classic Python library. More information here:\
https://github.com/Python-Markdown/markdown
- `markdown2`: a very popular library. More information here:\
https://github.com/trentm/python-markdown2

It splits the functionality across three scripts,\
each serving a specific purpose.

## 1. Final Decision and Library Comparison

I Chose `markdown` Over `markdown2`

### 1.1. Test Results

#### Basic Performance Test

The test results on my laptop showed a significant advantage of the `markdown`
library—it is up to 11 times faster in bulk tests and from 2 to 4 times more
efficient in single tests (single tests are not shown in the output):

```console
> python .\01_markdown_conversion_time.py
Comparing "markdown" library and "markdown2" library with 10000 iterations for each test:
========================================
Using markdown library:
========================================
Time taken for markdown library:
  1) Simple conversion:
      - 3.902678 seconds: Total time for all tests
      - 0.000390 seconds: Average time per conversion
  2) With extra TOC conversion:
      - 5.335405 seconds: Total time for all tests
      - 0.000534 seconds: Average time per conversion

========================================
Using markdown2 library:
========================================
Time taken for markdown2 library:
  1) Simple conversion:
      - 35.368335 seconds: Total time for all tests
      - 0.003537 seconds: Average time per conversion
  2) With extra TOC conversion:
      - 36.475701 seconds: Total time for all tests
      - 0.003648 seconds: Average time per conversion
```

#### Comparison of Resulting HTML Code

Results can be seen in the `converted_html` folder—exactly what the libraries\
generated. And in the terminal display, the formatted code is displayed, which\
will simply be easier to understand.

Surprisingly, both libraries generate almost identical HTML—there are only four\
minor differences I noticed:

- First and foremost, markdown2 adds new lines between every HTML tag, whereas\
markdown does not. This could affect the readability of the HTML when viewed\
directly in a code editor.

- The `markdown` library does not add a newline after the last line in a code\
block, resulting in the last line containing code + closing code block tags:

```html
<p><code>console
$ cd my_folder</code></p>
```

In the case of `markdown`, it is slightly more readable:

```html
<p><code>console
$ cd my_folder
</code></p>
```

- When titles contain non-unicode characters, like the Russian alphabet, the\
`markdown` library generates TOC labels only with readable unicode characters,\
e.g., numbers:

```html
<h2 id="11">Заголовок 1.1</h2>
```

whereas `markdown2` generates labels containing non-unicode characters:

```html
<h2 id="заголовок-11">Заголовок 1.1</h2>
```

This is not critical, but it can cause problems somewhere, for example, when\
generating links to headings in the text.

- Additionally, the markdown2 library does not automatically replace the\
  [TOC] tag with generated HTML. It only keeps it stored in the Python object,\
  leaving the [TOC] tag unprocessed in the final HTML.\
  Users must manually replace it in the HTML:

```html
<p>[TOC]</p>
```

### 1.2. Conclusion and Library Selection

After thorough testing and comparison, I chose the `markdown` library for the\
following reasons:

- **Simplicity and Flexibility**: `markdown` provides a straightforward way of\
  converting Markdown to HTML, with enough flexibility to customize the output as\
  needed.
- **Performance**: In my benchmarks, `markdown` performed slightly better,\
  especially in scenarios involving large documents and complex Markdown features.\
- **Extensibility**: The ability to easily integrate with other Python tools and\
  libraries without extensive configuration or compatibility issues was a\
  significant factor.

These factors made `markdown` the more suitable choice for my needs.

## 2. Guide to Usage and Project Details

### 2.1. Files Description

- **markdown_content.py**: Contains the Markdown string used as the input for
  conversion processes in the other scripts. This script ensures that the
  Markdown content is centralized and can be easily updated.

- **00_simple_markdown_example.py**: Demonstrates a simple example of converting
  Markdown to HTML using the `markdown` and `markdown2` libs. It includes the
  use of extensions such as Table of Contents (TOC).

- **01_markdown_conversion_time.py**: Measures and outputs the performance time
  of converting Markdown to HTML using the `markdown` and `markdown2` libs.
  This script focuses on performance metrics and comparisons between different
  conversion methods.

### 2.2. Requirements

- 1. **Python 3 Installation**: Ensure that Python 3.6 or higher is installed on
   your system. You can check this by running `python --version` or
   `python3 --version` in your command prompt or terminal.

- 2. **Library Installation**: This project requires the following Python
   libraries:
   - `markdown`
   - `markdown2`
   - `beautifulsoup4`

   Install the necessary libraries using the following command:

```bash
$ pip install markdown markdown2 beautifulsoup4
```

   This ensures that all dependencies are properly installed to avoid any
   compatibility issues during the execution of the scripts.

### 2.3. Downloading the Project Repository

To download this project repository to your local machine,\
you have a few options:

- Clone the Repository via git
- Download as ZIP file

#### Clone the Repository via git

If you have Git installed on your system, you can clone the repository\
using the following command in your terminal or command prompt:

```console
  # Clone the repo via HTTPS
  # (Do not use SSH because it requires configured local git credentials)
$ REPO_URL='https://github.com/voidlib/python-markdown-libs-example.git' && \
  GOAL_DIR_NAME='python-markdown-libs-example' && \
  git clone "${REPO_URL}" "${GOAL_DIR_NAME}"
```

This will create a local copy of the repository on your machine.

#### Download as ZIP file

Alternatively, you can download the repository as a ZIP file.\
Simply navigate to the repository's page here and click on the "Code" button.\
Then select "Download ZIP" to save the ZIP file to your computer.\
After downloading, extract the contents of the ZIP file to access\
the repository files.

### 2.4. How to Use

Run the scripts from your terminal or command prompt:

```bash
$ python 00_simple_markdown_example.py
$ python 01_markdown_conversion_time.py
```

### 2.5. Contribution

Feel free to fork this repository and submit pull requests to enhance the
functionalities or improve the existing methods. For major changes, please open
an issue first to discuss what you would like to change.
