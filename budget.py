class Category:
  
  #instantiation of the object based on different budget categories.

    def __init__(self,name) :
        self.name = name
        self.ledger = []
        self.funds = 0
        self.dct = {}
        self.withd = 0

    #the deposit method.

    def deposit(self,amount,description="") :
        self.ledger.append({"amount": amount, "description": description})
        self.funds = amount + self.funds
        self.dct.update({description:amount})

    #the withdraw method.

    def withdraw(self,amount,description="") :
        if amount < self.funds :
            self.ledger.append({"amount": -amount, "description": description})
            self.funds = self.funds - amount
            self.dct.update({description:-amount})
            self.withd = self.withd + amount

            return(True)
        else :
            return(False)
    
    #the get_balance method.
    
    def get_balance(self) :
        return(self.funds)

    #the transfer method.

    def transfer(self,amount,other_instance) :
        if self.funds > amount :
            self.withdraw(amount,f"Transfer to {other_instance.name}")
            other_instance.deposit(amount,f"Transfer from {self.name}")
            return(True)
        else :
            return(False)

    #the check_funds method.

    def check_funds(self,amount) :
        if amount > self.funds :
            return(False)
        else :
            return(True)

    #string.
    def __str__(self):
        max_width = 30
        stars_width = max_width - len(self.name)
        stars_width ="*" * int(stars_width / 2)
        line1 = f"{stars_width}{self.name}{stars_width}"
        count = 0
        lst = []
        for dsc,amnt in self.dct.items():
            count = count + 1
            max_dsc = dsc[:23]
            amnt = str("{:.2f}".format(float(amnt)))
            meow = f"{max_dsc}{amnt.rjust(max_width - len(max_dsc))}"
            lst.append(meow)
        if count == 0 :
            return(f"{line1}")
        elif count == 1 :
            return(f"{line1}\n{lst[0]}\nTotal: {self.funds}")
        elif count == 2 :
            return(f"{line1}\n{lst[0]}\n{lst[1]}\nTotal: {self.funds}")
        elif count == 3 :
            return(f"{line1}\n{lst[0]}\n{lst[1]}\n{lst[2]}\nTotal: {self.funds}")
        elif count == 4 :
            return(f"{line1}\n{lst[0]}\n{lst[1]}\n{lst[2]}\n{lst[3]}\nTotal: {self.funds}")
        
        
#hell in a form of code :

def create_spend_chart (categories) :

    #getting the rounded percentages.

    abs_total = 0
    cat_total = {}
    percentages = {}
    for category in categories :
        abs_total = abs_total + category.withd
        cat_total[category.name] = category.withd
    for k,v in cat_total.items() :
        percentages[k] =v * 100 / abs_total

    #Percentage spent by category.

    s="Percentage spent by category\n"

    #the o thing.

    for h in range(100,-1,-10) :
        hh = f"{h}|"
        hh = hh.rjust(4)
        for value in percentages.values() : 
            if value >= h :
                hh += " o "
            elif value < h :
                hh+="   "
        s += f"{hh}\n"
        
    #the dashes.

    line1="    -"
    for category in categories :
        line1 = line1+"---"
    s += f"{line1}\n"

    #the vertical categos names (hardest part ong).

    count = 0
    index = 0
    p = ""
    for i in range(max(len(key)for key in percentages.keys())) :
        count = count + 1
        for key in percentages.keys():
            try:
                p += f"{key[index]}  "
            except IndexError:
                p += "   "
        index = index + 1
        if count != max(len(key)for key in percentages.keys()) :
            s += f"     {p}\n"
        else :
            s += f"     {p}"
        p = ""
    return(s)
