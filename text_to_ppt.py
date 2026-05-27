"""
Main entry point - CLI for converting text to PowerPoint
"""

import argparse
import sys
from pathlib import Path
from text_parser_ppt import parse_text
from ppt_generator_ppt import generate_from_slides


def main():
    parser = argparse.ArgumentParser(
        description='Convert raw text into PowerPoint presentations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python text_to_ppt.py input.txt output.pptx
  python text_to_ppt.py -i input.txt -o presentation.pptx
  cat text.txt | python text_to_ppt.py -o output.pptx
        '''
    )

    parser.add_argument(
        'input',
        nargs='?',
        help='Input text file (use "-" or omit for stdin)'
    )
    parser.add_argument(
        'output',
        nargs='?',
        default='output.pptx',
        help='Output PowerPoint file (default: output.pptx)'
    )
    parser.add_argument(
        '-i', '--input',
        dest='input_file',
        help='Input text file path'
    )
    parser.add_argument(
        '-o', '--output',
        dest='output_file',
        help='Output PowerPoint file path'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    # Determine input and output files
    input_file = args.input_file or args.input
    output_file = args.output_file or args.output or 'output.pptx'

    # Read input text
    try:
        if input_file and input_file != '-':
            if not Path(input_file).exists():
                print(f"Error: Input file '{input_file}' not found", file=sys.stderr)
                sys.exit(1)
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
            if args.verbose:
                print(f"Read {len(text)} characters from '{input_file}'")
        else:
            text = sys.stdin.read()
            if args.verbose:
                print(f"Read {len(text)} characters from stdin")

        if not text.strip():
            print("Error: Input text is empty", file=sys.stderr)
            sys.exit(1)

        # Parse text
        if args.verbose:
            print("Parsing text structure...")
        slides = parse_text(text)

        if args.verbose:
            print(f"Detected {len(slides)} slides")
            for i, slide in enumerate(slides, 1):
                print(f"  Slide {i}: {slide['type']} - {slide['title'][:50]}")

        # Generate PowerPoint
        if args.verbose:
            print(f"Generating PowerPoint presentation...")
        output_path = generate_from_slides(slides, output_file)

        print(f"✓ Successfully created: {output_path}")
        if args.verbose:
            print(f"  {len(slides)} slides in presentation")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
