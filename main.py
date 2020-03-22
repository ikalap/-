#coding:gb2312
from tkinter import *


class gui(object):
    def __init__(self,master=None,*args,**kwargs):
        #����tk����
        self.root = Tk()
        self.x,self.y = 0,0
        self.bg = '#F8F8FF'
        self.font = ('Fixdsys',13)

        #�ĸ��ؼ�
        self.cha = Canvas(self.root,width=35,height=35,bg=self.bg,borderwidth=0)
        self.question = Label(self.root,text='��������ǲ�����?',font=self.font,bg=self.bg)
        self.yes = Button(self.root,text='�ǵ�',font=self.font,width=10,borderwidth=1,bg=self.bg)
        self.no = Button(self.root,text='����',font=self.font,width=10,borderwidth=1,bg=self.bg)

        self.set_root()
        self.set_widget()

        self.root.mainloop()

    def set_root(self):
        '''
        ����������
        '''
        self.root.overrideredirect(True)
        self.root.config(bg='#F8F8FF')

        w,h = 500,200
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        self.x = (ws//2) - (w//2)
        self.y = (hs//2) - (h//2)
        self.root.geometry(f'{w}x{h}+{self.x}+{self.y}')

    def set_widget(self):
        '''
        ��������Ŀؼ�
        '''
        def change_word(event):
            '''
            �������¼����ı䰴ť��ʾ���ı�
            '''
            print(f'����Enter�¼�,widget{event.widget["text"]}')
            a = event.widget['text']
            event.widget.config(bg='#7FFFAA')

            if a == '����':
                event.widget.config(text='�ǵ�')
                if self.yes is event.widget:
                    self.no.config(text='����')
                elif self.no is event.widget:
                    self.yes.config(text='����')

        s_n = 1
        def move(event):
            '''
            �ƶ����ǵİ�ť������s_n��ֵ��ֻ�ƶ����Σ�һ��һ��
            '''
            nonlocal s_n
            if s_n == 1:
                self.no.place(relx=0.7,rely=0.3)
                s_n += 1
            elif s_n == 2:
                self.no.place(relx=0.7,rely=0.7)
                self.no.unbind('<Enter>')
                self.no.bind('<Enter>',change_word)

        def change_end(event):
            '''
            ����뿪��ť������ɫ�ָ�
            '''
            event.widget.config(bg='#F8F8FF')

        def _top(string):
            '''
            �����ṩ�����Ӵ��ڵķ���
            '''
            t = Toplevel()
            t.geometry(f'400x150+{self.x}+{self.y}')
            #t.overrideredirect(True)
            t.config(bg='#F8F8FF')
            Label(t,text=string,font=self.font,bg=self.bg).place(relx=0.2,rely=0.15)
            def top_f(event):
                nonlocal t
                t.destroy()
            b = Button(t,text='ȷ��',font=self.font,bg=self.bg,width=10)
            b.bind('<Button-1>',top_f)
            b.place(relx=0.6,rely=0.65)


        def top(event):
            '''
            ������ı�Ϊ �ǵ� �İ�ť
            '''
            if event.widget['text'] == '�ǵ�':
                _top('��֪����ϲ����!')

        def cha_f(event):
            '''
            ����� �ر�
            '''
            _top('�رմ���Ҳ�ı䲻��\n��ϲ���ҵ���ʵ!')


        #�ռ���¼�
        self.yes.bind('<Enter>',change_word)
        self.no.bind('<Enter>',move)
        self.yes.bind('<Leave>',change_end)
        self.no.bind('<Leave>',change_end)
        self.yes.bind('<Button-1>',top)
        self.no.bind('<Button-1>',top)
        self.cha.bind('<Button-1>',cha_f)
        #���رյ�������
        self.cha.create_line(0,0,35,35,fill='#8B4513',width=2)
        self.cha.create_line(35,0,0,35,fill='#8B4513',width=2)
        #�ؼ�����
        self.cha.place(relx=0.85,rely=0.08)
        self.question.place(relx=0.15,rely=0.2)
        self.yes.place(relx=0.40,rely=0.7)
        self.no.place(relx=0.70,rely=0.7)

if __name__ == "__main__":
    a = gui()





