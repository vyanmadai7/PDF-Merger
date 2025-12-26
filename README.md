✨ Features

🚀 Simple & Fast - Merge PDFs in seconds
📂 Batch Processing - Handles all PDFs in a folder automatically
🔤 Smart Sorting - Files merged in alphabetical order
💬 Interactive CLI - Easy-to-use command-line interface
⚡ Lightweight - Only one dependency required

📦 Installation
bash# Clone the repository
git clone https://github.com/yourusername/pdf-merger-tool.git
cd pdf-merger-tool

# Install required package
pip install PyPDF2
🚀 Usage
bashpython pdf_merger.py
```

**Follow the prompts:**
```
===== PDF Merger Tool =====
Enter folder path: ./my-documents
Enter output file name: combined.pdf

Added: chapter-01.pdf
Added: chapter-02.pdf
Added: chapter-03.pdf

All PDFs merged successfully into: combined.pdf
```

### 📖 How It Works

1. **Specify folder** containing your PDF files
2. **Name your output** file
3. **Done!** - All PDFs merged and saved in the same folder

Files are automatically sorted alphabetically, so use prefixes like `01-`, `02-` to control the order.

### 🎯 Use Cases

- Combine multiple scanned documents
- Merge report chapters into one file
- Consolidate invoices or receipts
- Join split PDF files

### ⚙️ Requirements

- Python 3.x
- PyPDF2

### 🛠️ Configuration

The script uses sensible defaults, but you can modify the `merge_pdfs()` function to:
- Filter specific PDF patterns
- Add custom sorting logic
- Include subdirectories

### ❗ Troubleshooting

**Error: Folder not found**
- Check the folder path is correct
- Use absolute paths if relative paths don't work

**Error: Permission denied**
- Ensure you have write permissions in the folder
- Close any PDFs that are currently open

**PDFs in wrong order**
- Rename files with number prefixes: `01-file.pdf`, `02-file.pdf`

### 📝 Example File Structure
```
my-documents/
├── 01-introduction.pdf
├── 02-methodology.pdf
├── 03-results.pdf
└── 04-conclusion.pdf

→ Output: combined.pdf (in my-documents/)
🤝 Contributing
Contributions welcome! Feel free to:

Report bugs
Suggest features
Submit pull requests

📄 License
MIT License - free to use and modify.
