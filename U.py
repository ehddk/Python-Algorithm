print("1. 10초   2.30초   3.1분   4.10분   5.시작")
time=0
while True:
  n=int(input("원하는 버튼의 숫자를 입력 : "))
  if n == 1:
    time += 10
  elif n == 2:
    time += 30
  elif n == 3:
    time += 60
  elif n == 4:
    time += 600
  elif n == 5:
    print("전자레인지를 작동합니다.")
    break
  else:
    print("잘못 입력하였습니다.")
  
  sec=time
  if sec>=60:
    min = sec// 60 #몫
    sec= time-(min*60)
    print(min,end=":")
  if time<60:
    print("00",end=":")
  if sec!=0:
    print(str(sec))
  if sec==0:
    print("00")
