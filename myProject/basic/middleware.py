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

class signupMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        data=json.loads(request.body)
        username=data.get("username")
        email=data.get("email")
        dob=data.get("dob")
        password=data.get("pswd")
        #check username rules with regex
        #check email rules with regex
        #check dob rules with regex
        #check password rules with regex

