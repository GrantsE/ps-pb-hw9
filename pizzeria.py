class Product:
    def __init__ (self, title, calorific, cost):
        # Вызываем метод check_title, где осуществляется проверка атрибута title   
        # Создаём условие: если calorific и cost > 0, то удастся создать экземляр
        if Product.check_title(title) and calorific > 0 and cost > 0:
            self.__title = title
            self.__calorific = calorific  
            self.__cost = cost
        else:
            raise ValueError
        
    # Создаём статистический метод, в котором осуществляем проверку tittle
    # title не может быть пустым
    @staticmethod
    def check_title(title):
        if type(title) == str and (title != '' and title.isspace() is False):
            return title
           
    # Превращаем метод в свойство, чтобы в дальнейшем обращаться без круглых скобок
    @property
    def title(self):
        return self.__title
    
    # Превращаем метод calorific в свойство, чтобы обращаться далее без круглых скобок
    @property
    def calorific(self):
        return self.__calorific
    
    # Превращаем метод cost в свойство, чтобы обращаться далее без круглых скобок
    @property
    def cost(self):
        return self.__cost
    
    # Создаём сеттер, чтобы была возможность обновить значение title
    # Передаём условие из метода check_title, чтобы сработала проверка в области вне класса
    @title.setter
    def title(self, title):
        if Product.check_title(title):
            self.__title = title
        else:
            raise ValueError
            
    # Создаём сеттер, чтобы была возможность обновить значение calorific
    # при соответствии условию
    @calorific.setter
    def calorific(self, calorific):
        if calorific > 0:
            self.__calorific = calorific
        else:
            raise ValueError
            
    # Создаём сеттер, чтобы была возможность обновить значение cost
    # При соответствии условию
    @cost.setter
    def cost(self, cost):
        if cost > 0:
            self.__cost = cost
        else:
            raise ValueError
            

class Ingredient:
    def __init__ (self, product, weight):
        # Создаём условие: если weight > 0, то удастся создать экземляр       
        if weight > 0:
            self.product = product
            self.__weight = weight
        else:
            raise ValueError
            
    # Создаём функцию для получения калорийности
    def get_calories(self):
        return self.__weight / 100 * self.product.calorific
    
    # Создаём функцию для получения себестоимости
    def get_cost(self):
        return self.__weight / 100 * self.product.cost
    
    # Превращаем метод weight в свойство, чтобы обращаться далее без круглых скобок
    @property
    def weight(self):
        return self.__weight
    
    # Создаём сеттер, чтобы была возможность обновить значение weight
    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError                
    
           
class Pizza (Product):
    def __init__ (self, title, ingredients):
        if Product.check_title(title):
            self.title = title
            self.ingredients = ingredients
        else:
            raise ValueError
                 
    # Создаём метод, где будем получать общую колорийность
    def get_calories(self):
        # Создаём переменную, в которую передаём значения по калорийности
        total_calorific = []
        # Проходимся по атрибуту ingredients, из которого можем получить значения калорий
        # при помощи вызова product.calorific 
        for с in self.ingredients:
            total_calorific.append(с.product.calorific)
        # Получаем общую калорийность
        return float(sum(total_calorific))

    # Создаём метод, где будем получать общую себестоимость
    def get_cost(self):
        # Создаём переменную, в которую передаём значения по себестоимости
        total_сost = []
        # Проходимся по атрибуту ingredients, из которого можем получить себестоимость
        # при помощи вызова product.cost 
        for i in self.ingredients:
            total_сost.append(i.product.cost)
        # Получаем общую себестоимость
        return float(sum(total_сost))
                
                
# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])


print(f'{pizza_margarita.title} ({pizza_margarita.get_calories()} kkal) - {pizza_margarita.get_cost()} руб')

