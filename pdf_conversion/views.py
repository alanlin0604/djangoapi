from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from weasyprint import HTML
import json
import requests

@csrf_exempt
def generate_pdf(request):
    """根據提供的 HTML 內容生成 PDF 並返回下載"""
    if request.method == "POST":
        data = json.loads(request.body)
        urls = data.get("urls", [])

        if not urls:
            return HttpResponse("No URLs provided", status=400)

        # 下載所有 HTML 內容
        html_content = ""
        for url in urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                html_content += response.text
            except requests.exceptions.RequestException as e:
                return HttpResponse(f"Error fetching {url}: {str(e)}", status=500)

        # 轉換 HTML 為 PDF
        pdf_file = HTML(string=html_content).write_pdf()

        # 返回 PDF 作為回應
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="merged_document.pdf"'
        return response
