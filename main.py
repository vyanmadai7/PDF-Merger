from PyPDF2 import PdfMerger 
import os                   

def merge_pdfs(folder_path, output_name):
    # Create a PDF merger object
    merger = PdfMerger()

    # Get all PDF files from the given folder
    files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

    # Sort files alphabetically
    files.sort()

    # Add each PDF file into the merger
    for pdf in files:
        path = os.path.join(folder_path, pdf)  
        merger.append(path)                  
        print("Added:", pdf)

    # Create output file path
    output_path = os.path.join(folder_path, output_name)

    # Write all merged PDFs into a single file
    merger.write(output_path)
    merger.close() 

    print(f"\nAll PDFs merged successfully into: {output_name}")

if __name__ == "__main__":
    print("===== PDF Merger Tool =====")

    #Ask the user for folder path and output name
    folder = input("Enter folder path: ").strip()
    output = input("Enter output file name: ").strip()

    try:
        merge_pdfs(folder, output)
    except Exception as e:
        print(f"Error Occurred: {e}") 