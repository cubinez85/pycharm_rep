from hashlib import md5
print('https://www.gravatar.com/avatar/' + md5(b'cubinez85@mail.ru').hexdigest())