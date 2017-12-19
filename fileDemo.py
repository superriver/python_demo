import os
import re
import sys
class FileOption(object):
    global t
    t = '0'
    def operator(self):
        while True: 
            print("请选择要操作的类型:")
            print("0.文件")
            print("1.文件夹")
            print("当前路径:",os.getcwd())
            num = input("请选择操作码:")
            if num not in ['0','1']:
                print("只能选择0或1")
            else:
                self.select(num)

    def operatorDir(self):
        while True: 
            print("1.新建")
            print("2.删除")
            print("3.重命名")
            print("4.查找")
            print("5.切换目录")
            print("6.退出")
            num = input("请选择操作码:")
            if num == '4':
                self.find()
            if num == '6':
               sys.exit(0)
        
           

    def operatorFile(self):
        while True: 
            print("1.新建")
            print("2.删除")
            print("3.重命名")
            print("4.查找")
            print("5.编辑")
            print("6.退出")
            num = input("请选择操作码:")
            if num == '4':
                self.find()

            if num == '6':
                 sys.exit(0)

    def select(self,num):
        if num == '0':
              self.operatorFile()
        if num == '1':
              self.operatorDir()

    def rename(self):
        new = input("请输入新的文件名:")
        os.rename(old,new)

    def changeDir(self):
        name=input("请输入目录名:")
        os.chdir(name)
        
    def writeFile(self):
        filename=input("请输入文件名：")
        try:
            with open(os.path.join(os.getcwd(),filename),"w") as f:
                content=input("请输入内容：")
                f.write(content)
                print("写入成功")
        except:
            print("写入失败")
        finally:
            f.close()

    def readFile(self,filename):
        try:
            with open(os.path.join(os.getcwd(),filename),"r") as f:
                content = f.read()
                print("读取成功:"+content)
        except:
            print("读取失败")
        finally:
            f.close()
    
    def removeDir(self,path):
        os.removedirs(path)

    def create(self):
        if t == '0':

        if t == '1':
            name=input("请输入新建的文件夹名:")
            path = os.join(os.getcwd(),name)
            if os.path.exists(path):
                print(path)
            
            else:
                os.mkdir(path)
                print
                ("文件夹创建成功")
            self.writeFile()
     

    def find(self):
         if t == '0':
            filelist = [name for name in os.listdir('.') if os.path.isfile(name)]
            for name in filelist:
                print(name)
         if t == '1':
            dirlist = [name for name in os.listdir('.') if os.path.isdir(name)]
            for name in dirlist:
                print(name)
      
                
    def printPath(self,rootPath):
        if os.path.isdir(rootPath):
            for name in os.listdir(rootPath):
                filePath = os.path.join(rootPath,name)
                regex=r".*\.txt$"
                if re.match(regex,name):
                     print('文件的路径%s和文件名%s'%(filePath,name))
               
                if os.path.isdir(filePath):
                    print(filePath)
                    self.printPath(filePath)
                
        else:
             print(self.dirPath)

    def getcwd(self):
        print(os.getcwd())

if __name__=='__main__':
  
   
    file = FileOption()
    file.operator()
    #file.printPath("E:\\Python")
   
   
