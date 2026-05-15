Set WshShell = CreateObject("WScript.Shell")

' Define o atalho para fechar
closeKey = "CTRL+SHIFT+X"

' Cria um loop infinito
Do
    x = MsgBox("I Love You!", 1 + 16, "Attention")

    ' Verifica se o atalho foi pressionado
    If WshShell.AppActivate("Attention") Then
        If WshShell.Popup("Pressione " & closeKey & " para fechar.", 1, "Info", 64) Then
        End If
    End If

    ' Detecta tecla
    If GetAsyncKeyState(vbKeyX) <> 0 Then
        If WshShell.Popup("Fechando...", 1, "Saindo", 64) Then
            Exit Do
        End If
    End If
Loop

' Função para detectar tecla
Function GetAsyncKeyState(Key)
    Set obj = CreateObject("WScript.Shell")
    GetAsyncKeyState = obj.SendKeys("")
End Function
