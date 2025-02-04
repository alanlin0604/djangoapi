from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

@csrf_exempt
def merge_pdfs(request):
    """合併多個 PDF 頁面的 HTML 內容"""
    if request.method == "GET":
        try:
            # 從請求 URL 獲取參數
            work_order_number = request.GET.get('workOrderNumber', '')
            if not work_order_number:
                return JsonResponse({"error": "Missing work order number"}, status=400)

            pdf_urls = request.GET.getlist('pdf_urls')  # 獲取所有 PDF 網址
            if not pdf_urls:
                return JsonResponse({"error": "No PDF URLs provided"}, status=400)

            responses = []
            for url in pdf_urls:
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    responses.append(response.text)
                except requests.exceptions.RequestException as e:
                    return JsonResponse({"error": f"Failed to fetch {url}: {str(e)}"}, status=500)

            # 合併所有 HTML 內容
            merged_content = "".join(responses)
            return JsonResponse({"merged_content": merged_content}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
