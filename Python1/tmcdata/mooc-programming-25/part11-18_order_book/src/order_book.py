# Write your solution here:
class Task:
    idseed = 1
    def __init__(self, description: str, name: str, hours: int):
        self.description = description
        self.programmer = name
        self.workload = hours
        self.status = "NOT FINISHED"
        self.id = Task.idseed
        Task.idseed += 1
    
    def is_finished(self):
        return self.status == "FINISHED"

    def mark_finished(self):
        self.status = "FINISHED"

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.status}"

class OrderBook:
    def __init__(self):
        self.orders = []
        self.programmer = []

    def add_order(self, description: str, name: str, hours: int):
        task = Task(description, name, hours)
        self.orders.append(task)
        if name not in self.programmer:
            self.programmer.append(name)

    def all_orders(self):
        return self.orders

    def programmers(self):
        return self.programmer

    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError("{id} doesn't exist")
    
    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]
    
    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]

    def status_of_programmer(self, programmer: str):
        fcount = len([f.workload for f in self.finished_orders() if f.programmer == programmer]) 
        fhours = sum([f.workload for f in self.finished_orders() if f.programmer == programmer])
        ccount = len([f.workload for f in self.unfinished_orders() if f.programmer == programmer])   
        ufhours = sum([f.workload for f in self.unfinished_orders() if f.programmer == programmer])   

        if fhours == 0 and ufhours == 0:
            raise ValueError("not exist")

        return (fcount, ccount, fhours, ufhours)


if __name__=="__main__":
    t = OrderBook()
    t.add_order("program webstore", "Andy", 10)
    t.add_order("program mobile app", "Andy", 5)
    t.add_order("program something with pygame", "Andy", 50)
    t.add_order("code better facebook", "Jonas", 5000)
    t.mark_finished(1)
    t.mark_finished(2)
    # for m in t.all_orders():
    #     print(m)
    print(t.status_of_programmer("Andy"))
