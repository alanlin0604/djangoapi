from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
from datetime import datetime
from django.shortcuts import render

def mo_view(request):
    return render(request, 'MO.html')  
# 日期格式化函數
def format_date(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    return date.strftime('%Y-%m-%d %H:%M:%S')

# 資料展示視圖
def display_data(request):
    # 獲取主表數據
    response1 = requests.get('http://<ip>/api/gettable1')
    data1 = response1.json()

    # 處理每個項目，將上傳日期、編輯日期格式化並添加詳細資料
    for item in data1:
        item['上傳日期'] = format_date(item['上傳日期'])
        item['上次編輯日期'] = format_date(item['上次編輯日期'])

        # 獲取該製令單號的詳細資料
        response2 = requests.get(f'http://<ip>/api/gettable2?s={item["製令單號"]}')
        item['details'] = response2.json()

    return render(request, 'data_template.html', {'data': data1})

# 刪除資料的視圖
def remove_item(request, order_id):
    if request.method == 'POST':
        # 調用 API 刪除指定項目
        response = requests.post('http://<ip>/api/removetable1', data={'ids': order_id})
        
        if response.status_code == 200:
            # 成功刪除後，重新加載頁面
            return redirect('display_data')
        else:
            return JsonResponse({'error': '刪除失敗'}, status=500)

# 定義自動刷新視圖
def refresh_data(request):
    return redirect('display_data')

# 渲染 MO.html 的視圖
def mo_view(request):
    # 獲取主表數據
    response1 = requests.get('http://<ip>/api/gettable1')
    data1 = response1.json()

    # 處理每個項目，將上傳日期、編輯日期格式化並添加詳細資料
    for item in data1:
        item['上傳日期'] = format_date(item['上傳日期'])
        item['上次編輯日期'] = format_date(item['上次編輯日期'])

        # 獲取該製令單號的詳細資料
        response2 = requests.get(f'http://<ip>/api/gettable2?s={item["製令單號"]}')
        item['details'] = response2.json()

    return render(request, 'MO.html', {'data': data1})
