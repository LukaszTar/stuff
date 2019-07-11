def test_file_output_with_tempdir(tmpdir):
    tempf = tmpdir.join('output.txt')
    tempf.write('witaj swiecie')
    content = tempf.read()
    assert  content == 'witaj swiecie'