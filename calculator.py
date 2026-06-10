class statistic_calculator():

  def __init__(self,data):
    self.data = data

  def mean(self):
    total = 0
    for num in self.data:
        total += num
    x = total / len(self.data)
    print("mean :",x)

  def median(self):
    self.data.sort()
    n = len(self.data)
    if n % 2 != 0:
     median_value = self.data[n//2]
     
    else:
     median_value =(self.data[n//2-1] + self.data[n//2])/2

    print("median : ",median_value )

  def mode(self):
    frequency = {}
    for num in self.data:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_frequency = max(frequency.values())
    for key,value in frequency.items():
     if value == max_frequency:

      print("mode :",key ) 


data = list(map(int, input("Enter elements: ").split()))

obj = statistic_calculator(data)

while True:
  print("1. Mean")
  print("2. Mode")
  print("3. median")
  print("4. Exit")

  Choice = int(input("Enter the Choice : "))
  if Choice == 1:
   obj.mean()
  elif Choice == 2:
    obj.mode()
  elif Choice == 3:
    obj.median()
  
  elif Choice == 4:
    break

  else:
    print('invalid choice')
