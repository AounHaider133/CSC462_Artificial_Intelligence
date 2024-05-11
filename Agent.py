
class Sensor:
    def __init__(self,percept):
        self.percept = percept
    
    def sense(self,env):
        if self.percept in env:
            return env
        else:
            return ""

class Agent:
    def __init__(self):
        self.sensor1 = Sensor("a")
        self.sensor2 = Sensor("what")
        self.sensor3 = Sensor("h")
        self.percept_table = []
    
    def sense(self,env):
        s1 = self.sensor1.sense(env)
        s2 = self.sensor2.sense(env)
        s3 = self.sensor3.sense(env)
        ctr = 0

        if s1:
            ctr = ctr + 1
        if s2:
            ctr = ctr + 1
        if s3:
            ctr = ctr + 1

        if ctr > 0:
            p = (env,ctr)
            self.percept_table.append(p)
            self.decision()
    
    def decision(self):
        sum = 0
        for i in self.percept_table:
            sum = sum + i[1]
        if sum > 10:
            self.actuator("reached")
            self.actuator("clear")
    def actuator(self,command):
        if command == "reached":
            print("You are a good Agent!")
        if command == "clear":
            self.percept_table = []


agent = Agent()
#env = input("Please enter a string:")
agent.sense("CUI Lahore")

print(agent.percept_table)