from django.shortcuts import render

def home(request):
    if request.method == "POST":
        n1 = eval(request.POST.get('number1'))
        n2 = eval(request.POST.get('number2'))

        op = request.POST.get('operator')

        if op=='+':
            c=n1+n2
        elif op=='-':
            c=n1-n2
        elif op=='*':
            c=n1*n2
        elif op=='/':
            if n2!=0:
                c=n1/n2
            else:
                'error'
        else:
            'coming sooon' 
        return render(request,'index.html',{'answer':c})

    return render(request,'index.html')