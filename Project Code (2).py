from tkinter import * # tkinter import

class ProcessOrder:
    def __init__(self):
        self.window = Tk()
        self.window.title('Glamping World Order Processing Application')
        photo = PhotoImage(file="P:\GWlogo.gif") # specify the path to your file
        label = Label(self.window, image=photo)  #put the image in a label to disdaply it in the window
        label.grid()  # show the label on the screen

        Label(self.window, text ="Customer Name:")
        label.grid(sticky = W, column = 0, row = 0)
        text = Entry(self.window, width = 35)
        text.grid(column=1, row=0)
        Label(self.window, text= "Product Name:")
        label.grid(sticky = W, column = 0, row = 1)
        text = Entry(self.window, width = 35)
        text.grid(column=1, row=1)
        Label(self.window, text ="Product Quantity:")
        label.grid(sticky = W, column = 0, row = 2)
        text = Entry(self.window, width = 35)
        text.grid(column=1, row=2)
        Label(self.window, text ="Product Price:")
        label.grid(sticky = W, column = 0, row = 3)
        text = Entry(self.window, width = 35)
        text.grid(column=1, row=3)

        # set up inputs for the order application
        self.CustomerNameVar = StringVar()
        Entry(self.window, textvariable = self.CustomerNameVar).grid(sticky = W, column = 1, row = 2)
        self.ProductNameVar = StringVar()
        Entry(self.window, textvariable = self.ProductName, justify= RIGHT).grid(column = 1, row = 3)
        self.ProductPriceVar = StringVar()
        Entry(self.window, textvariable = self.ProductPrice, justify = RIGHT).grid(column = 1, row = 4)
        self.ProductQuantityVar = StringVar()
        Entry(self.window, textvariable = self.ProductQuantity, justify = RIGHT).grid(column = 1, row = 5)

        # set up outputs for the order application
        self.SubTotalVar = StringVar()
        Label(window, textvariable = self.SubTotal).grid(column = 2, row = 4, sticky = E)
        self.TotalVar = StringVar()
        Label(window, text = self.Total).grid(column = 2, row = 5, sticky = E)
        Button(window, text = "Subtotal", command = self.Subtotal).grid(column = 2, row = 6, sticky = E)
        Button(window, text = "Total", command = self.Total).grid(column = 2, row = 7, sticky = E)
        self.window.mainloop()

    def CalculateSubtotal(self):
        Subtotal = self.getSubtotal(
            float(self.ProductPriceVar.get()),
            int(self.ProductQuantityVar.get()))
        self.SubTotal = SubTotal
        Label(self.window, text = "Subtotal: {10.2f}".format(Subtotal).grid(column = 1, row = 8, sticky = W)
    
    def Subtotal(self, subtotal):
        Subtotal = ProductQuantity * ProductPrice
        return Subtotal

    def CalculateTotal (self):
        OrderTotal = self.getOrderTotal(
            float(self.Subtotal)
        Label(self.window, text = "Order Total: {10.2f}".format(Total).grid(sticky = W, column = 1, row = 9))
        self.Total = Total

    def Total(self, Subtotal):
        Total = Subtotal + Subtotal
        return Total


        

        
        

        

