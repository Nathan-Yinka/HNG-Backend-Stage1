from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import datetime
import pytz

# Create your views here.
@require_GET
def get_user_info(request):
    slack_name = request.GET.get("slack_name","null")
    track = request.GET.get("track","null")
    
    current_day = datetime.datetime.now(pytz.utc).strftime('%A')
    current_utc_time = datetime.datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': current_utc_time,
        'track': track,
        'github_file_url': 'https://github.com/Nathan-Yinka/HNG-Backend-Stage1/blob/main/api/views.py',
        'github_repo_url': 'https://github.com/Nathan-Yinka/HNG-Backend-Stage1',
        'status_code': 200
    }
    
    return JsonResponse(response)
    
