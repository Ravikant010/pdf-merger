from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PyPDF2 import PdfMerger
import tempfile
import os
from datetime import datetime


def index(request):
    """Main page with file upload interface"""
    return render(request, 'pdfmergeapp/index.html')


def about(request):
    """About page"""
    return render(request, 'pdfmergeapp/about.html')


@csrf_exempt
def merge_pdfs(request):
    """Handle PDF file upload and merging"""
    if request.method == 'POST' and request.FILES:
        try:
            pdf_files = request.FILES.getlist('pdf_files')
            
            if len(pdf_files) == 0:
                return JsonResponse({'error': 'No files uploaded'}, status=400)
            
            if len(pdf_files) == 1:
                return JsonResponse({'error': 'Please upload at least 2 PDF files to merge'}, status=400)

            # Validate all files are PDFs
            for pdf_file in pdf_files:
                if not pdf_file.name.lower().endswith('.pdf'):
                    return JsonResponse({'error': f'File {pdf_file.name} is not a PDF'}, status=400)

            merger = PdfMerger()
            temp_files = []

            # Process each PDF file
            for i, pdf_file in enumerate(pdf_files):
                # Create temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
                    for chunk in pdf_file.chunks():
                        tmp.write(chunk)
                    tmp_path = tmp.name
                    temp_files.append(tmp_path)

                # Add to merger with outline_item (updated from bookmark)
                try:
                    merger.append(tmp_path, outline_item=f"{i+1}. {pdf_file.name}")
                except Exception as e:
                    # Clean up temp files
                    for temp_file in temp_files:
                        if os.path.exists(temp_file):
                            os.unlink(temp_file)
                    return JsonResponse({'error': f'Error processing {pdf_file.name}: {str(e)}'}, status=400)

            # Create merged PDF
            merged_pdf_path = tempfile.mktemp(suffix='.pdf')
            merger.write(merged_pdf_path)
            merger.close()

            # Clean up individual temp files
            for temp_file in temp_files:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)

            # Read merged PDF and return as response
            with open(merged_pdf_path, 'rb') as f:
                pdf_content = f.read()
                
            # Clean up merged temp file
            os.unlink(merged_pdf_path)

            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"merged_pdf_{timestamp}.pdf"

            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            response['Content-Length'] = len(pdf_content)
            
            return response

        except Exception as e:
            return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
