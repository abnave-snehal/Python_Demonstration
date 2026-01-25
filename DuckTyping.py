# Duck Typing : It is a concept where the type of an object is determined by it's behaviour

# not by it's class


class InkjetPrinter:
    def printdocument(self,docuemnt):
        print("Inkjet Printer printing : ",docuemnt)

class LaserPrinter:
    def printdocument(self,docuemnt):
        print("Laser Printer printing : ",docuemnt)

class PDFWriter:
    def printdocument(self,docuemnt):
        print(f"Saving {docuemnt} as PDF")


def StartPrinting(device):
    device.printdocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()