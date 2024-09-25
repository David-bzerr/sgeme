from django.urls import path
from .views import login_view, home, register_view, cadastrar_produto, lista_produtos, movimentar_estoque, lista_movimentos

urlpatterns = [
    path('', home, name='home'),  # URL para a página inicial
    path('login/', login_view, name='login'),  # URL para a tela de login
    path('register/', register_view, name='register'),  # URL para a página de cadastro
    path('produtos/', lista_produtos, name='lista_produtos'),  # Listagem de produtos
    path('produtos/cadastrar/', cadastrar_produto, name='cadastrar_produto'),  # Cadastro de produtos
    path('estoque/movimentar/', movimentar_estoque, name='movimentar_estoque'),  # Movimentação de estoque
    path('estoque/movimentos/', lista_movimentos, name='lista_movimentos'),  # Listagem de movimentos de estoque
]
