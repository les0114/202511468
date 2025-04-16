
def read_single_digit(n):
    digit_korean = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    return digit_korean[n]


def read_number(n):
    result = ""
    for digit in str(n):
        result += read_single_digit(int(digit)) + " "

    return result.strip()


def main():
    number = int(input("세 자리 정수 입력: "))
    if 0 <= number <= 999:
        print(read_number(number))
    else:
        print("오류: 0 이상 999 이하의 정수만 입력 가능합니다.")


if __name__ == "__main__":
    main()
