## MillionaireProject

This project is a quiz game based on “Who Wants to Be a Millionaire?” You answer questions to earn points and try to reach the top prize. The game has a frontend (what you see) and a backend (how it works behind the scenes).

## Files and Folders
Root Files

Dockerfile – Instructions for running the project in a container. You don’t need this to play the game, but it can help if you want the project to run the same way on different computers.

.gitignore – A list of files that Git will ignore (like temporary files or logs).

## README.md – This file that explains the project.

test.txt, test1.txt, testc.txt – Files used during development or testing. They are not needed to play the game.

.github/workflows

This folder has files for GitHub Actions. These files help automatically:

Check the code for mistakes

Run tests to see if the game works correctly

Make sure new code does not break anything

You don’t need to run these manually. They are mostly for developers.

backend

This folder has all the server-side code. The backend does the “thinking” part of the game. It:

Chooses questions and keeps track of which ones you already answered

Checks if your answer is correct

Keeps the player’s score

Sends information to the frontend so it can display the questions and results

Some files you might see here:

server.js / app.js – The main file that starts the server

routes/ – Files that define the addresses you can use in the game, like /questions or /answers

controllers/ – Files that contain the main logic, like checking if an answer is correct

models/ – Files that define the data, like what a question or player looks like

config/ – Settings for the server, database, or other things

## frontend

This folder has all the code for what the player sees and interacts with. It includes:

## HTML files 

The pages of the game

## CSS files 
The styles to make the game look nice

## JavaScript files 

Code for game actions, like selecting answers, showing results, and updating the score

## Images or icons 

Pictures for buttons, background, or the game interface

## The frontend talks to the backend to get questions and send answers. It also shows things like:

Questions and possible answers

The “money ladder” showing how much you have won

Game over or win messages

## test

This folder has files to test the game. Testing is used to make sure everything works.

## Unit tests 
Check small parts of the code, like functions that calculate scores

## Integration tests 
Check if the frontend and backend work together

## Other test files 
Developers use them to try ideas or fix bugs



## How the Game Works

You open the game in a browser.

The frontend asks the backend for a question.

You select an answer.

The frontend sends your answer to the backend.

The backend checks if it is correct and sends back the result.

The frontend shows the result and either moves to the next question or ends the game.

You can see your score and the “money ladder” at the side

