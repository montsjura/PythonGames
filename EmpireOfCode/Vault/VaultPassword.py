golf=lambda s:(9<len(s))*(s.lower()>s>s.upper())*'?'>min(s)

# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert golf('A1213pokl') == False
#     assert golf('bAse730onE') == True
#     assert golf('asasasasasasasaas') == False
#     assert golf('QWERTYqwerty') == False
#     assert golf('123456123456') == False
#     assert golf('QwErTy911poqqqq') == True
#     print("Use 'Check' to earn sweet rewards!")