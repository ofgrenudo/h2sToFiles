# headers2files

headers2files is a Python tool for breaking down large markdown documents into smaller, organized files. 
Designed for users who create "super-documents" with multiple levels of headers, this program extracts 
content based on either H1 (`#`) or H2 (`##`) headers and saves it into separate markdown files.

- **Default Mode:** Splits content by H2 headers (`##`) and creates individual files for each section.
- **H1 Mode:** Groups all content under an H1 header (`#`) into a single file, including subordinate H2 sections.

This tool is perfect for organizing documentation, notes, or large markdown files into easily navigable pieces.


### Features:
- Splits content based on H2 headers (`##`) by default.
- Supports grouping all content under H1 headers (`#`) into a single file, including nested H2 headers.
- Generates output files with filenames derived from the header text.

---

## Usage

### Requirements
- Python 3.x

### Installation
1. Clone this repository or download the script directly.
2. Ensure Python is installed on your system.

### Running the Program
Run the script using the following command:
```bash
python script.py -d <input_file> [-o <output_directory>] [--header-one]
```

#### Arguments:
- `-d`, `--document`: Path to the markdown file to be processed (required).
- `-o`, `--outdir`: Directory to save the output files (optional, defaults to `output_headers2files`).
- `--header-one`: Switches to H1 mode, grouping content under H1 headers instead of creating individual files for H2 headers.

#### Example Commands:
- Split content by H2 headers (default):
  ```bash
  python script.py -d example.md
  ```
- Group content under H1 headers:
  ```bash
  python script.py -d example.md --header-one
  ```

---

## Output
- The program creates markdown files for each header:
  - For H2 mode, a file is created for each H2 header and its content.
  - For H1 mode, a single file is created for each H1 header, grouping all content (including nested H2s).

- Output files are saved in the specified or default directory.

---

## License
This program is licensed under a "do whatever the **** you want" license. Feel free to modify and use it as you see fit!

---

## Contributions
Contributions are welcome! If you encounter issues or have suggestions for improvement, feel free to create a pull request or open an issue.
