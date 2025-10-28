# Math Homework Environment Template

A template for setting up a math homework environment with note downloading, LaTeX compilation, and comprehensive mathematical typesetting capabilities.

## Features

- Download notes from notes.sjtu.edu.cn and convert to Markdown
- Compile LaTeX documents with XeLaTeX
- Comprehensive LaTeX preamble for mathematical typesetting
- Virtual environment setup with dependency management

## Setup

1. Install this template using mango
2. The installation script will create a virtual environment and install dependencies
3. Use `mango download <url>` to download notes
4. Use `mango compile <file.tex>` to compile LaTeX documents

## Requirements

- Python 3.8+
- XeLaTeX (for LaTeX compilation)
- Required fonts (see preamble.tex)

## Usage

### Downloading Notes

```bash
mango download https://notes.sjtu.edu.cn/s/abcdefg
```

Options:
- `--html-file`: Use a local HTML file instead of downloading
- `-o, --output`: Specify output file (defaults to stdout)

### Compiling LaTeX Documents

```bash
mango compile homework.tex
```

This will compile the LaTeX file using XeLaTeX and output the PDF in the same directory.

## File Structure

```
.
├── .mango/
│   ├── .instructions    # Command exports
│   ├── .on_install     # Installation script
│   ├── download         # Note downloader script
│   └── compile         # LaTeX compilation script
├── note_downloader.py   # Python script for downloading notes
├── preamble.tex         # LaTeX preamble with math packages
├── requirements.txt     # Python dependencies
└── README.md          # This file
```

## LaTeX Preamble Features

The included [`preamble.tex`](preamble.tex) provides:

- Comprehensive math packages (amsmath, amssymb, mathtools)
- Chinese language support (ctex)
- Custom math commands and environments
- Theorem environments for questions and answers
- Proper formatting for academic papers

## Dependencies

The Python dependencies are pinned for reproducibility:

- requests>=2.25.0,<3.0.0
- beautifulsoup4>=4.9.0,<5.0.0
- markdownify>=0.6.0,<1.0.0
- lxml>=4.6.0,<5.0.0

## Troubleshooting

### LaTeX Compilation Issues

If you encounter font-related errors, ensure you have the required fonts installed:
- XCharter-Math
- Noto Serif CJK SC
- Noto Sans CJK SC

### Python Issues

The installation script checks for Python 3.8+ compatibility. If you encounter issues, ensure you're using the correct Python version.

## License

This template is provided as-is for educational purposes.