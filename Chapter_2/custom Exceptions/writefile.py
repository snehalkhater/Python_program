class filehandler:
    def writefile(self):
        try :
            file = open("D:\Python_33\Chapter_2\Exception\sample.txt", "a")
            data = file.write("Mca 1st year student ")
            print(data)
        except FileNotFoundError:
            print("File is not found")
        except PermissionError:
            print("permission denied")
        except Exception as e:
            print(e)
        finally:
            file.close()
obj = filehandler()
obj.writefile()
