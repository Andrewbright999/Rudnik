import pickle, os

pikle_path = "user_data.pickle"


if not os.path.exists(pikle_path):
    data = ["@dasha"]
    with open(pikle_path, "wb") as file:
        pickle.dump(data, file)
        
def write_data(data):
    with open(pikle_path, "wb") as file:
        pickle.dump(data, file) # записать сериализованные данные в jar
    
def read_data():
    with open(pikle_path, "rb") as file:
        data = pickle.load(file)
        print(data)
    return data




class UserList:
    '''Класс для работы с списком пользователем'''

    def __init__(self, username_list=None):
        if username_list is None:
            usernames = read_data()
            self.username_list = usernames
        else:
            self.username_list = username_list
    
    def check_user(self, username):
        username = f"@{username}"
        if username in self.username_list:
            print("такой был")
        else:
            print(f"Новый {username}")
            self.append(username)

    def get_all_list(self):
        return self.username_list

    def __getitem__(self, key):
        # если значение или тип ключа некорректны, list выбросит исключение
        return self.username_list[key]

    def __setitem__(self, key, value):
        self.username_list[key] = value

    def __delitem__(self, key):
        del self.username_list[key]

    def __iter__(self):
        return iter(self.username_list)
    
    def __len__(self):
        return len(self.username_list)


    def append(self, value):
        self.username_list.append(value)
        write_data(self.username_list)
