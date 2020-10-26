# Задание 2

1. Написать функцию, которая конвертирует **Decimal Degrees (DD)** формат координат в **Degrees Decimal Minutes (DDM)** формат координат
2. С помощью pytest написать параметризированный тест, который принимает на вход значение в DD формате и ожидаемое значение в DDM формате

Пример:
```python
def test_cordinates(given_dd, expected_ddm)
```
Тест дата для параметризации:
```python
TEST_DATA_LONGITUDE = [
  (-180, "180^0W"),
  (-180.0, "180^0W"),
  (-13.912, "13^54.72W"),
  (0, "0^0E"),
  (180.0, "180^0E"),
  (180, "180^0E"),
  (170.0323, "170^1.938E"),
]
```

The functions are in *coordinates_converter.py*. In order to test them:
```
pytest -v
```
The output:
```
============================= test session starts ==============================
platform linux -- Python 3.7.7, pytest-6.1.1, py-1.9.0, pluggy-0.13.1 -- /home/kors/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /home/kors/Documents/test_task_ajax_systems/task_2
collected 14 items                                                             

test_coordinates.py::test_converted_longitude[-180-180^0W] PASSED        [  7%]
test_coordinates.py::test_converted_longitude[-180.0-180^0W] PASSED      [ 14%]
test_coordinates.py::test_converted_longitude[-13.912-13^54.72W] PASSED  [ 21%]
test_coordinates.py::test_converted_longitude[0-0^0E] PASSED             [ 28%]
test_coordinates.py::test_converted_longitude[180.0-180^0E] PASSED       [ 35%]
test_coordinates.py::test_converted_longitude[180-180^0E] PASSED         [ 42%]
test_coordinates.py::test_converted_longitude[170.0323-170^1.938E] PASSED [ 50%]
test_coordinates.py::test_converted_latitude[-90-90^0S] PASSED           [ 57%]
test_coordinates.py::test_converted_latitude[90.0-90^0N] PASSED          [ 64%]
test_coordinates.py::test_converted_latitude[45.8-45^48N] PASSED         [ 71%]
test_coordinates.py::test_converted_latitude[0-0^0N] PASSED              [ 78%]
test_coordinates.py::test_converted_latitude[-50-50^0S] PASSED           [ 85%]
test_coordinates.py::test_converted_latitude[60.55-60^33N] PASSED        [ 92%]
test_coordinates.py::test_converted_latitude[-80.9-80^54S] PASSED        [100%]

============================== 14 passed in 0.08s ==============================
```

#### Requirements:
- Python 3.7.7
- pytest 6.1.1
