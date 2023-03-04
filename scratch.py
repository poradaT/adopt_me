from werkzeug.security import generate_password_hash, check_password_hash

pass1 = '1234'
pass1_hash = generate_password_hash(pass1)
print(pass1_hash)
#pbkdf2:sha256:260000$ntZqPanvtctOGV3a$05f5db9e2a537cd73d011b96dbfa7a38063afb4d8f0ee9ef2fb2eca9e5e1d74a

pass1_matches = check_password_hash(pass1_hash, '1234')
print(pass1_matches)

pass2 = '5678'
pass2_hash = generate_password_hash(pass2)
print(pass2_hash)
#pbkdf2:sha256:260000$O5K3Qlrcuq3R8yDy$7ab4e05aa4e7b83813a02260d6154c5e6873dc1b7af65944d8d5a9a66305dee0

pass2_matches = check_password_hash(pass2_hash, '5678')
print(pass2_matches)

pass3 = '1111'
pass3_hash = generate_password_hash(pass3)
print(pass3_hash)
#pbkdf2:sha256:260000$Jp4p9atQEtCagFfz$b2b1a270bb1db2d8df22979d87d918b3a63698831722587091db1612f1436371

pass3_matches = check_password_hash(pass3_hash, '1111')
print(pass3_matches)

pass4 = '2222'
pass4_hash = generate_password_hash(pass4)
print(pass4_hash)
#pbkdf2:sha256:260000$7Whc0uYJGS4egAvq$6e30bb9d39fc213591d90627b84b270e7e664151f14dadacf9e3cea6faf812b6

pass4_matches = check_password_hash(pass4_hash, '2222')
print(pass4_matches)