
from django.shortcuts import redirect

# create our  own middlewares..
def authMiddleware(get_response):

    def middlewares(request):
        returnUrl = request.META['PATH_INFO']
        # print(returnUrl)
        if not request.session.get('customer'):
            return redirect(f'/login?return_url={returnUrl}')

        response = get_response(request)
        return response
    
    return middlewares
