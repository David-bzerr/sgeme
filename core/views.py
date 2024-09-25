from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Produto, MovimentoEstoque  # Importando os modelos corretamente
from .forms import LoginForm, RegistrationForm, ProdutoForm, MovimentoEstoqueForm  # Importando os formulários

def home(request):
    return render(request, 'index.html')

# View de login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

# View de registro
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Ajuste no campo de senha
            user.save()
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

# View para cadastrar produto
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')  # Redireciona para a listagem de produtos após o cadastro
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form': form})

# View para listar produtos
def lista_produtos(request):
    produtos = Produto.objects.all()  # Busca todos os produtos do banco de dados
    return render(request, 'lista_produtos.html', {'produtos': produtos})

# View para movimentação de estoque
def movimentar_estoque(request):
    if request.method == 'POST':
        form = MovimentoEstoqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_movimentos')  # Redireciona para a lista de movimentos
    else:
        form = MovimentoEstoqueForm()
    return render(request, 'movimentar_estoque.html', {'form': form})

# View para listar movimentações de estoque
def lista_movimentos(request):
    movimentos = MovimentoEstoque.objects.all()  # Busca todas as movimentações de estoque
    return render(request, 'lista_movimentos.html', {'movimentos': movimentos})
