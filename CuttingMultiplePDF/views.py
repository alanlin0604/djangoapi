from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def merge_pdfs(request):
    """合併多個 PDF 的 HTML 輸出"""
    if request.method == "GET":
        try:
            # 從請求 URL 獲取參數
            url_params = request.GET.getlist('urls')  # 獲取 URL 列表

            if not url_params:
                return JsonResponse({"error": "No URLs provided"}, status=400)

            responses = []
            for url in url_params:
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    responses.append(response.text)
                except requests.exceptions.RequestException as e:
                    return JsonResponse({"error": f"Failed to fetch {url}: {str(e)}"}, status=500)

            # 合併所有 HTML 文件內容
            merged_content = "".join(responses)
            return JsonResponse({"merged_content": merged_content}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
