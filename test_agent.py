#!/usr/bin/env python
"""
Test script to verify the agent functionality
"""

import sys
from pathlib import Path
from text_parser_ppt import parse_text
from ppt_generator_ppt import generate_from_slides

def test_basic_parsing():
    """Test basic text parsing"""
    print("Test 1: Basic Text Parsing")
    text = """
# Introduction to Python

Python is a powerful programming language.

## Key Features

- Easy to learn
- Versatile
- Large community

## Getting Started

Install Python from python.org
    """
    
    slides = parse_text(text)
    print(f"  ✓ Parsed {len(slides)} slides")
    for i, slide in enumerate(slides, 1):
        print(f"    Slide {i}: {slide['type']:10} - {slide['title'][:40]}")
    
    assert len(slides) > 0, "No slides parsed"
    print("  ✓ Test passed\n")

def test_ppt_generation():
    """Test PowerPoint generation"""
    print("Test 2: PowerPoint Generation")
    
    slides = [
        {'title': 'Welcome', 'type': 'title', 'content': 'A Test Presentation'},
        {'title': 'Slide 1', 'type': 'content', 'content': 'This is content'},
        {'title': 'Points', 'type': 'bullets', 'content': ['Point 1', 'Point 2', 'Point 3']}
    ]
    
    output_file = 'test_output.pptx'
    result = generate_from_slides(slides, output_file)
    
    assert Path(result).exists(), f"Output file not created: {result}"
    print(f"  ✓ Created PowerPoint: {result}")
    print(f"  ✓ File size: {Path(result).stat().st_size} bytes")
    print("  ✓ Test passed\n")
    
    return result

def test_example_file():
    """Test with example file"""
    print("Test 3: Example File Processing")
    
    example_file = Path(__file__).parent / 'examples' / 'sample_text.txt'
    if not example_file.exists():
        print(f"  ⚠ Example file not found: {example_file}")
        return
    
    text = example_file.read_text()
    slides = parse_text(text)
    
    print(f"  ✓ Parsed example file: {len(slides)} slides")
    
    output_file = 'example_output.pptx'
    result = generate_from_slides(slides, output_file)
    
    assert Path(result).exists(), f"Output file not created: {result}"
    print(f"  ✓ Generated: {result}")
    print(f"  ✓ File size: {Path(result).stat().st_size} bytes")
    print("  ✓ Test passed\n")

def main():
    print("\n" + "="*50)
    print("PowerPoint Text Conversion Agent - Tests")
    print("="*50 + "\n")
    
    try:
        test_basic_parsing()
        test_ppt_generation()
        test_example_file()
        
        print("="*50)
        print("All tests passed! ✓")
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
