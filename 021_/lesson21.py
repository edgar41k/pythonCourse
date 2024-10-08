import hashlib

password = '123456'

print(hashlib.md5(password.encode()).hexdigest())

# 827ccb0eea8a706c4c34a16891f84e7b
# e10adc3949ba59abbe56e057f20f883e