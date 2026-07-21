# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
It does not cosider things like tempo, lyrics or prior listening history 
- Genres or moods that are underrepresented 
- Cases where the system overfits to one preference  
May overfits to a users favorite genre 
- Ways the scoring might unintentionally favor some users  
It favors users that have more songs 
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
High-Energy Pop, Chill Lofi, Deep Intense Rock, Conflicting Edge Case 
- What you looked for in the recommendations  
Compared whether the top recommendations matched each profile’s genre, mood, energy, and acoustic preferences.
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  



## OUTPUT: 

Loaded songs: 10

Top recommendations:

1. Sunrise City - Score: 0.97
Because: Genre matches (pop): +0.40; Mood matches (happy): +0.30; Energy similarity (0.82 vs 0.80): +0.15; Acoustic similarity (0.18 vs target 0.0): +0.12

2. Gym Hero - Score: 0.67
Because: Genre matches (pop): +0.40; Mood differs (intense): +0.00; Energy similarity (0.93 vs 0.80): +0.13; Acoustic similarity (0.05 vs target 0.0): +0.14

3. Rooftop Lights - Score: 0.54
Because: Genre differs (indie pop): +0.00; Mood matches (happy): +0.30; Energy similarity (0.76 vs 0.80): +0.14; Acoustic similarity (0.35 vs target 0.0): +0.10

4. Storm Runner - Score: 0.27
Because: Genre differs (rock): +0.00; Mood differs (intense): +0.00; Energy similarity (0.91 vs 0.80): +0.13; Acoustic similarity (0.10 vs target 0.0): +0.14

5. Night Drive Loop - Score: 0.26
Because: Genre differs (synthwave): +0.00; Mood differs (moody): +0.00; Energy similarity (0.75 vs 0.80): +0.14; Acoustic similarity (0.22 vs target 0.0): +0.12