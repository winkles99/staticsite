from inline_markdown import markdown_to_html_node, extract_title
import os
from pathlib import Path

def generate_page(from_path: str, template_path: str, dest_path: str):
    """
    Generates an HTML page.
    
    - from_path:    path to source Markdown file
    - template_path: path to HTML template containing {{ Title }} and {{ Content }} placeholders
    - dest_path:    path where the generated HTML should be written
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # 1. Read markdown
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown_src = f.read()
    
    # 2. Read template
    with open(template_path, 'r', encoding='utf-8') as f:
        template_src = f.read()
    
    # 3. Convert markdown → HTML
    # assume markdown_to_html_node is in scope
    node = markdown_to_html_node(markdown_src)
    html_content = node.to_html()
    
    # 4. Extract title
    title = extract_title(markdown_src)
    
    # 5. Inject into template
    page_src = (
        template_src
        .replace('{{ Title }}', title)
        .replace('{{ Content }}', html_content)
    )
    
    # 6. Ensure destination directory exists
    dest_dir = Path(dest_path).parent
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # 7. Write out
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(page_src)
    
    print(f"Page written to {dest_path}")
