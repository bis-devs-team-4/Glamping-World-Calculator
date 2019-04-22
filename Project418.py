from tkinter import * # tkinter import

class ProcessOrder:
    def __init__(self):
        self.window = Tk()
        self.window.title('Glamping World Order Processing Application')
        photo = PhotoImage(file="P:\GWlogo.gif") # specify the path to your file
        label = Label(self.window, image=photo)  #put the image in a label to display it in the window
        label.grid()  # show the label on the screen

        Label(self.window, text ="Customer Name:").grid(sticky = W, column = 0, row = 1)
        self.CustomerNameVar = StringVar()
        Entry(self.window, textvariable = self.CustomerNameVar, justify = LEFT).grid(sticky = W, column = 1, row = 1)
        Label(self.window, text= "Product Name:").grid(sticky = W, column = 0, row = 2)
        self.ProductNameVar = StringVar()
        Entry(self.window, textvariable = self.ProductNameVar, justify= LEFT).grid(column = 1, row = 2)
        Label(self.window, text ="Product Quantity:").grid(sticky = W, column = 0, row = 3)
        self.ProductQuantityVar = StringVar()
        Entry(self.window, textvariable = self.ProductQuantityVar, justify = LEFT).grid(column = 1, row = 3)
        Label(self.window, text ="Product Price:").grid(sticky = W, column = 0, row = 4)
        self.ProductPriceVar = StringVar()
        Entry(self.window, textvariable = self.ProductPriceVar, justify = LEFT).grid(column = 1, row = 4)

        # set up outputs for the order application
        self.SubTotalVar = StringVar()
        Label(self.window, textvariable = self.SubTotalVar).grid(column = 2, row = 4, sticky = E)
        Button(self.window, text = "Subtotal", command = self.Subtotal).grid(column = 2, row = 6, sticky = E)
        self.TotalVar = StringVar()
        Label(self.window, text = self.Total).grid(column = 2, row = 5, sticky = E)
        Button(self.window, text = "Total", command = self.Total).grid(column = 2, row = 7, sticky = E)
        self.window.mainloop()

    def CalculateSubtotal(self, ProductPriceVar, ProductQuantityVar):
        ProductPriceVar = 0
        ProductQuantityVar = 0
        ProductPriceVar = float(ProductPriceVar.get()
        ProductQuantityVar = int(ProductQuantityVar.get()
        Label(self.window, text = "Subtotal: {10.2f}".format(Subtotal).grid(column = 1, row = 8, sticky = W))
        
    def Subtotal(self):
        Subtotal = 0
        for ProductNameVar in self:
            Subtotal = self.ProductQuantityVar * self.ProductPriceVar
        return Subtotal
    

    def CalculateTotal (self):
        OrderTotal = self.getOrderTotal(
            float(self.Subtotal))
        Label(self.window, text = "Order Total: {10.2f}".format(Total).grid(sticky = W, column = 1, row = 9))
        self.Total = Total

    def Total(self, Subtotal):
        Total = Subtotal * .13
        return Total

ProcessOrder()
    

        
        

        

