from django.shortcuts import redirect, render
from django.core.mail import EmailMessage

# Create your views here.

def contactosForm(request):

    if request.method == 'POST':

        nome = request.POST['name']
        email = request.POST['email']
        assunto = request.POST['Assunto']
        mensagem = request.POST['textarea']

        envio_do_email = EmailMessage(f'APP DJANGO: {assunto}', f'O usuário com o nome de {nome}. Escreve o seguinte:\n\n {mensagem}.\n\n E-mail do visitante do site: {email}', '', ['sitepessoal249@gmail.com'], reply_to=[email])

        retribuição = EmailMessage('Gestão de pedidos: AGRADECIMENTO!', f'Muito obrigado por preencher o formulário no site GESTÃO DE PEDIDOS com o assunto: \"{assunto}\".\nEstou sempre disponível a receber críticas construtivas que possam ajudar no crescimento do site e aperfeiçoamento das minhas habilidades como estudante de programação!\n\n Cumprimentos\n Lourenço Gulo\n\n\nE-mail pessoal: gastronumo@gmail.com\nTelefone: +351 936417787', '', [email], reply_to=['sitepessoal249@gmail.com'])

        try:
            envio_do_email.send()
            retribuição.send()
            return redirect('/contactos/?valid')
        except:
            return redirect('/contactos/?notvalid')

    return render(request, 'contacto.html')