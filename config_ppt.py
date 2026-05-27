"""
Configuration and styling defaults for PowerPoint presentations
"""

from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# Default colors
COLORS = {
    'primary': RGBColor(0, 51, 102),      # Dark blue
    'accent': RGBColor(0, 102, 204),      # Light blue
    'text': RGBColor(0, 0, 0),            # Black
    'light_text': RGBColor(255, 255, 255),  # White
    'background': RGBColor(255, 255, 255),  # White
}

# Font settings
FONTS = {
    'title': {
        'name': 'Calibri',
        'size': Pt(54),
        'bold': True,
        'color': COLORS['primary'],
    },
    'subtitle': {
        'name': 'Calibri',
        'size': Pt(32),
        'bold': True,
        'color': COLORS['accent'],
    },
    'heading': {
        'name': 'Calibri',
        'size': Pt(28),
        'bold': True,
        'color': COLORS['primary'],
    },
    'body': {
        'name': 'Calibri',
        'size': Pt(18),
        'bold': False,
        'color': COLORS['text'],
    },
    'bullet': {
        'name': 'Calibri',
        'size': Pt(16),
        'bold': False,
        'color': COLORS['text'],
    },
}

# Slide layout settings
SLIDE_DIMENSIONS = {
    'width': Inches(10),
    'height': Inches(7.5),
}

MARGINS = {
    'left': Inches(0.5),
    'right': Inches(0.5),
    'top': Inches(0.5),
    'bottom': Inches(0.5),
}

# Text detection patterns
PATTERNS = {
    'title': r'^[A-Z][A-Za-z\s]{2,}[.!?]?$',  # Capitalized title-like text
    'heading': r'^#{1,3}\s+(.+)$',  # Markdown heading
    'bullet': r'^[\-\*\+]\s+(.+)$',  # Bullet point
    'numbered': r'^\d+[\.]\)\s+(.+)$',  # Numbered list
}
