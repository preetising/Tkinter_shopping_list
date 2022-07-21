from tkinter import*
from tkinter.font import BOLD
root = Tk()
root.title('Shopping_list')
root.geometry("500x500")

global my_label
my_label = Label(root, text=" Navgurukul Campus Group:--3 ").pack(pady=10)

my_Frame= Frame(root)
my_Frame.pack(pady=20)            #creating frame

my_list=Listbox(my_Frame,         #Putting list in the frame
bg="orange",
bd=0,
fg="black",
highlightthickness=0,
activestyle="none",
width=50,
height=20
)
my_list.pack(side=LEFT,fill=BOTH)

my_lists = ["Aata","sugar","bread","tea leaves ","maggie","fruits","mango","cherry"]
for _ in my_lists:
    my_list.insert(END,_)


## Create scrollbar


my_scrollbar = Scrollbar(my_Frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)      #add scrollbar
my_scrollbar.config(command=my_list.yview)

## To delete an item:

def delete():
    my_list.delete(ANCHOR)
    my_label.config(text=" ")

## To extra_add items:

extra_items=Entry(root,bg="white",fg="blue")
extra_items.pack(pady=10)
def add():
    my_list.insert(END,extra_items.get() )
    extra_items.delete(0,END)
    



my_button = Button(root,text="DELETE", bg="blue",command=delete).pack(pady=15)
my_button = Button(root,text="ADD" ,bg="blue",command=add).pack(pady=15)



root.mainloop()
