"""
Text parser for converting raw text into structured slide content.
Auto-detects titles, sections, bullets, and paragraphs.
"""

import re
from typing import List, Dict, Tuple


class TextParser:
    """Parse raw text and auto-detect slide structure"""

    def __init__(self):
        self.title_pattern = re.compile(r'^#{1,2}\s+(.+)$', re.MULTILINE)
        self.heading_pattern = re.compile(r'^###\s+(.+)$|^[A-Z][A-Za-z\s]{5,}:?$', re.MULTILINE)
        self.bullet_pattern = re.compile(r'^[\s]*[\-\*\+]\s+(.+)$', re.MULTILINE)
        self.numbered_pattern = re.compile(r'^[\s]*\d+[\.\)]\s+(.+)$', re.MULTILINE)
        self.empty_line_pattern = re.compile(r'^\s*$', re.MULTILINE)

    def parse(self, text: str) -> List[Dict]:
        """
        Parse raw text and return structured slide content
        
        Returns list of slide dictionaries with:
        - title: str
        - type: str ('title', 'content', 'bullets')
        - content: str or List[str]
        """
        slides = []
        paragraphs = self._split_by_blank_lines(text)

        current_slide = None
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            # Detect if this is a title/heading
            if self._is_title(para):
                if current_slide:
                    slides.append(current_slide)
                current_slide = {
                    'title': para.replace('# ', '').replace('## ', '').strip(),
                    'type': 'title',
                    'content': ''
                }
            elif current_slide and self._is_bullet_list(para):
                bullets = self._extract_bullets(para)
                current_slide['type'] = 'bullets'
                current_slide['content'] = bullets
            elif current_slide:
                current_slide['content'] = para
                current_slide['type'] = 'content'
            else:
                # First paragraph might be a title
                current_slide = {
                    'title': para[:50] + '...' if len(para) > 50 else para,
                    'type': 'content',
                    'content': para
                }

        if current_slide:
            slides.append(current_slide)

        return slides

    def _split_by_blank_lines(self, text: str) -> List[str]:
        """Split text into paragraphs by blank lines"""
        paragraphs = re.split(r'\n\s*\n', text)
        return paragraphs

    def _is_title(self, text: str) -> bool:
        """Check if text is a title/heading"""
        # Markdown style
        if text.startswith('# ') or text.startswith('## '):
            return True
        # All caps or title case with less than 60 chars
        if len(text) < 60 and len(text.split()) <= 8:
            if text.isupper() or (text[0].isupper() and ':' in text):
                return True
        return False

    def _is_bullet_list(self, text: str) -> bool:
        """Check if text contains bullet points"""
        lines = text.split('\n')
        bullet_count = 0
        for line in lines:
            if re.match(r'^[\s]*[\-\*\+]\s+', line):
                bullet_count += 1
        return bullet_count >= 2 or (bullet_count > 0 and len(lines) <= 5)

    def _extract_bullets(self, text: str) -> List[str]:
        """Extract bullet points from text"""
        lines = text.split('\n')
        bullets = []
        for line in lines:
            match = re.match(r'^[\s]*[\-\*\+]\s+(.+)$', line)
            if match:
                bullets.append(match.group(1).strip())
            elif line.strip() and not match:
                # Include non-bullet lines as text
                if bullets:
                    bullets[-1] += ' ' + line.strip()
        return [b.strip() for b in bullets if b.strip()]


class ContentBlock:
    """Represents a block of content for a slide"""

    def __init__(self, content_type: str, text: str):
        self.type = content_type  # 'title', 'heading', 'body', 'bullet', 'numbered'
        self.text = text

    def __repr__(self):
        return f"ContentBlock(type={self.type}, text={self.text[:30]}...)"


def parse_text(text: str) -> List[Dict]:
    """Convenience function to parse text"""
    parser = TextParser()
    return parser.parse(text)
