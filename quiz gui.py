import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")

        self.questions = [
            {
                'question': 'How many Cricket World Cup does India have?',
                'choices': ['3', '2', '4', '1'],
                'correct_answer': '2'
            },
            {
                'question': 'What is the capital of France?',
                'choices': ['Paris', 'Berlin', 'Madrid', 'Rome'],
                'correct_answer': 'Paris'
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'choices': ['Earth', 'Mars', 'Venus', 'Jupiter'],
                'correct_answer': 'Mars'
            },
            {
                'question': 'Giddha is the folk dance of?',
                'choices': ['Karnataka', 'Haryana', 'Punjab', 'Orissa'],
                'correct_answer': 'Punjab'
            }
            
            # Add more questions as needed
        ]

        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(master, text="")
        self.question_label.grid(row=0, column=0, pady=10)

        self.choice_var = tk.StringVar()
        self.choice_var.set(None)

        self.choices_frame = tk.Frame(master)
        self.choices_frame.grid(row=1, column=0, pady=10)

        self.feedback_label = tk.Label(master, text="")
        self.feedback_label.grid(row=2, column=0, pady=10)

        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.grid(row=3, column=0, pady=10)

        self.load_question()
        self.display_question()

    def load_question(self):
        current_question = self.questions[self.current_question_index]
        self.question_text = current_question['question']
        self.choices = current_question['choices']
        self.correct_answer = current_question['correct_answer']

    def display_question(self):
        self.question_label.config(text=self.question_text)

        for i, choice in enumerate(self.choices):
            tk.Radiobutton(self.choices_frame, text=choice, variable=self.choice_var, value=choice).grid(row=i, column=0, sticky='w')

    def evaluate_answer(self):
        user_answer = self.choice_var.get()
        if user_answer == self.correct_answer:
            self.score += 1
            feedback = "Correct!"
        else:
            feedback = f"Incorrect! The correct answer is {self.correct_answer}"

        self.feedback_label.config(text=feedback)

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.evaluate_answer()
            self.current_question_index += 1
            self.load_question()
            self.display_question()
            self.feedback_label.config(text="")
        else:
            self.show_final_results()

    def show_final_results(self):
        self.evaluate_answer()
        messagebox.showinfo("Quiz Completed", f"Your final score is {self.score}/{len(self.questions)}")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
