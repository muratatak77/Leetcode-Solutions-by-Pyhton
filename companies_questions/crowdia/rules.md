# Flakey API Challenge
## CrowdAI Full-Stack Engineer Interview

Hello,

Welcome to the interview. Today we are going to do some data manipulation with our flakey API.

### What does the API do?

The API returns a JSON response with a list of employees of a company. The full list is constant; each employee has a unique name and income data. Income data contains an array of objects, and each of them, in turn, contains a month and income. Just make a test request to check out the schema!

### How do I access it?

The project has an already implemented `Client` class, which is already included in your main project file, `main.rb`. The client should be used "as is." If you check its implementation, it expects a token for initialization. This token will be provided to you by your CrowdAI interviewer.

### Sounds great! But why is it flakey?

Well, out of 100 employees and 12 income data records per employee we have in our database, the API returns only a subset of employees and a subset of their income data every time. Moreover, sometimes it can respond with an **unparsable JSON**, so be aware.

### Got it! What should I do?

We expect you to make several requests in one run and properly resolve duplicates to add new data and preserve existing data at the same time. Gathering whole dataset is **not** the goal, but if you do, that's awesome! It would be great if your program also printed some statistics, e.g., how many employees you received, how many of the received employees have been already saved, how many are new, etc. **If you still have any questions, please talk to your interviewer**.

### Good luck!