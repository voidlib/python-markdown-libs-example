import time

from markdown_content import markdown_content

import markdown


def convert_md_with_toc_and_calc_time_markdown_lib(markdown_content, iterations=10):
    """
    Convert Markdown to HTML with TOC using the markdown library and calculate time.
    """
    print(f"Time taken for markdown library:")

    # 1. Simple conversion without extras (Do not output)
    start_time = time.time()
    for _ in range(iterations):
        html_content = markdown.markdown(markdown_content)
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / iterations
    print(f"  1) Simple conversion:")
    print(f"      - {total_time:.6f} seconds: Total time for all tests")
    print(f"      - {average_time:.6f} seconds: Average time per conversion")

    # 2. Conversion with TOC extension
    start_time = time.time()
    for _ in range(iterations):
        html_content = markdown.markdown(markdown_content, extensions=['toc'])
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / iterations
    print(f"  2) With extra TOC conversion:")
    print(f"      - {total_time:.6f} seconds: Total time for all tests")
    print(f"      - {average_time:.6f} seconds: Average time per conversion")


import markdown2


def convert_md_with_toc_and_calc_time_markdown2_lib(markdown_content, iterations=10):
    """
    Convert Markdown to HTML with TOC using the markdown2 library and calculate time.
    """
    print(f"Time taken for markdown2 library:")

    # 1. Simple conversion without extras (Do not output)
    start_time = time.time()
    for _ in range(iterations):
        html_content = markdown2.markdown(markdown_content)
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / iterations
    print(f"  1) Simple conversion:")
    print(f"      - {total_time:.6f} seconds: Total time for all tests")
    print(f"      - {average_time:.6f} seconds: Average time per conversion")

    # 2. Conversion with TOC extra
    start_time = time.time()
    for _ in range(iterations):
        html_content = markdown2.markdown(markdown_content, extras=["toc"])
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / iterations
    print(f"  2) With extra TOC conversion:")
    print(f"      - {total_time:.6f} seconds: Total time for all tests")
    print(f"      - {average_time:.6f} seconds: Average time per conversion")

# Number of iterations for timing
iterations = 10000

# Display the differences between the two libraries
print(f'Comparing "markdown" library and "markdown2" library with {iterations} iterations for each test:')


# Display the differences between the two libraries
print("="*40)
print("Using markdown library:")
print("="*40)
convert_md_with_toc_and_calc_time_markdown_lib(markdown_content, iterations)

print("\n" + "="*40)
print("Using markdown2 library:")
print("="*40)
convert_md_with_toc_and_calc_time_markdown2_lib(markdown_content, iterations)
