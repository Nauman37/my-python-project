class robot:
    def __init__(self,name,x=0,y=0,battery=30):
        self.name="eren"
        self.x=x
        self.y=y
        self.battery=battery
    def move(self,direction,steps):
        if self.battery<=0:
            print("robot has no battery left! charge first.")
            return
        battery_needed=steps*2
        if self.battery<battery_needed:
            print("robot does not have enough battery to move ")
            return
        direction=direction.lower()
        if direction == 'up':
            self.y+=steps
        elif direction =='down':
            self.y-=steps
        elif direction == 'left':
            self.x-=steps
        elif direction == 'right':
            self.x+=steps
        else:
            print("invalid direction")
            return

        self.battery-=battery_needed
        
        print(f"Moved {steps} steps {direction}. Battery: {self.battery}%. Position: ({self.x}, {self.y})")

    def charge_battery(self,amount):
        self.battery=min(100,self.battery+amount)
        print(f"robot charged. battery level: {self.battery}")

class AI_robot(robot):
    def move(self,direction,steps):
        if self.battery<10:
            self.auto_charge()
        battery_needed=steps*2
        if self.battery<battery_needed:
            print("robot does not have enough battery to move {steps} steps!")
            return
        
        super().move(direction,steps)

    def auto_charge(self):
        print("robot has low battery! auto charging...")
        self.charge_battery(50)

r1 =robot("Nauman") #test cases
r1.move("up", 10)   
r1.charge_battery(80)
r1.move("left", 20) #tst cases

