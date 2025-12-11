import pytest
from assignment import Student,TemperatureSensor

def test1():
    s = Student("Bob")
    s.set_grade(85)
    assert s.get_grade() == 85
    s.set_grade(150)
    assert s.get_grade() in [0,85]
    with pytest.raises(AttributeError):
        _ = s.__grade
    assert s.name == "Bob"

def test2():
    s = TemperatureSensor("Lab")
    s.set_temperature(20)
    assert s.get_temperature() == 20
    s.set_temperature(999)
    assert s.get_temperature() == 20
    s.increase(10)
    assert s.get_temperature() == 30
    s.increase(200)
    assert s.get_temperature() == 150
    s.decrease(50)
    assert s.get_temperature() == 100
    s.decrease(500)
    assert s.get_temperature() == -50
