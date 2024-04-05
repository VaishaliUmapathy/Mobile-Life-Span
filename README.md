# Mobile Phone Usage Prediction
## Introduction

With the increasing complexity and variety of mobile phones available in the market, it becomes challenging for users to estimate the usage lifespan of their devices. This Flask web application aims to address this challenge by providing a simple tool for predicting mobile phone usage based on user-provided features.

The application is built using Flask, a lightweight Python web framework, and employs a machine learning model trained on a dataset containing information about mobile phone characteristics. Users can input details such as storage capacity, battery capacity, brand, etc., and receive a prediction of their phone's usage lifespan.
This Flask web application predicts mobile phone usage based on various features provided by the user. It utilizes a linear regression model trained on a dataset containing mobile phone characteristics such as storage capacity, battery capacity, brand, etc.

## Getting Started

To run this application locally, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
3. Install the required Python packages by running:
    ```
    pip install -r requirements.txt
    ```
4. Run the Flask application by executing the following command in your terminal:
    ```
    python app.py
    ```
5. Access the application in your web browser at `http://localhost:5000`.
6. This formatting will display the commands as separate code blocks, making them stand out and easier to understand for users who want to set up and run your Flask application.


## Usage

1. Enter the required information about your mobile phone in the provided form fields.
2. Click on the "Predict Lifespan" button.
3. The application will display the predicted mobile phone usage based on the input data.

## File Structure

- `app.py`: The Flask application file containing the routes and model implementation.
- `index.html`: The main HTML template for the user interface.
- `result.html`: The HTML template for displaying the prediction result.
- `style.css`: The CSS file for styling the HTML templates.
- `mobile1.csv`: Dataset used for training the machine learning model.
- `requirements.txt`: Contains a list of required Python packages.

## Dependencies

- Flask: Web framework for building the application.
- pandas: Library for data manipulation and analysis.
- scikit-learn: Library for machine learning modeling.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
