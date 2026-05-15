import tkinter as tk
from PIL import Image, ImageTk

def abrir_tela_morte():
    root = tk.Tk()
    
    # Remove bordas, barra de título e botões do sistema
    root.overrideredirect(True)
    
    # Detecta a resolução exata do monitor
    largura = root.winfo_screenwidth()
    altura = root.winfo_screenheight()
    root.geometry(f"{largura}x{altura}+0+0")
    
    # Força a janela a ficar sobreposta a qualquer outro app
    root.attributes("-topmost", True)
    root.focus_force()
    
    try:
        # Tenta carregar e redimensionar a imagem realista
        imagem_original = Image.open("bsod1.png")
        imagem_redimensionada = imagem_original.resize((largura, altura), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(imagem_redimensionada)
        
        label = tk.Label(root, image=foto, bd=0, highlightthickness=0)
        label.image = foto  # Mantém a referência na memória
        label.pack(fill="both", expand=True)
        
    except FileNotFoundError:
        # Fallback: Cria a tela em texto criada anteriormente caso a foto suma
        root.configure(bg="#0000AA")
        
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

    # Fecha o script imediatamente ao pressionar a tecla 'q' (minúscula ou maiúscula)
    root.bind("<Key-q>", lambda e: root.destroy())
    root.bind("<Key-Q>", lambda e: root.destroy())

    root.mainloop()

if __name__ == "__main__":
    abrir_tela_morte()
