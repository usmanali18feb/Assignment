from behave import given, when, then
from your_app.models import YourModel  # Import your model

# Load data into the system
@given("I have loaded the following data")
def load_data(context):
    # The context.data_table variable contains the loaded data
    for row in context.data_table:
        # You can access the columns of each row using their headers
        data = {
            "column_name_1": row["Column 1 Header"],
            "column_name_2": row["Column 2 Header"],
            # Add more columns as needed
        }

        # Create and save your model instance
        your_model_instance = YourModel(**data)
        your_model_instance.save()

# Additional steps related to data loading, if needed
# ...

# Verify that the data has been loaded
@then("the data should be loaded into the system")
def verify_data_loaded(context):
    # You can use your model's query methods to check if the data is in the database
    loaded_data = YourModel.objects.filter(...)  # Adjust the filter conditions

    # Assert that the data exists in the database
    assert len(loaded_data) > 0

# Additional verification steps, if needed
# ...
