from cipher_yz4122 import cipher_yz4122

def test_special():
    expected = "Z%"
    actual = cipher_yz4122.cipher("U%", 5)
    assert expected == actual