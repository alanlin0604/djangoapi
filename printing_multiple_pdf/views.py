from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

@csrf_exempt
def merge_printing_pdfs(request):
    """合併多個印刷派工單 PDF 頁面"""
    if request.method == "POST":
        data = json.loads(request.body)
        urls = data.get("urls", [])

        if not urls:
            return JsonResponse({"error": "No URLs provided"}, status=400)

        responses = []
        for url in urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                responses.append(response.text)
            except requests.exceptions.RequestException as e:
                return JsonResponse({"error": f"Failed to fetch {url}: {str(e)}"}, status=500)

        # 合併所有 HTML 文件內容
        merged_content = "".join(responses)
        return JsonResponse({"merged_content": merged_content}, status=200)
