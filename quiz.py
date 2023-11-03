# 사용자로부터 크리스마스 트리의 높이를 입력 받음
height = int(input("크리스마스 트리의 높이를 설정하세요: "))

# 크리스마스 트리 출력
for i in range(height):
    # 공백과 별의 조합을 계산하여 출력
    space = " " * (height - i - 1)
    stars = "*" * (2 * i + 1)
    print(space+stars)

print(" " * (height - 1) + "|")
