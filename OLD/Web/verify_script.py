import sys
import os

# Set up paths
skill_root = r"C:\Users\user\.gemini\antigravity\skills\docx"
sys.path.append(skill_root)

from scripts.document import Document

def verify_structure():
    unpacked_path = r"e:\弘光\課程\114.2\OLD\Web\unpacked"
    doc = Document(unpacked_path)
    
    # Get the document body
    body = doc["word/document.xml"]
    
    # Targets to find
    targets = [
        "第10週", "第11週", "第12週", "第13週", 
        "第14週", "第15週", "第16週", "第17週"
    ]
    
    print("Verifying target rows...")
    for target in targets:
        # We look for paragraphs containing the target text
        # In a table, these should be inside <w:tc> (table cell)
        node = body.get_node(tag="w:p", contains=target)
        if node:
            print(f"Found {target}")
            # Try to get the parent row to see the whole row's content
            # w:p -> w:tc -> w:tr
            parent_cell = node.parentNode
            while parent_cell and parent_cell.tagName != "w:tc":
                parent_cell = parent_cell.parentNode
                
            if parent_cell:
                parent_row = parent_cell.parentNode
                if parent_row and parent_row.tagName == "w:tr":
                    # Print all text in the row to see if we can find the subject cell
                    text_content = ""
                    # Simple text extraction for verification
                    for p in parent_row.getElementsByTagName("w:t"):
                        text_content += p.firstChild.nodeValue + " | "
                    print(f"  Row content: {text_content}")
                else:
                    print(f"  Could not find parent row for {target}")
            else:
                 print(f"  Could not find parent cell for {target}")
        else:
            print(f"NOT FOUND: {target}")

if __name__ == "__main__":
    verify_structure()
