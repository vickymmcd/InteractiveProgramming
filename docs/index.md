# Project Overview [Maximum 100 words]
The purpose of the project is to predict where someone is from and what their age is based on their responses to a survey. The predictions are updated after every question is answered. We visually depict these predictions using a map of the US and an age line. We use two datasets (grammar and earthquake) as background information to make our predictions as well as our knowledge of Bayesian statistics.


# Results [~2-3 paragraphs + figures/examples]
We have accessed two datasets and the answers to various questions from those datasets to update probabilities that people are from various regions in the United States and various age groups. We used our knowledge of Bayesian statistics to update these probabilities after each question is answered. The questions serve as the controller which updates the model which is the probabilities of what we know about a person based on their answers to various questions. The model immediately updates the view being the pictures of the United States and the age line. The colors and hover titles change to represent the updated probabilities that a person is from a given location and age group based on their answer to the question.

We had several people interact with and answer the questions in our data visualization. By the end of the questions, it often gives a clear picture of where our model thinks the person is from and how old they are just by looking at where the concentrated lighter colors representing a higher probability lie. It is not always accurate in its predicitions but we are assuming this is due to the limitations of the data sets we chose and the ways in which they might be related to location and age as opposed to any inherent problem in our algorithms or visualization. It is also really interesting to see that as people answer questions about different things they affect the probabilities in different ways. For example, it seems that the comma questions contribute more to the probabilities people are from various age groups, while the earthquake questions contribute more to the probabilities of people being from certain locations. 


# Implementation [~2-3 paragraphs + UML diagram]
Describe your implementation at a system architecture level. Include a UML class diagram, and talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did.


# Reflection [~2 paragraphs]
From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?
Also discuss your team process in your reflection. How did you plan to divide the work (e.g. split by class, always pair program together, etc.) and how did it actually happen? Were there any issues that arose while working together, and how did you address them? What would you do differently next time?

