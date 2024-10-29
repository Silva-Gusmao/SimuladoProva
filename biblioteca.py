def cadastrarLivrosExemplo():
    exemploLivros = [
        {"Título": "Livro A", "Autor": "Autor A", "Editora": "Editora A", "Ano": "2020", "Gênero": "Ficção", "Idioma": "Português", "ISBN": "1234567890", "Páginas": "300", "Formato": "Digital", "Localização": "Estante 1"},
        {"Título": "Livro B", "Autor": "Autor B", "Editora": "Editora B", "Ano": "2019", "Gênero": "Romance", "Idioma": "Inglês", "ISBN": "1234567891", "Páginas": "200", "Formato": "Impresso", "Localização": "Estante 2"},
        {"Título": "Livro C", "Autor": "Autor C", "Editora": "Editora C", "Ano": "2018", "Gênero": "História", "Idioma": "Espanhol", "ISBN": "1234567892", "Páginas": "150", "Formato": "Digital", "Localização": "Estante 3"},
        {"Título": "Livro D", "Autor": "Autor D", "Editora": "Editora D", "Ano": "2021", "Gênero": "Ciência", "Idioma": "Português", "ISBN": "1234567893", "Páginas": "400", "Formato": "Impresso", "Localização": "Estante 4"},
        {"Título": "Livro E", "Autor": "Autor E", "Editora": "Editora E", "Ano": "2022", "Gênero": "Arte", "Idioma": "Francês", "ISBN": "1234567894", "Páginas": "350", "Formato": "Digital", "Localização": "Estante 5"}
    ]
    for livro in exemploLivros:
        adicionarLivro(livro)

import tkinter as tk
from funcoes import listarLivros, adicionarLivro, excluirLivro, exibirLivroDetalhes, alterarLivro

def iniciarBiblioteca():
    global bibliotecaWindow, frameConteudo
    bibliotecaWindow = tk.Tk()
    bibliotecaWindow.title("Internoteca")

    menuPrincipal = tk.Menu(bibliotecaWindow)

    menuCadastro = tk.Menu(menuPrincipal, tearoff=0)
    menuCadastro.add_command(label="Cadastrar Livro", command=abrirCadastroLivro)
    menuPrincipal.add_cascade(label="Cadastro", menu=menuCadastro)

    menuListagem = tk.Menu(menuPrincipal, tearoff=0)
    menuListagem.add_command(label="Listar Livros", command=exibirLivros)
    menuPrincipal.add_cascade(label="Listar", menu=menuListagem)

    bibliotecaWindow.config(menu=menuPrincipal)

    frameConteudo = tk.Frame(bibliotecaWindow)
    frameConteudo.pack(fill="both", expand=True)

    exibirLivros()
    bibliotecaWindow.mainloop()

def exibirLivros():
    limparFrame()
    tk.Label(frameConteudo, text="Livros Cadastrados", font=("Arial", 16)).pack(pady=10)
    livros = listarLivros()

    if livros:
        for idx, livro in enumerate(livros):
            frameLivro = tk.Frame(frameConteudo)
            frameLivro.pack(fill="x", padx=10, pady=5)

            tk.Label(frameLivro, text=livro['Título'], anchor="w").pack(side="left")

            tk.Button(frameLivro, text="Exibir", command=lambda idx=idx: exibirLivroDetalhes(idx)).pack(side="right", padx=5)
            tk.Button(frameLivro, text="Excluir", command=lambda idx=idx: excluirLivro(idx, exibirLivros)).pack(side="right", padx=5)
            tk.Button(frameLivro, text="Alterar", command=lambda idx=idx: abrirAlterarLivro(idx)).pack(side="right", padx=5)
    else:
        tk.Label(frameConteudo, text="Nenhum livro cadastrado.").pack(pady=10)

def abrirCadastroLivro():
    limparFrame()
    tk.Label(frameConteudo, text="Cadastro de Livro", font=("Arial", 16)).pack(pady=10)

    campos = [
        "Título", "Autor", "Editora", "Ano", "Gênero",
        "Idioma", "ISBN", "Páginas", "Formato", "Localização"
    ]

    entradas = {}
    for campo in campos:
        tk.Label(frameConteudo, text=f"{campo}:").pack(pady=2)
        entrada = tk.Entry(frameConteudo)
        entrada.pack(pady=2)
        entradas[campo] = entrada

    def salvarLivro():
        dadosLivro = {campo: entrada.get() for campo, entrada in entradas.items()}
        adicionarLivro(dadosLivro)
        exibirLivros()

    tk.Button(frameConteudo, text="Salvar Livro", command=salvarLivro).pack(pady=10)

def abrirAlterarLivro(idx):
    limparFrame()
    tk.Label(frameConteudo, text="Alterar Livro", font=("Arial", 16)).pack(pady=10)

    livro = listarLivros()[idx]

    campos = [
        "Título", "Autor", "Editora", "Ano", "Gênero",
        "Idioma", "ISBN", "Páginas", "Formato", "Localização"
    ]

    entradas = {}
    for campo in campos:
        tk.Label(frameConteudo, text=f"{campo}:").pack(pady=2)
        entrada = tk.Entry(frameConteudo)
        entrada.pack(pady=2)
        entrada.insert(0, livro[campo])
        entradas[campo] = entrada

    tk.Button(frameConteudo, text="Salvar Alterações", command=lambda: salvarAlteracoes(idx, entradas)).pack(pady=10)

def salvarAlteracoes(idx, entradas):
    novosDados = {campo: entrada.get() for campo, entrada in entradas.items()}
    alterarLivro(idx, novosDados)
    exibirLivros()

def limparFrame():
    for widget in frameConteudo.winfo_children():
        widget.destroy()