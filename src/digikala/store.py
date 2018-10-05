from models import Product, User


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        if product not in self.products.keys() or self.products[product] < amount:
            raise Exception('Not Enough Products')
        else:
            self.products[product] -= amount

            if self.products[product] <= 0:
                del self.products[product]

    def add_user(self, username):
        u = User(username)
        if u in self.users:
            return None
        else:
            self.users.append(u)
            return username

    def get_total_asset(self):
        total_price = 0

        for product, count in self.products.items():
            total_price += (count * product.price)

        return total_price

    def get_total_profit(self):

        total_profit = 0

        for user in self.users:
            for product in user.bought_products:
                total_profit += product.price

        return total_profit

    def get_comments_by_user(self, user):

        comment_list = list()

        for product in self.products.keys():
            for comment in product.comments:
                if comment.user == user:
                    comment_list.append(comment.text)

        return comment_list

    def get_inflation_affected_product_names(self):

        inflated_products = list()

        for product in self.products.keys():
            for same_name_product in self.products.keys():
                if product == same_name_product or product.name != same_name_product.name:
                    continue
                else:
                    if product.price != same_name_product.price:
                        if product.name not in inflated_products:
                            inflated_products.append(product.name)

        return inflated_products

    def clean_old_comments(self, date):

        comment_list = dict()

        # for product in self.products.keys():
        #     for comment in product.comments:
        #         if comment.date_added < date:
        #             del product.comments[comment]

        for product in self.products.keys():
            for i in range(len(product.comments)):
                comment = product.comments[i]
                if comment.date_added < date:
                    comment_list.update(product=i)

        for pro,i in comment_list.items():
            product = self.products[pro]
            product.comments.pop(i)

    def get_comments_by_bought_users(self, product):

        comment_list = list()

        for user in self.users:
            for product in user.bought_products:
                for comment in product.comments:
                    if comment.user == user:
                        comment_list.append(comment.text)

        return comment_list
