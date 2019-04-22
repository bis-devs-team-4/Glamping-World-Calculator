from tkinter import * # tkinter import

class ProcessOrder:
    def __init__(self):
        self.window = Tk()
        self.window.title('Glamping World Order Processing Application')

        # set up the inputs for the order application

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
        Label(self.window, text = "Subtotal($):").grid(sticky = W, column = 0, row = 5)
        Label(self.window, text = "Sales Tax(13%):").grid(sticky = W, column = 0, row = 6)
        Label(self.window, text = "Total($):").grid(sticky = W, column = 0, row = 7)
        Checkbutton(self.window, text = "Pick up").grid(sticky = W, column = 0, row = 8)
        Checkbutton(self.window, text = "Delivery").grid(sticky = W, column = 1, row = 8)

        # set up outputs for the order application
        self.SubTotalVar = StringVar()
        Label(self.window, textvariable = self.SubTotalVar).grid(column = 1, row = 5)
        self.TotalVar = StringVar()
        Label(self.window, textvariable = self.TotalVar).grid(column = 1, row =7)
        self.SalesTaxVar = StringVar()
        Label(self.window, textvariable = self.SalesTaxVar).grid(column = 1, row = 6)
        Button(self.window, text = "Calculate Total", command = self.CalculateSubTotal).grid(column = 2, row = 10, sticky = E)
        self.window.mainloop()

         

    def CalculateSubTotal(self):
        SubTotal = self.getSubTotal(
            float(self.ProductPriceVar.get()),
            int(self.ProductQuantityVar.get()))
            
        self.SubTotalVar.set(format(SubTotal, '10.2f'))
        SalesTax = self.getSalesTax(
            float(self.SubTotalVar.get()))

        self.SalesTaxVar.set(format(SalesTax, '10.2f'))
        Total = float(self.SubTotalVar.get()) + float(self.SalesTaxVar.get())
        self.TotalVar.set(format(Total, '10.2f'))
        
        
    def getSubTotal(self, ProductPrice, ProductQuantity):
        SubTotal = (ProductPrice * ProductQuantity)
        return SubTotal

    def getSalesTax(self, SubTotal):
        SalesTax = (SubTotal * 0.13)
        return SalesTax

    
    

ProcessOrder()
    

        
        

        

