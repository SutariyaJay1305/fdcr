from django.shortcuts import render
from .models import UIManager,ReportTypes,DataManager
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def index(request):
    title_text = UIManager.objects.get(UI_position=1)
    text2 = UIManager.objects.get(UI_position=2)
    report_type = ReportTypes.objects.all()
    context = {
        "title_text":title_text,
        "text2":text2,
        "report_type":report_type
        }
    
    return render(request,'index.html',context)

@csrf_protect
def verify(request):
    if request.method == 'POST':
        q = request.POST['q']
        report_type = request.POST['report_type']
        try:
            data = DataManager.objects.get(report_number=q,is_active=True,report_type=report_type)
            return JsonResponse({'status': 'success', 'message': 'Successfully Verified'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Not Verified'})
