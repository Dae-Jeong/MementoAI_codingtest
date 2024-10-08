
def solution(arr: list[int]) -> list[int]:
    """
    제한 조건 A : arr은 길이 1 이상인 배열입니다
    제한 조건 B : 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

    :param arr: 길이 1 이상인 배열
    :return: 최솟값을 제외한 나머지 값들로 이루어진 배열
    """

    # 제한 조건 A에 따라 arr이 1의 경우 남은 원소가 없기 때문에, 추가 로직 진행 없이 길이가 1의 경우 -1을 반환합니다.
    # 제한 조건 B에 따라 중복되는 숫자가 없기 때문에, 길이가 2 이상인 경우 arr의 길이가 0일 경우는 없습니다.
    if len(arr) == 1:
        return [-1]

    # min 함수를 통해 O(N)의 시간 복잡도로 최솟값을 구합니다.
    min_value = min(arr)

    # 리스트 컴프리헨션을 통해 최솟값을 제외한 나머지 값을 반환합니다.
    return [value for value in arr if value != min_value]


def generate_sample_data(length: int) -> list[int]:
    """
    실행 예시를 수행하기 위해 별도로 랜덤한 데이터를 생성는 로직을 구성하였습니다.
    random.sample 메서드를 통해 중복값을 허용치 않는 샘플 데이터를 생성합니다.
    :param length: 생성할 샘플 데이터의 길이
    :return: 샘플 데이터
    """
    import random

    if length < 1:
        raise ValueError("길이는 최소 1 이상이어야 합니다.")

    arr = random.sample(range(1, 1000), length)
    return arr

# 실행 예시 구문
if __name__ == "__main__":
    sample_data = generate_sample_data(10)
    result = solution(sample_data)

    print(sample_data, result)
