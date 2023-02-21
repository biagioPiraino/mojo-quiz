import os
import tkinter as tk
from pathlib import Path
from Quizzer import Quizzer

class UserInterface:
    __UI_BG_COLOR = "#375362"
    __UI_FG_SCORE = "white"
    __UI_BG_CANVA = "white"
    __UI_FG_CANVA = "#375362"
    __UI_BG_RIGHT = "green"
    __UI_BG_WRONG = "red"

    def __init__(self, quizzer: Quizzer) -> None:
        self.__load_quizzer(quizzer)
        self.__load_images_folder_path()
        self.__define_root()
        self.__define_scoreboard()
        self.__define_canva()
        self.__define_buttons()
        self.__launch()
    
    def __load_quizzer(self, quizzer: Quizzer) -> None:
        self.__quizzer = quizzer

    def __load_images_folder_path(self) -> None:
        current_directory = os.path.dirname(os.path.realpath(__file__))
        self.__images_folder_path = Path(current_directory,"Images") 

    def __define_root(self) -> None:
        self.__root = tk.Tk()
        self.__root.title("Mojo-Quiz!")
        self.__root.config(bg=self.__UI_BG_COLOR, padx=20, pady=20)
    
    def __define_scoreboard(self) -> None:
        self.__score_label = tk.Label(
            self.__root, 
            text="Score: 0", 
            padx=20,
            bg=self.__UI_BG_COLOR,
            fg=self.__UI_FG_SCORE
            )
        self.__score_label.grid(column=1, row=0)
    
    def __define_canva(self) -> None:
        self.__qst_canva = tk.Canvas(
            self.__root, 
            bg=self.__UI_BG_CANVA,
            width=300,
            height=250
        )
        self.__question_text = self.__qst_canva.create_text(
            150, 
            125, 
            width=280, 
            text=self.__quizzer.ReturnNextQuestions(), 
            fill=self.__UI_FG_CANVA,
            font=("Arial", 14, "italic"))
        self.__qst_canva.grid(row=1, column=0, columnspan=2, pady=30)

    def __define_buttons(self) -> None:
        self.__true_image = tk.PhotoImage(file=self.__images_folder_path / "true.png")
        self.__true_button = tk.Button(image=self.__true_image, highlightthickness=0, command=self.__click_true_button)
        self.__true_button.grid(row=2, column=0)
        self.__false_image = tk.PhotoImage(file=self.__images_folder_path / "false.png")
        self.__false_button = tk.Button(image=self.__false_image, highlightthickness=0, command=self.__click_false_button)
        self.__false_button.grid(row=2, column=1)
        
    def __click_true_button(self) -> None:
        if (self.__quizzer.CheckUserAnswer(True)):
            self.__qst_canva.config(bg=self.__UI_BG_RIGHT)
        else:
            self.__qst_canva.config(bg=self.__UI_BG_WRONG)
        
        self.__qst_canva.itemconfig(self.__question_text, fill=self.__UI_FG_SCORE)

        if (self.__quizzer.QuestionsStillAvailable()):
            self.__root.after(1000, self.__reset_canva)
        
    def __click_false_button(self) -> None:
        if (self.__quizzer.CheckUserAnswer(False)):
            self.__qst_canva.config(bg=self.__UI_BG_RIGHT)
        else:
            self.__qst_canva.config(bg=self.__UI_BG_WRONG)
        
        self.__qst_canva.itemconfig(self.__question_text, fill=self.__UI_FG_SCORE)
        
        if (self.__quizzer.QuestionsStillAvailable()):
            self.__root.after(1000, self.__reset_canva)

    def __reset_canva(self) -> None:
        self.__qst_canva.config(bg=self.__UI_BG_CANVA)
        next_question = self.__quizzer.ReturnNextQuestions()
        self.__qst_canva.itemconfig(
            self.__question_text, 
            fill= self.__UI_FG_CANVA, 
            text=next_question)

    def __launch(self) -> None:
        self.__root.mainloop()   