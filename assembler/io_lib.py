from SingletonMeta import SingletonMeta

class IO(metaclass=SingletonMeta):
    openFiles = []

    def readFileIntoLines(self, file_name):
        f = open(file_name, 'r')
        self.openFiles.append(f)
        return f.readlines()
    
    def writeLineToFile(self, file_name, lines):
        f = open(file_name, 'w')
        f.writelines(lines)
    
    def closeOpenFiles(self):
        [f.close() for f in self.openFiles]