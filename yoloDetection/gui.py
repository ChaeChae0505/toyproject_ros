
#python detect.py --img 640 --data data/Sejong.yaml --weights runs/train/sejong_batch010203_rev1/weights/best.pt --name sejong_batch010203_rev1 --save-txt\
#                 --source /home/a307/Sejong/AutoLabeling/dataset/Batch010203_rev1/val/images


#python detect.py --img 640 --data data/Sejong.yaml --weights runs/train/sejong_batch010203_rev1/weights/best.pt --name sejong_batch010203_rev1 --save-txt\
#                 --source /home/a307/Sejong/AutoLabeling/dataset/Batch010203_rev1/val/images


from tkinter import *
from tkinter import filedialog
import tkinter
import tkinter.font
import subprocess


size = "640"
# dataload = "data/Sejong.yaml"
# ptfile = "runs/train/sejong_batch010203_rev1/weights/best.pt"
# sourcefile = "/home/a307/Sejong/AutoLabeling/dataset/Batch010203_rev1/val/images"
    

def Load_pt(txt_dest_path):
    filename = filedialog.askopenfilename(initialdir="../", title="Select file",
                                          filetypes=((".pt file open", "*.pt"),
                                          ("all files", "*.*")))
    if filename is None: # 사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, filename)
    print(filename)

def Load_yaml(txt_dest_path):
    filename = filedialog.askopenfilename(initialdir="../", title="Select file",
                                          filetypes=((".yaml file open", "*.yaml"),
                                          ("all files", "*.*")))
    if filename is None: # 사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, filename)
    print(filename)

def domenu():
    print("OK")

def path(): # path load
    filename = filedialog.askdirectory();
    print(filename)
    
    return filename

# 저장 경로 (폴더)
def browse_dest_path(txt_dest_path):
    folder_selected = filedialog.askdirectory(initialdir="../",)
    if folder_selected is None: # 사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)
    return folder_selected


# 시작
def start(yolo):
    # 각 옵션들 값을 확인
    sp = subprocess.call(yolo, stdout=subprocess.PIPE, shell=True)




root = Tk()
font=tkinter.font.Font(family="맑은 고딕", size=30, slant="italic")

# 저장 경로 프레임
path_frame1 = LabelFrame(root, text="File load(.yaml)")
path_frame1.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path1 = Entry(path_frame1)
txt_dest_path1.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_dest_path1 = Button(path_frame1, text="Search", width=10, command=lambda : Load_yaml(txt_dest_path1))
result_yaml = btn_dest_path1.pack(side="right", padx=5, pady=5)


# 저장 경로 프레임
path_frame2 = LabelFrame(root, text="File load(.pt)")
path_frame2.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path2 = Entry(path_frame2)
txt_dest_path2.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_dest_path2 = Button(path_frame2, text="Search", width=10, command=lambda : Load_pt(txt_dest_path2))
result_pt = btn_dest_path2.pack(side="right", padx=5, pady=5)

# 저장 경로 프레임
path_frame3 = LabelFrame(root, text="Source directory")
path_frame3.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path3 = Entry(path_frame3)
txt_dest_path3.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_dest_path3 = Button(path_frame3, text="Search", width=10, command=lambda : browse_dest_path(txt_dest_path3))
result_dir = btn_dest_path3.pack(side="right", padx=5, pady=5)

dataload = result_yaml
ptfile = result_pt
sourcefile = result_dir

if dataload or ptfile or sourcefile is None:
    yolo = "python detect.py --img 640 --data data/Sejong.yaml --weights runs/train/sejong_batch010203_rev1/weights/best.pt --name sejong_batch010203_rev1 --save-txt\
         --source /home/a307/Sejong/AutoLabeling/dataset/Batch010203_rev1/val/images"
else:
    yolo = "python detect.py"\
        +" " + "--img"+" "+size \
        +" "+"--data"+" "+dataload\
        +" "+"--weights"+" "+ptfile+" "+"--name"+" "+"sejong_batch010203_rev1"\
        +" "+"--save-txt"\
        +" "+"--source"+" "+sourcefile

print(yolo)
# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12, command=lambda : start(yolo))
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()

