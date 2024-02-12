from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages 
def register(request):
    form = RegisterForm()
    
    if request.method =='POST':
        form =RegisterForm(request.POST)

        if form.is_valid():
            form.save() 
            messages.success(request, 'Usuario gravado sucesso...')    
            return redirect('contact:index')
        else:
            messages.error(request, 'Formulario nao gravado, contem  erro...')       
            messages.info(request, 'Formulario nao gravado, contem  info...')       
            messages.warning(request, 'Formulario nao gravado, contem  aviso...')       
            messages.success(request, 'Formulario nao gravado, contem  sucesso...')       
    return render(
        request,
        'contact/register.html',
        {'form': form}
    )
