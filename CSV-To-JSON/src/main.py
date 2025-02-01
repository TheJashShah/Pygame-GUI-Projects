import pygame
import os
import tkinter as tk
from tkinter.filedialog import *

pygame.init()

from dropbox import DropBox
from button import Button
from json_to_text import make_line_list

root = tk.Tk()
root.withdraw()

from csv_to_json import make_json, return_list

class App:
    def __init__(self):
        self.width, self.height = 700, 800
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (235, 235, 235)
        self.dropbox = DropBox((self.width - 400)/2, 50)
        self.file = None
        self.result_list = []
        self.line_list = []
        
        self.button = Button((self.width - 200)/2, 300, "Convert to JSON")
        self.save_button = Button((self.width - 200)/2, 400, "Save as .json")

    def update(self):

        if self.file is None:
            self.dropbox.text = "Drag and Drop your CSV Files!"
            self.button.visible = False

    def line_toggle(self):

        if self.line_list != []:

            for line in self.line_list:

                if (line.y <= 475 or line.y >= 765):
                    line.visible = False
                else:
                    line.visible = True

    def main_function(self):

        Running = True
        while Running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False

                if event.type == pygame.DROPFILE:
                    
                    if(event.file.split(".")[-1] != "csv"):
                        self.dropbox.text = "Only CSV Files Allowed!"
                        self.dropbox.icon_display = False
                        self.button.visible = False
                    else:
                        self.file = event.file
                        self.dropbox.text = os.path.basename(self.file)
                        self.dropbox.icon_display = True
                        self.button.visible = True

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    if self.button.visible:
                        if self.button.rect.collidepoint(pos):
                            self.result_list = return_list(self.file)
                            self.save_button.visible = True
                            self.line_list = make_line_list(self.result_list, 10, 475)

                    if self.save_button.visible:
                        if self.save_button.rect.collidepoint(pos):
                            
                            filetypes = (('Text Files', '*.txt'),
                                ('All Files', '*.*'))

                            file = asksaveasfilename(filetypes=filetypes, defaultextension='.json')
                            path = file

                            make_json(self.result_list, path)

                            self.file = None
                            self.result_list = []
                            self.save_button.visible = False
                            self.dropbox.icon_display = False
                            self.line_list = []

                if event.type == pygame.MOUSEWHEEL:

                    for line in self.line_list:
                        line.y += event.y * 5

            self.draw()

    def draw(self):

        self.win.fill(self.color)

        self.dropbox.draw(self.win)

        self.button.draw(self.win)
        self.save_button.draw(self.win)

        self.update()

        if self.line_list != []:
            for line in self.line_list:
                line.draw(self.win)

        self.line_toggle()

        pygame.draw.line(self.win, (0, 0, 0), (0, 470), (self.width, 470))
        pygame.draw.line(self.win, (0, 0, 0), (0, 470 + 310), (self.width, 470 + 310))

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    App().main_function()