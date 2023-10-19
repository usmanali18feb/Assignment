from django.test import TestCase
from .models import Product  # Import your Product model

class ProductModelTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="A sample product for testing",
            price=99.99,
            in_stock=True,
        )

    def test_read_product(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.name, "Test Product")

    def test_update_product(self):
        product = Product.objects.get(name="Test Product")
        product.description = "Updated description"
        product.save()
        updated_product = Product.objects.get(name="Test Product")
        self.assertEqual(updated_product.description, "Updated description")

    def test_delete_product(self):
        product = Product.objects.get(name="Test Product")
        product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(name="Test Product")

    def test_list_all_products(self):
        products = Product.objects.all()
        self.assertTrue(products.count() > 0)

    def test_find_product_by_name(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.name, "Test Product")

    def test_find_product_by_category(self):
        # Assuming you have a 'category' field in your model
        product = Product.objects.filter(category="Sample Category").first()
        self.assertIsNotNone(product)

    def test_find_product_by_availability(self):
        available_products = Product.objects.filter(in_stock=True)
        self.assertTrue(available_products.count() > 0)
