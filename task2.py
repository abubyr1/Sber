def build_atm(n: int, k: int, L: list) -> list:
    def can_place_atms(max_distance: int) -> bool:
        count = 0
        for distance in L:
            count += (distance - 1) // max_distance
        return count <= k
#уточнялось как написать двоичный поиск
    left, right = 1, max(L)
    while left < right:
        mid = (left + right) // 2
        if can_place_atms(mid):
            right = mid
        else:
            left = mid + 1
        print(left, right)

    max_distance = left

    new_distances = []
    for distance in L:
        num_splits = (distance + max_distance - 1) // max_distance  # Количество сегментов
        base_distance = distance // num_splits
        print(num_splits, )

        remainder = distance % num_splits

        for _ in range(num_splits):
            if remainder > 0:
                new_distances.append(base_distance + 1)
                remainder -= 1
            else:
                new_distances.append(base_distance)

    return new_distances

