from example import full_name

# class TestSomething:
#     def test_somethng(self):
#         pass

def test_example():
    first_name = 'John'
    second_name = 'Smith'

    assert full_name(first_name, second_name) == 'John Smith'
