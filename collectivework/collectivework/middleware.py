def simple_middleware(get_response):
    #
    def middleware(resquest):
        #view çalıştırılmadan önce çağırılacak
        response = get_response(resquest)
        #view çalıştırıldıktan sonra çağırılacak
        return response
    return middleware

class simpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response=get_response
        #tek seferlik yapılandırma parametreleri
        def __call__(self, request):
            #view çalıştırılmadan önceki kodlar
            response = self.get_response(request)
            #view çalıştırıldıktan sonraki kodlar
            return response
