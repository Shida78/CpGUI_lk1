import numpy as np

def normalize_to_unit(values: np.ndarray) -> np.ndarray:
    maximum = values.max()
    minimum = values.min()
    if maximum == minimum:
        return np.zeros_like(values, dtype=float)
    return (values - minimum) / (maximum - minimum)

# ✅ ПРОВЕРКА ЗАДАНИЯ 5
test_values = np.array([10, 20, 30], dtype=float)
actual = normalize_to_unit(test_values)
expected = np.array([0.0, 0.5, 1.0])

constant_actual = normalize_to_unit(np.array([7, 7, 7]))

if np.allclose(actual, expected) and np.allclose(
    constant_actual,
    np.zeros(3),
):
    print("✅ Все тесты пройдены.")
else:
    print("Пока решение требует исправления.")
    print("Получено для [10, 20, 30]:", actual)
    print("Ожидалось:", expected)
    print("Получено для одинаковых значений:", constant_actual)
#%%
