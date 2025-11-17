from django.http import JsonResponse
class basicMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        # print(request,"hello")
        if(request.path=="/student/"):
            print(request.method,"method")
            print(request.path)
        response= self.get_response(request)
        return response

# class signupMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         data=json.loads(request.body)
#         username=data.get("username")
#         email=data.get("email")
#         dob=data.get("dob")
#         password=data.get("pswd")
#         #check username rules with regex
#         #check email rules with regex
#         #check dob rules with regex
#         #check password rules with regex

class SscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in ["/job1/","/job2/"]):
            ssc_result=request.GET.get("ssc")
            print(ssc_result,'hello')
            if(ssc_result !='True'):
                return  JsonResponse({"error":"u should qualify atleast ssc for applying this job"},status=400)
        return self.get_response(request)

 
class MedicalFitMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path == "/job1/"):
            medical_fit_result=request.GET.get("medically_fit")
            if(medical_fit_result !='True'):
                return JsonResponse({"error":"u not medically fit to apply for this job role"},status=400)
        return self.get_response(request)
 
class AgeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path in ["/job1/","/job2/"]):
            Age_checker=int(request.GET.get("age",17))
            if(Age_checker >25 and Age_checker<18):
                return JsonResponse({"error":"age must be in b/w 18 and 25"},status=400)
        return self.get_response(request)

