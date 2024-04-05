# Mobile Phone Usage Prediction

## Introduction


* With the increasing complexity and variety of mobile phones available in the market, it becomes challenging for users to estimate the usage lifespan of their devices.

* The application is built using Flask, a lightweight Python web framework, and employs a machine learning model trained on a dataset containing information about mobile phone characteristics.
  
*  Users can input details such as storage capacity, battery capacity, brand, etc., and receive a prediction of their phone's usage lifespan.
This Flask web application predicts mobile phone usage based on various features provided by the user.

* It utilizes a linear regression model trained on a dataset containing mobile phone characteristics such as storage capacity, battery capacity, brand, etc.


## Project Structure


The project folder is organized as follows:
    project-root/(Folder name of your project)
    
        │ ├── app.py # Flask application file
        │ └── mobile1.csv # Dataset file
        │
        ├── static/ # Folder for static files
        │ ├── style.css # CSS stylesheet
        │ └── script.js # JavaScript file (if any)
        │
        └── templates/ # Folder for HTML templates
        └── index.html # Main HTML template


- (`app.py`) for the Flask application and a dataset (`mobile1.csv`) used for training the machine learning model.

- **static:** This folder contains static files such as CSS (`style.css`) and JavaScript (`script.js`) files. These files are served to the client and are used for styling and client-side functionality.

- **templates:** This folder contains HTML templates, with `index.html` being the main template. These templates are rendered by Flask and served to the client.

  
## Getting Started


To run this application locally, follow these steps:


### Prerequisites


Before running the application, ensure you have the following installed:

1. Clone this repository to your local machine.

    i) ---bash---
       git clone https://github.com/VaishaliUmapathy/Mobile-Life-Span.git

    ii)Navigate to the project directory:
       cd mobile-phone-usage-prediction


3. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
    
     
4. Install the required Python packages by running:
    ```
    pip install -r requirements (Flask==2.0.2, pandas==1.3.3, scikit-learn==0.24.2)
    ```
5. Run the Flask application by executing the following command in your terminal:
    ```
    python app.py
    ```
6. Access the application in your web browser at `http://localhost:5000`.

 
7. This formatting will display the commands as separate code blocks, making them stand out and easier to understand for users who want to set up and run your Flask application.



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

Feel free to adjust the content according to your specific project details and preferences. This README provides a comprehensive guide for users to understand the project, install dependencies, run the application, and contribute to it.

