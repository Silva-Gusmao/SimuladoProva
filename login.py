import tkinter as tk
from tkinter import messagebox
from biblioteca import iniciarBiblioteca, cadastrarLivrosExemplo
from funcoes import validarUsuario

def iniciarLogin():
    loginWindow = tk.Tk()
    loginWindow.title("Bem-vindo à Biblioteca")

    tk.Label(loginWindow, text="Usuário:").pack(pady=5)
    entradaUsuario = tk.Entry(loginWindow)
    entradaUsuario.pack(pady=5)

    tk.Label(loginWindow, text="Senha:").pack(pady=5)
    entradaSenha = tk.Entry(loginWindow, show="*")
    entradaSenha.pack(pady=5)

    def realizarLogin():
        usuario = entradaUsuario.get()
        senha = entradaSenha.get()
        if validarUsuario(usuario, senha):
            cadastrarLivrosExemplo()  # Adiciona os livros de exemplo
            loginWindow.destroy()
            iniciarBiblioteca()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    tk.Button(loginWindow, text="Login", command=realizarLogin).pack(pady=20)
    loginWindow.mainloop()