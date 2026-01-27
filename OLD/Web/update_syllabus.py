import sys
import os

# Set up paths
skill_root = r"C:\Users\user\.gemini\antigravity\skills\docx"
sys.path.append(skill_root)

from scripts.document import Document

def update_syllabus():
    unpacked_path = r"e:\弘光\課程\114.2\OLD\Web\unpacked"
    doc = Document(unpacked_path, rsid="D30097E3")
    
    body = doc["word/document.xml"]
    
    updates = {
        "第10週": "Introduction to Interactive Media and Web",
        "第11週": "Simple Website Development Experience",
        "第12週": "Frontend vs Backend",
        "第13週": "HTML Basics",
        "第14週": "Style and CSS",
        "第15週": "DOM and JavaScript",
        "第16週": "Frontend Frameworks and Modern Web Development",
        "第17週": "AI Web Development Experience"
    }
    
    print("Updating syllabus...")
    count = 0
    for key, translation in updates.items():
        # Find the row containing the week label
        node = body.get_node(tag="w:p", contains=key)
        if node:
            # Navigate to the cell containing the main text
            # Assuming structure: Week Cell -> Date Cell -> Content Cell
            # We found the Week Cell paragraph. Go up to cell, then row.
            week_cell = node.parentNode
            while week_cell and week_cell.tagName != "w:tc":
                week_cell = week_cell.parentNode
            
            if week_cell:
                row = week_cell.parentNode
                if row and row.tagName == "w:tr":
                    # Get all cells in this row
                    cells = row.getElementsByTagName("w:tc")
                    if len(cells) >= 3:
                        content_cell = cells[2] # 3rd cell (index 2) is Content
                        
                        # Check if translation already exists to avoid duplicates
                        content_text = ""
                        for p in content_cell.getElementsByTagName("w:t"):
                             if p.firstChild: content_text += p.firstChild.nodeValue
                        
                        if translation in content_text:
                            print(f"  Skipping {key}, translation already present.")
                        else:
                            # Append new paragraph with translation
                            # Create a new paragraph with appropriate styling if possible, or just a paragraph
                            # We can try to copy styling from the last paragraph in the cell
                            last_p = content_cell.getElementsByTagName("w:p")[-1]
                            
                            # Simple insertion: Insert a new paragraph with content
                            # We insert an empty line (spacing) then the English text
                            print(f"  Updating {key} with '{translation}'")
                            
                            # Add an empty paragraph for spacing
                            empty_p = '<w:p><w:pPr><w:spacing w:before="0" w:after="0"/></w:pPr></w:p>'
                            doc["word/document.xml"].insert_after(last_p, empty_p)
                            
                            # Re-fetch last_p (which is now the empty p)
                            last_p = content_cell.getElementsByTagName("w:p")[-1]
                            
                            # Add the translation paragraph
                            # Use basic P structure
                            eng_p = f'<w:p><w:pPr><w:spacing w:before="0" w:after="0"/></w:pPr><w:r><w:t>{translation}</w:t></w:r></w:p>'
                            doc["word/document.xml"].insert_after(last_p, eng_p)
                            count += 1
                    else:
                        print(f"Row for {key} has unexpected cell count: {len(cells)}")
                else:
                    print(f"Parent of cell is not row for {key}")
            else:
                 print(f"Could not find cell for {key}")
        else:
            print(f"Week label {key} not found")
            
    print(f"Updated {count} entries.")
    doc.save()

if __name__ == "__main__":
    update_syllabus()
