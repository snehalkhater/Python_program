class filehandler:
    def readfile(self):
        try :
            file = open("D:\Python_33\Chapter_2\Exception\sample.txt", "r")
            data = file.read()
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
obj.readfile()
