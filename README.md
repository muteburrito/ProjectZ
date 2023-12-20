# Project Z

Project Z is an AI-based GIF and Meme finder. It utilizes in-house developed giphy module to search and retrieve the most relevant GIFs and memes based on user input.

## Features

- AI-powered search: The application leverages machine learning techniques to provide accurate and personalized search results. (Coming soon later next year)
- GIF finder: Users can search for GIFs by entering keywords or phrases.
- Meme finder: Users can discover and share popular memes from various categories.
- User-friendly interface: The application provides a simple and intuitive interface for easy navigation and interaction.

## Installation

To install and run Project Z locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/muteburrito/ProjectZ.git
    ```
    
**Note:** To run the backend server, it is highly recommended to use Python 3.8. You can manage your Python environment using Conda.

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the Flutter app:

    - Install Flutter by following the instructions in the [official documentation](https://flutter.dev/docs/get-started/install).
    - Navigate to the `flutter_app` directory in the cloned repository.
    - Run the following command to fetch the Flutter dependencies:

        ```bash
        flutter pub get
        ```

4. Start the backend server:

    ```bash
    python app.py
    ```

5. Expose your local server to the internet with ngrok:

    - Navigate to the `backend` directory in the cloned repository.
    - Run the following command:

        ```bash
        ./ngrok http 5000
        ```

    **Note:** This assumes that your backend server is running on port 5000. If it's running on a different port, replace `5000` with your server's port number. Also, if you're on Windows, you might need to run `ngrok.exe` instead of `./ngrok`.

6. Start the Flutter app:

    - Connect your device or emulator.
    - Run the following command in the `flutter_app` directory:

        ```bash
        flutter run
        ```

## Usage

Once the application is running, open your web browser and navigate to `http://localhost:5000`. From there, you can start searching for GIFs and memes using the provided search bar.

## Contributing

Contributions are welcome! If you'd like to contribute to Project Z, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions regarding Project Z, feel free to contact us at [kulkarnichinmay65@gmail.com](mailto:kulkarnichinmay65@gmail.com).
