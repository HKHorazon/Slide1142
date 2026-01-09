import subprocess
import os

def export_marp_slides(input_file, output_format='pdf', theme_path=None):
    print("exporting...")
    output_file = input_file.replace('.md', f'.{output_format}')
    
    # Base command
    command = [
        'marp', input_file, 
        '--pdf',
        '--theme--set', theme_path,
        '-o', output_file]
    

    try:
        subprocess.run(command, check=True)
        print(f"Successfully exported {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def multi_export_marp_slides(theme_path=None):
    # export all files in MD directory to PDF directory as PDF Files (include subdirectories)
    input_dir = 'MD'
    output_dir = 'PDF'
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                os.makedirs(output_subdir, exist_ok=True)
                output_file_path = os.path.join(output_subdir, file.replace('.md', '.pdf'))
                
                print(f"Exporting {input_file_path} to {output_file_path}...")
                
                # Build command
                command = ['marp', input_file_path, '-o', output_file_path]
                
                # Add theme if specified
                if theme_path and os.path.exists(theme_path):
                    command.extend(['--theme-set', theme_path])
                
                try:
                    subprocess.run(command, check=True)
                    print(f"Successfully exported to {output_file_path}")
                except subprocess.CalledProcessError as e:
                    print(f"Error exporting {input_file_path}: {e.stderr}")


if __name__ == "__main__":
    # Usage examples
    # multi_export_marp_slides(theme_path='themes/my-theme.css')
    export_marp_slides('a.md', 'pdf', theme_path='HoraStyle.css')
    # export_marp_slides('presentation.md', 'pptx', theme_path='themes/my-theme.css')