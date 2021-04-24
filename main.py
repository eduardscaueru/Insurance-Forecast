import turicreate
import matplotlib.pyplot as plt

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_region(reg):
    if reg == 'southwest':
        return 0
    elif reg == 'southeast':
        return 1
    elif reg == 'northwest':
        return 2
    else:
        return 3


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Load dataset
    insurance = turicreate.SFrame.read_csv('insurance.csv')

    # Edit data
    insurance['sex'] = insurance['sex'] == 'female'
    insurance['smoker'] = insurance['smoker'] == 'yes'
    insurance['region'] = insurance['region'].apply(get_region)
    print(insurance[1])

    # Split data
    train_data, test_data = insurance.random_split(0.8)

    # Build model
    features = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
    regression_insurance_model = turicreate.linear_regression.create(train_data, target='charges',
                                                                     features=features, validation_set=None)
    print(test_data['charges'].mean())
    print(regression_insurance_model.evaluate(test_data))
    print(regression_insurance_model)

    # Predict
    age = int(input("age: "))
    sex = 0 if input("sex ('male' or 'female'): ") == 'male' else 1
    bmi = float(input("bmi: "))
    children = int(input("children: "))
    smoker = 0 if input("smoker ('yes' or 'no'): ") == 'no' else 1
    region = get_region(input("region ('southwest', 'southeast', 'northwest' or 'northeast'): "))
    person = {'age': [age], 'sex': [sex], 'bmi': [bmi], 'children': [children], 'smoker': [smoker], 'region': [region]}
    print(person)
    print(regression_insurance_model.predict(turicreate.SFrame(person)))

