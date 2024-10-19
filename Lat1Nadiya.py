import PySimpleGUI as sg
window = sg.Window(title="Profile",layout=[
    [sg.Text("NPM    : 2710010045")],
    [sg.Text("Nama   : Nadiya Izzaty Rahman")],
    [sg.Text("Kelas  : 5A Non Reguler Banjarmasin")],
    [sg.Text("Matkul : Pemrograman Visual 3")],
    
    ],size=(400,200) )
window()
window.close()