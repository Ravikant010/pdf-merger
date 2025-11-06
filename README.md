
# PDF MERGE TOOL
A Django-based PDF Merger Application

═══════════════════════════════════════════════════════════════════════════════

OVERVIEW
────────────────────────────────────────────────────────────────────────────────

A simple and intuitive web-based PDF merger built with Django and PyPDF2 that
allows users to combine multiple PDF files into a single document. Perfect for
batch processing and document management tasks.


KEY FEATURES
────────────────────────────────────────────────────────────────────────────────

✓ Multiple PDF Upload - Drag and drop or browse to select multiple PDF files
✓ Batch Merging - Combine 2 or more PDF files into a single document
✓ File Validation - Automatic validation to ensure only PDF files are processed
✓ Bookmarks/Outlines - Automatically creates bookmarks for each merged PDF
✓ Timestamped Output - Generated files include timestamp in filename
✓ Clean UI - Modern, responsive interface with visual feedback
✓ Error Handling - Comprehensive error handling for invalid files


TECH STACK
────────────────────────────────────────────────────────────────────────────────

Backend:              Django (Python web framework)
PDF Processing:       PyPDF2 library
Frontend:             HTML, CSS (modern gradient UI)
File Handling:        Python tempfile module
Version Control:      Git


PREREQUISITES
────────────────────────────────────────────────────────────────────────────────

• Python 3.7 or higher
• pip (Python package manager)
• Django 3.2 or higher
• Virtual environment (recommended)


INSTALLATION & SETUP
────────────────────────────────────────────────────────────────────────────────

1. Clone the repository:
   $ git clone <your-repository-url>
   $ cd pdf-merge-tool

2. Create and activate virtual environment:
   $ python -m venv venv
   $ source venv/bin/activate
   # On Windows: venv\Scripts\activate

3. Install dependencies:
   $ pip install -r requirements.txt
   # OR manually:
   $ pip install django PyPDF2

4. Run migrations:
   $ python manage.py migrate

5. Start development server:
   $ python manage.py runserver

6. Access the application:
   Open browser and navigate to: http://127.0.0.1:8000/


PROJECT STRUCTURE
────────────────────────────────────────────────────────────────────────────────

pdf-merge-tool/
├── pdfmergeapp/
│   ├── migrations/           # Database migrations
│   ├── templates/
│   │   └── pdfmergeapp/
│   │       ├── index.html    # Main upload interface
│   │       └── about.html    # About page
│   ├── views.py              # Application logic
│   ├── urls.py               # URL routing
│   ├── models.py             # Database models
│   ├── apps.py
│   └── __init__.py
├── pdfmergeproject/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── static/                   # Static files (CSS, JS)
├── manage.py
├── requirements.txt
└── README.md


API ENDPOINTS
────────────────────────────────────────────────────────────────────────────────

GET  /                  Renders main upload interface
GET  /about/            Renders about/information page
POST /merge/            Handles PDF upload and merging


POST /merge/ - Request Parameters
────────────────────────────────────────────────────────────────────────────────

Parameter:    pdf_files (multipart/form-data)
Type:         Multiple file upload
Required:     Yes
Minimum:      2 PDF files
Accepted:     *.pdf files only

Response on Success (200):
  Content-Type: application/pdf
  Content-Disposition: attachment; filename="merged_pdf_YYYYMMDD_HHMMSS.pdf"
  Body: Binary PDF file content

Response on Error:
  Content-Type: application/json
  Status Codes:
    400 - Bad Request (invalid input)
    405 - Method Not Allowed
    500 - Internal Server Error
  Body: {"error": "descriptive error message"}


HOW TO USE
────────────────────────────────────────────────────────────────────────────────

1. Navigate to http://127.0.0.1:8000/
2. Click the upload area or drag and drop PDF files
3. Select at least 2 PDF files to merge
4. Click Merge button
5. The merged PDF automatically downloads with timestamped filename
6. Each PDF appears as a bookmark in merged document


FEATURES EXPLAINED
────────────────────────────────────────────────────────────────────────────────

File Validation
───────────────
The application validates:
• At least one file is uploaded
• Minimum 2 files provided for merging
• All files have .pdf extension
• Files are valid PDF documents


Temporary File Management
──────────────────────────
Uses Python's tempfile module to:
• Securely store uploaded files during processing
• Automatically clean up temporary files after merging
• Prevent disk space issues from accumulated temp files
• Support concurrent merge operations


Bookmark Creation
──────────────────
Each merged PDF includes bookmarks showing:
• Sequential number of PDF in merge order
• Original filename of each PDF
• Improves navigation in final document


Timestamped Downloads
──────────────────────
Output files named: merged_pdf_YYYYMMDD_HHMMSS.pdf
Benefits:
• Prevents filename conflicts
• Helps organize downloads
• Shows when merge was performed
• Easy to sort by date


ERROR HANDLING
────────────────────────────────────────────────────────────────────────────────

Status Code  Scenario                           Response Type
───────────  ────────────────────────────────   ──────────────
400          No files uploaded                  JSON error
400          Single file uploaded               JSON error
400          Non-PDF files detected             JSON error
400          Corrupted PDF files                JSON error
405          Invalid request method             JSON error
500          Unexpected server error            JSON error


SECURITY CONSIDERATIONS
────────────────────────────────────────────────────────────────────────────────

☐ CSRF protection disabled for merge endpoint
  → Consider implementing token-based authentication in production

☐ File validation prevents non-PDF uploads
  → Only .pdf extensions accepted

☐ Temporary files cleaned up immediately
  → No residual files after processing

☐ No persistent storage of user files
  → Downloads are ephemeral

☐ Input validation on all uploads
  → Files validated before processing

RECOMMENDED PRODUCTION ENHANCEMENTS:
→ Re-enable CSRF tokens
→ Add file size limits
→ Implement rate limiting
→ Add user authentication
→ Use HTTPS only
→ Add logging and monitoring


FUTURE ENHANCEMENTS
────────────────────────────────────────────────────────────────────────────────

Phase 1 (User Experience):
☐ Drag-and-drop reordering of files before merging
☐ Preview thumbnails of uploaded PDFs
☐ Custom filename for merged output
☐ Progress indicator during merging

Phase 2 (Advanced Features):
☐ Password protection for merged PDFs
☐ Page range selection for each PDF
☐ PDF compression options
☐ Batch scheduling with Celery

Phase 3 (Deployment & Scaling):
☐ Docker containerization
☐ Deploy to DigitalOcean/AWS
☐ User authentication and accounts
☐ Merge history and statistics

Phase 4 (Enterprise):
☐ File size optimization
☐ Async job processing
☐ Webhook notifications
☐ API rate limiting
☐ Advanced analytics


DEPENDENCIES
────────────────────────────────────────────────────────────────────────────────

Django>=3.2
PyPDF2>=3.0.0


DEVELOPMENT COMMANDS
────────────────────────────────────────────────────────────────────────────────

# Create superuser
python manage.py createsuperuser

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files (for production)
python manage.py collectstatic

# Run tests
python manage.py test

# Start development server with verbose output
python manage.py runserver --verbosity 2


DEPLOYMENT
────────────────────────────────────────────────────────────────────────────────

For DigitalOcean or similar hosting:

1. Set DEBUG = False in settings.py
2. Configure ALLOWED_HOSTS
3. Set up environment variables
4. Use gunicorn as WSGI server
5. Configure Nginx as reverse proxy
6. Enable HTTPS with Let's Encrypt
7. Set up monitoring and logging


TROUBLESHOOTING
────────────────────────────────────────────────────────────────────────────────

Issue: "No files uploaded"
→ Check if file input is correctly sending data
→ Verify multipart form-data in form tag

Issue: "File is not a PDF"
→ Ensure files have .pdf extension
→ Check file is valid PDF format
→ Use PDF validator tools

Issue: "Merge failed"
→ Check if PDFs are corrupted
→ Verify temporary directory has write permissions
→ Check disk space availability

Issue: "500 error"
→ Check Django logs for detailed error
→ Verify PyPDF2 is installed correctly
→ Ensure temp directory exists


CONTRIBUTING
────────────────────────────────────────────────────────────────────────────────

1. Fork the repository
2. Create feature branch: git checkout -b feature/YourFeature
3. Commit changes: git commit -m 'Add YourFeature'
4. Push to branch: git push origin feature/YourFeature
5. Submit Pull Request


LICENSE
────────────────────────────────────────────────────────────────────────────────

This project is open source and available under the MIT License.
See LICENSE file for details.


AUTHOR & SUPPORT
────────────────────────────────────────────────────────────────────────────────

Built with Django & PyPDF2
Created: 2025
Support: GitHub Issues

For bugs and feature requests, please open an issue on GitHub.


═══════════════════════════════════════════════════════════════════════════════
Generated: November 06, 2025 at 19:31:09 IST
═══════════════════════════════════════════════════════════════════════════════
