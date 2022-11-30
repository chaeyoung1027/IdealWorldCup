import tkinter  # GUI 모듈

# 윈도우 생성
window = tkinter.Tk()
window.title("IdealWorldCup")
window.geometry("1000x650+100+100")  # 가로 x 세로 + x좌표 + y좌표
window.resizable(False, False)  # 상하, 좌우 창 크기 조절 가능 여부

background_image = tkinter.PhotoImage(file="images/c.png")  # 임의
label1 = tkinter.Label(window, image=background_image)
label1.pack()

label = tkinter.Label(window, text='이상형 월드컵', font=('맑은 고딕', 30))
label.place(x=400, y=50)

start_button = tkinter.Button(window, text="시작하기", foreground="brown2", background="snow", overrelief="groove", width=10, height=2).place(x=400, y=500)
ranking_button = tkinter.Button(window, text="랭킹보기", foreground="orange", background="snow", overrelief="groove", width=10, height=2).place(x=500, y=500)

window.mainloop()
