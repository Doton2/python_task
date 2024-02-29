# ----- 코드 정의 ------
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f'회원 이름 : {self.name}   /   회원 아이디 : {self.username}')
        pass


class Post():
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        pass


# ----- 코드 실행 ------
members = []


user_1 = Member('봄', 'spring', 'spting123')
user_2 = Member('여름', 'summer', 'summer123')
user_3 = Member('가을', 'fall', 'fall123')

user_1.display()
user_2.display()
user_3.display()


members.append(user_1)
members.append(user_2)
members.append(user_3)


print('회원의 이름')
for member in members:
    print(member.name)


posts = []
post1_user_1 = Post(title='1', content='111a111', author='봄')
post2_user_1 = Post(title='2', content='222ㄴ222', author='봄')
post3_user_1 = Post(title='3', content='333ㄷ333', author='봄')

posts.append(post1_user_1)
posts.append(post2_user_1)
posts.append(post3_user_1)


post1_user_2 = Post(title='ㄱ', content='ㄱㄱ1ㄱㄱ', author='여름')
post2_user_2 = Post(title='ㄴ', content='ㄴㄴcㄴㄴ', author='여름')
post3_user_2 = Post(title='ㄷ', content='ㄷㄷ3ㄷㄷ', author='여름')

posts.append(post1_user_2)
posts.append(post2_user_2)
posts.append(post3_user_2)


post1_user_3 = Post(title='a', content='aaaㄱaaa', author='가을')
post2_user_3 = Post(title='b', content='bbb1bbb', author='가을')
post3_user_3 = Post(title='c', content='cccaccc', author='가을')

posts.append(post1_user_3)
posts.append(post2_user_3)
posts.append(post3_user_3)

print('제목')
for i in posts:
    print(i.title)


post_search = input('특정단어를 검색합니다.')
for a in posts:
    if post_search in a.content:
        print(a.title)
