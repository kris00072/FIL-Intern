def middleware(get_response):
    print("One time initialization")
    def my_function(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response
    return my_function