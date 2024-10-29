from tkinter import messagebox

# Funções para manipulação de livros
livros = []  # Armazenamento temporário de livros em uma lista

def listarLivros():
    return livros 

def adicionarLivro(livro):
    livros.append(livro)

def excluirLivro(idx, callback):
    if 0 <= idx < len(livros):
        del livros[idx]
        callback()  # Atualiza a exibição dos livros

def exibirLivroDetalhes(idx):
    if 0 <= idx < len(livros):
        livro = livros[idx]
        detalhes = "\n".join(f"{campo}: {valor}" for campo, valor in livro.items())
        messagebox.showinfo("Detalhes do Livro", detalhes)

def validarUsuario(usuario, senha):
    return usuario == "l" and senha == "a"

def alterarLivro(idx, novosDados):
    if 0 <= idx < len(livros):
        livros[idx].update(novosDados)