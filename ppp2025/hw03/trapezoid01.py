base_up = int(input("윗변을 입력하세요"))
base_down = int(input("밑변을 입력하세요"))
height = int(input("높이를 입력하세요"))

area = (base_down + base_up) / 2 * height

print("윗변={}, 아랫변={}, 높이 ={} 일 때".format(base_down, base_up, height))
print(f"사다리꼴의 면적 = {area:.2f}")