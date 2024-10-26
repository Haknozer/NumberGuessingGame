<h1>Number Guessing Game</h1>
<p>A simple command-line number guessing game where the computer randomly selects a number, and the user has a limited number of attempts to guess it correctly.</p>

<h2>Game Rules</h2>
<ul>
    <li>The computer will randomly select a number between <strong>1 and 100</strong>.</li>
    <li>The user chooses a difficulty level (easy, medium, hard) to set the number of attempts.</li>
    <li>The user enters their guess, and the game will indicate whether the guess is too high or too low.</li>
    <li>The game ends when the user correctly guesses the number or runs out of attempts.</li>
</ul>

<h2>Features</h2>
<ul>
    <li>CLI-based game interaction.</li>
    <li>Difficulty levels to adjust the number of attempts:
        <ul>
            <li><strong>Easy:</strong> 10 attempts</li>
            <li><strong>Medium:</strong> 5 attempts</li>
            <li><strong>Hard:</strong> 3 attempts</li>
        </ul>
    </li>
    <li>Guidance on each guess (higher or lower) to help the player.</li>
</ul>

<h2>Sample Output</h2>
<pre><code>Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2

Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Enter your guess: 35
Incorrect! The number is less than 35.

Enter your guess: 30
Congratulations! You guessed the correct number in 4 attempts.
</code></pre>

<h2>Getting Started</h2>
<p>Clone the repository and navigate to the project directory:</p>
<pre><code>git clone https://github.com/Haknozer/NumberGuessingGame.git
cd NumberGuessingGame</code></pre>

<p>Run the application:</p>
<pre><code>python main.py</code></pre>

<h2>Requirements</h2>
<p>The game is implemented in Python and requires <code>Python 3.x</code> to run.</p>

<h2>Contributing</h2>
<p>Feel free to fork this repository, submit issues, or create pull requests. Contributions to improve the game's functionality or enhance the user experience are welcome!</p>
https://roadmap.sh/projects/number-guessing-game
