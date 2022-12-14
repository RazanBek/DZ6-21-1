def get_list() -> list:
    return list(range(0, 1_000_000, 2))


class Solution:
    def find_target(self, list, target):
        low = 0
        high = len(list) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = list[mid]
            if guess == target:
                return mid
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
        return None


search1 = Solution()
print(search1.find_target(list=get_list(), target=300_000))
with open('binary_search_docs.txt', 'w', encoding='UTF-8') as file:
    file.write(f'Бинарный поиск:\n')
    file.write("1)Binary Search - это алгоритм\n")
    file.write("2)Binary Search - нужен для поиска элемента\n")
    file.write("3)Находится средний элемент последовательности. Для этого первый и последний индексы связываются с\
переменными,а индекс\nсреднего элемента вычисляется Значение среднего элемента сравнивается с искомым значением.\
В зависимости от того,\nбольше оно или меньше значения среднего элемента, дальнейший поиск будет происходить только в \
левой или только в правой\nполовине. Если значение среднего элемента оказывается равным искомому, поиск\
завершается.Иначе одна из границ\nисследуемой последовательности сдвигается. Если искомое значение больше значения\
среднегоэлемента,то нижняя граница\nсдвигается за средний элемент на один элемент справа. Если искомое значение меньше\
значения среднего элемента, то верхняя\nграница сдвигается на элемент перед средним.Снова находится средний элемент\
теперь уже в выбранной половине.")
