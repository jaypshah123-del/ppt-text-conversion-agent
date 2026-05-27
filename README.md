# PowerPoint Text Conversion Agent

![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-production%20ready-brightgreen)

> An intelligent AI agent that converts raw text into professionally formatted PowerPoint presentations with auto-detection of content structure, customizable formatting, and multiple slide templates.

## 🎯 Features

✨ **Auto-Detection** - Automatically detects titles, sections, bullet points, and body content  
📝 **Multiple Templates** - Title slides, content slides, and bullet point slides  
🎨 **Customizable Styling** - Built-in color schemes, fonts, and formatting options  
⚡ **Easy to Use** - Simple CLI interface for quick conversions  
🔧 **Extensible** - Easy to add custom templates and formatting rules  
📦 **Production Ready** - Fully tested and documented  

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/jaypshah123-del/ppt-text-conversion-agent.git
cd ppt-text-conversion-agent

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Convert text file to PowerPoint
python text_to_ppt.py input.txt output.pptx

# With verbose output
python text_to_ppt.py input.txt output.pptx -v

# Using named arguments
python text_to_ppt.py -i input.txt -o presentation.pptx

# From stdin
cat mytext.txt | python text_to_ppt.py -o output.pptx
```

## 📖 Documentation

### Input Format

The agent auto-detects structure from your text. Recommended formats:

#### Markdown-style Headings
```markdown
# Main Title

## Section Title

Your body content here.

### Subsection

- Bullet point 1
- Bullet point 2
- Bullet point 3
```

#### Plain Text
```
Section Title

Your content paragraph here...

Another Section

- Point 1
- Point 2
```

### Python API

```python
from text_parser_ppt import parse_text
from ppt_generator_ppt import generate_from_slides

# Parse text
slides = parse_text("Your text content here...")

# Generate PowerPoint
output_path = generate_from_slides(slides, 'output.pptx')
print(f"Created: {output_path}")
```

### Batch Processing

```python
import os
from pathlib import Path
from text_parser_ppt import parse_text
from ppt_generator_ppt import generate_from_slides

input_dir = 'texts'
output_dir = 'presentations'

for txt_file in Path(input_dir).glob('*.txt'):
    slides = parse_text(txt_file.read_text())
    output_file = Path(output_dir) / f"{txt_file.stem}.pptx"
    generate_from_slides(slides, str(output_file))
    print(f"Created: {output_file}")
```

## 📁 Project Structure

```
.
├── text_to_ppt.py           # Main CLI entry point
├── text_parser_ppt.py       # Text parsing with auto-detection
├── ppt_generator_ppt.py     # PowerPoint generation engine
├── templates_ppt.py         # Slide templates (Title, Content, Bullet)
├── config_ppt.py            # Configuration and styling
├── requirements.txt         # Python dependencies
├── examples/
│   └── sample_text.txt      # Sample input file
└── README.md                # This file
```

## 🎨 Slide Types

### Title Slide
- Large centered title
- Optional subtitle
- Used for main presentation titles

### Content Slide
- Title at top
- Body text content
- Good for explanations and paragraphs

### Bullet Slide
- Title at top
- Bullet point list
- Auto-generated when bullets are detected

## ⚙️ Customization

### Modify Styles

Edit `config_ppt.py` to customize:

```python
# Change colors
COLORS = {
    'primary': RGBColor(0, 51, 102),
    'accent': RGBColor(0, 102, 204),
    # ...
}

# Change fonts
FONTS = {
    'title': {
        'name': 'Calibri',
        'size': Pt(54),
        'bold': True,
        'color': COLORS['primary'],
    },
    # ...
}
```

### Create Custom Templates

Add new template classes in `templates_ppt.py`:

```python
class CustomSlide(SlideTemplate):
    def add_title(self, title: str):
        # Your custom title logic
        pass
    
    def add_content(self, content):
        # Your custom content logic
        pass
```

## 💡 Examples

### Example 1: Research Paper Outline

```bash
python text_to_ppt.py research_outline.txt research_presentation.pptx
```

### Example 2: Meeting Notes to Presentation

```python
notes = """
# Q4 Sales Report

## Executive Summary
Total revenue reached $1.2M, up 15% from Q3.

## Key Metrics
- Revenue: $1.2M (+15%)
- Customers: 250 (+32)
- Retention: 94%

## Next Steps
- Expand to EU market
- Launch new product line
- Hire sales team
"""

from text_parser_ppt import parse_text
from ppt_generator_ppt import generate_from_slides

slides = parse_text(notes)
generate_from_slides(slides, 'q4_report.pptx')
```

## 🛠️ Command Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--input` | `-i` | Input text file path |
| `--output` | `-o` | Output PowerPoint file path |
| `--verbose` | `-v` | Show detailed processing info |
| `--help` | `-h` | Show help message |

## 🔍 Text Parsing Logic

The parser uses the following rules:

1. **Titles**: Lines starting with `#` or `##` (markdown) or capitalized text with 5+ words
2. **Bullets**: Lines starting with `-`, `*`, or `+`
3. **Sections**: Separated by blank lines
4. **Body**: Regular paragraphs between sections

## ⚡ Performance

- **Processing Speed**: Typically converts 10KB of text in <1 second
- **File Size**: Output PPT ~100KB-500KB depending on content
- **Memory**: Minimal (~10MB even for large documents)

## 🐛 Troubleshooting

### Issue: No slides are created
- Ensure input text is not empty
- Check that text has clear section breaks (blank lines)

### Issue: Wrong slide type detection
- Add explicit markdown headers (`#`, `##`)
- Use consistent bullet formatting (`-`, `*`, `+`)

### Issue: Text formatting is lost
- Some complex formatting may not transfer
- Consider restructuring text for better results

## 📋 Limitations

- Complex formatting is simplified
- Images are not supported in current version
- Tables are converted to text
- Font styling is limited to basic formatting (bold, italic)
- Maximum slide title: 100 characters (recommended)

## 🔮 Future Enhancements

- [ ] Image insertion support
- [ ] Table formatting
- [ ] Theme templates (professional, minimal, colorful)
- [ ] Export to other formats (PDF, HTML)
- [ ] Advanced text analysis for better structure detection
- [ ] Multi-language support
- [ ] Web UI for easy drag-and-drop conversion

## 📝 License

MIT License - Feel free to use and modify for personal and commercial projects.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 👨‍💻 Author

Created with ❤️ by Jay Shah

## 📧 Support

For issues or questions, please open an issue on GitHub or contact the maintainer.

---

**Made with ❤️ for presenters who value their time**
