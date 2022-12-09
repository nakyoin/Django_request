from django.http import HttpResponse

def index(request):
    host = request.META['HTTP_HOST']
    user_browser = request.META['HTTP_USER_AGENT']
    ip = request.META['REMOTE_ADDR']

    return HttpResponse(f"""
    <p> Host: {host}<p>
    <p> User browser: {user_browser}<p>
    <p> User IP: {ip}<p>
    """ )
def error(request):
    return HttpResponse('К сожалению, произошла ошибка', status=400, reason='Incorrect Data')