# Agent Metadata

This file contains metadata and configuration for using this agent in your workflow.

## Quick Info

- **Agent Name**: PowerPoint Text Conversion Agent
- **Purpose**: Convert raw text into formatted PowerPoint presentations
- **Language**: Python 3.7+
- **Status**: Production Ready
- **Maintainer**: Jay Shah (@jaypshah123-del)

## Setup

```bash
pip install -r requirements.txt
```

## Quick Usage

### CLI
```bash
python text_to_ppt.py input.txt output.pptx
```

### Python
```python
from text_parser_ppt import parse_text
from ppt_generator_ppt import generate_from_slides

slides = parse_text("# Title\n\nContent here")
generate_from_slides(slides, 'output.pptx')
```

## Key Functions

### `parse_text(text: str) -> List[Dict]`
Parse raw text and return structured slide content.

**Input**: Raw text string  
**Output**: List of slide dictionaries with title, type, and content

### `generate_from_slides(slides: List[Dict], output_path: str) -> str`
Generate PowerPoint from structured slides.

**Input**: List of slides and output file path  
**Output**: Path to created PowerPoint file

## Configuration

Edit `config_ppt.py` to customize:
- Colors and themes
- Font styles and sizes
- Slide dimensions and margins
- Text detection patterns

## Customization

### Add Custom Templates
Create new slide types by extending `SlideTemplate` in `templates_ppt.py`

### Modify Parsing Logic
Adjust detection rules in `TextParser` class in `text_parser_ppt.py`

## Testing

```bash
python test_agent.py
```

## Examples

See `examples/sample_text.txt` for sample input format.

## Dependencies

- **python-pptx** (0.6.21+): PowerPoint file manipulation

## Performance

- Converts ~10KB text in <1 second
- Memory efficient (~10MB for large documents)
- Output file size: 100KB-500KB depending on content

## Support

For issues or questions:
1. Check the README.md for detailed documentation
2. Review examples in the `examples/` directory
3. Open an issue on GitHub

## Version History

### v1.0 (Current)
- ✓ Text parsing with auto-detection
- ✓ Multiple slide templates
- ✓ Customizable styling
- ✓ CLI interface
- ✓ Comprehensive documentation

## Integration Tips

1. **Batch Processing**: Use in loops to convert multiple files
2. **Custom Styling**: Modify `config_ppt.py` before calling functions
3. **Error Handling**: Check for empty input and valid file paths
4. **Pipeline Integration**: Easily integrable with other Python tools

## Troubleshooting Checklist

- [ ] Python 3.7+ installed
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Input file is readable and non-empty
- [ ] Output directory exists or is writable
- [ ] Text has clear structure (blank line separators)
- [ ] Markdown headers used for titles

## License

MIT License - Free for commercial and personal use
