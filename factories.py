from factory import Factory, Faker

class ProductFactory(Factory):
    class Meta:
        model = Product  # Replace 'Product' with your actual product model class
    
    name = Faker('word')
    description = Faker('text', max_nb_chars=200)
    price = Faker('random_int', min=10, max=1000)
    in_stock = Faker('random_element', elements=[True, False])
