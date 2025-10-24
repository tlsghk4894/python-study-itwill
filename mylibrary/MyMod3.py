class Calc:
    def plus(self, x, y):
        return x + y
    
    def minus(self, x, y):
        return x - y
    
my_calc = Calc()

# 테스트 코드
if __name__ == "__main__":
    print(my_calc.plus(10, 20),my_calc.minus(10, 20))