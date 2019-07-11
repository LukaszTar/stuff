import os

def test_file_output():
    open('output.txt', 'w').write('witaj swiecie')
    assert os.path.exists('output.txt')

def teardown_function():
    if os.path.exists('output.txt'):
        os.remove('output.txt')