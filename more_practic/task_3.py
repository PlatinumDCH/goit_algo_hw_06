class Calculator:
    
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(num1,num2):
        return num1 * num2
    def divide(self,num1,num2):
        if num2 == 0:
            return "Error: division by zero"
        else:
            return num1 / num2
        