@login_required
def Pages_Lockscreen(request):
    if request.method == 'POST':
        password=request.POST.get('password')
        lastpage=request.POST.get('lastpage')
        
        lastpage=str(lastpage)
        if 'minimus' in lastpage: #if domain name
            lastpage=lastpage.split("tr",1)[1]
        
            user = auth.authenticate(username=request.user.username,password=password)
            if user is not None:
                if lastpage=='/Pages-Lockscreen/':
                    respons =redirect('index')
                    
                    respons.delete_cookie('last_connection') 
                    return respons    
                respons =redirect(lastpage)
                respons.delete_cookie('last_connection')
                return respons
            else:
                messages.add_message(request, messages.ERROR, _("Your Password is Wrong. Please Try Again"))
        else: #if ip address
            user = auth.authenticate(username=request.user.username,password=password)
            if user is not None:
                respons =redirect('index')
                        
                respons.delete_cookie('last_connection') 
                return respons
            else:
                messages.add_message(request, messages.ERROR, _("Your Password is Wrong. Please Try Again")) 
    respons=render(request, 'Pages-Lockscreen.html',{})
    respons.set_cookie('last_connection', "yes")
    return respons
