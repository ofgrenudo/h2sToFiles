#!/usr/bin/env python3

import re
import os
import sys
import argparse

# Global Constant Variables
program_name = "headers2files"
program_description = """
headers2files is a Python tool for breaking down large markdown documents into smaller, organized files. 
Designed for users who create "super-documents" with multiple levels of headers, this program extracts 
content based on either H1 (`#`) or H2 (`##`) headers and saves it into separate markdown files.

- **Default Mode:** Splits content by H2 headers (`##`) and creates individual files for each section.
- **H1 Mode:** Groups all content under an H1 header (`#`) into a single file, including subordinate H2 sections.

This tool is perfect for organizing documentation, notes, or large markdown files into easily navigable pieces.
"""
program_epilog = """Licensed Under MIT Copyright (c) 2024 Joshua Winters-Brown"""
program_default_outdir = "output_headers2files"

# Define Parser Configuration
parser = argparse.ArgumentParser(prog=program_name, description=program_description, epilog=program_epilog) 
parser.add_argument("-d", "--document", type=argparse.FileType('r'), required=True, help="Provide the document you want to parse")
parser.add_argument("-o", "--outdir", type=str, default=program_default_outdir, help="Provide your own output directory")
parser.add_argument("-h1", "--header-one", action="store_true", help="Parse on H1 '#' instead of H2 '##'")

# Parse args provided to program
args = parser.parse_args()

# TODO : Implement argparse library.

# Input content
input_text = "\n" + args.document.read() # Fixes bug where the program wont read the first newline header!

# Directory to save the split files
output_directory = args.outdir
os.makedirs(output_directory, exist_ok=True)

def hTWOtoFiles():
    """Create individual files for each H2 and its content."""
    # Regex to find H2 headers and their content (must start with '## ' followed by any text)
    sections = re.split(r"(^## .+|\n## .+)", input_text)
    files = []

    # Process and save each section
    for i in range(1, len(sections), 2):
        header = sections[i].strip()
        content = sections[i + 1].strip() if i + 1 < len(sections) else ""
        filename = f"{header[3:].strip().replace('/', '_')}.md"
        
        # Save each section as a markdown file
        file_path = os.path.join(output_directory, filename)
        with open(file_path, "w") as file:
            file.write(f"{content}")
        files.append(filename)

    print(f"Created {len(files)} files:")
    for file in files:
        print(file)

def hONEtoFiles():
    """Group all content under each H1 into a single file, preserving H2s within the content."""
    # Regex to split by H1 headers (must start with '# ' followed by any text)
    sections = re.split(r"(?<=\n)(# .+)", input_text)
    files = []

    # Process each H1 and its content
    for i in range(1, len(sections), 2):
        header = sections[i].strip()
        # Collect all content under the current H1, including H2 headers and their content
        content = ""
        for j in range(i + 1, len(sections)):
            if re.match(r"(^# .+|\n# .+)", sections[j]):  # Stop at the next H1
                break
            content += sections[j]
        
        # Create a filename from the H1 header
        filename = f"{header[2:].strip().replace('/', '_')}.md"
        
        # Save the grouped content into a single file
        file_path = os.path.join(output_directory, filename)
        with open(file_path, "w") as file:
            file.write(f"{header}\n\n{content.strip()}")
        files.append(filename)

    print(f"Created {len(files)} files:")
    for file in files:
        print(file)

if args.header_one :
    hONEtoFiles()
else:
    hTWOtoFiles()


