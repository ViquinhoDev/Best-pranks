import tkinter as tk

def criar_tela_morte():
    root = tk.Tk()
    
    # Remove as bordas da janela e os botões de fechar/minimizar
    root.overrideredirect(True)
    
    # Força a janela a ocupar toda a resolução da tela
    largura = root.winfo_screenwidth()
    altura = root.winfo_screenheight()
    root.geometry(f"{largura}x{altura}+0+0")
    
    # Mantém a janela sempre no topo e foca o cursor nela
    root.attributes("-topmost", True)
    root.focus_force()
    
    # Fundo azul característico da tela da morte
    root.configure(bg="#0000AA")

    # Mensagem clássica de erro (você pode personalizar)
    texto_erro = (
        "Um problema foi detectado e o Windows foi desligado para evitar danos\n"
        "ao seu computador.\n\n"
        "O problema parece ser causado pelo seguinte arquivo: ntoskrnl.exe\n\n"
        "PAGE_FAULT_IN_NONPAGED_AREA\n\n"
        "Informações técnicas:\n"
        "*** STOP: 0x00000050 (0xFD3094C2, 0x00000001, 0xFBFE7617, 0x00000000)\n\n"
        "*** ntoskrnl.exe - Address 0xFBFE7617 base at 0xFBFC0000 DateStamp 0x3d6dd67c"
    )

    label = tk.Label(
        root, 
        text=texto_erro, 
        fg="white", 
        bg="#0000AA", 
        font=("Consolas", 18), 
        justify="left"
    )
    label.pack(expand=True)

    # Permite fechar a pegadinha pressionando a tecla 'q'
    root.bind("<q>", lambda e: root.destroy())

    root.mainloop()

if __name__ == "__main__":
    criar_tela_morte()
