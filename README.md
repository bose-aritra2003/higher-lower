# higher-lower
This is my first FLASK application made in python.<br>

## So the rules are simple:
* I am thinking of a number between 0 to 9
* Can you guess it ?

## How to play
* In the address bar just type your guessed number after the '/' and press enter
  * Example: 
    ```http://127.0.0.1:5000/3```,
    ```http://127.0.0.1:5000/6```,
    ```http://127.0.0.1:5000/0```, etc.
* Everytime you guess a number, you will be told whether your guessed number is higher, lower or equal to the correct number

## How to run ?
1. Install python3 on your computer https://www.python.org/downloads/
2. Clone this repository on your local system
3. Open terminal/command-prompt and navigate to this cloned repository
4. Run the following commands:

    * On Linux/MacOS
    ```
    python3 -m venv myvenv
    myvenv/bin/activate
    pip install Flask
    export FLASK_APP=server.py
    flask run
    ```
    * On Windows
    ```
    py -3 -m venv myvenv
    myvenv\Scripts\activate
    pip install Flask
    set FLASK_APP=server.py
    flask run
    ```
5. Click on the server link that you get in the terminal/command-prompt and your are ready to play
    * Example server link: ```http://127.0.0.1:5000```
