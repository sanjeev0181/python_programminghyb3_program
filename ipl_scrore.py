from tkinter import *
import requests
from bs4 import BeautifulSoup


#Create instance from windows
root=Tk()
#set titile form Windows
root.title("Indian Premier League")
#Cricbuzz url to get score updates
url="https://www.cricbuzz.com/"

def get_score():
    #request data from cricbuzz
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    #name of the first team
    team_1=soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
    #name of the second team
    team_2=soup.findall(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
    #score of the first team
    team_1_score=soup.findall(class_ = "cb-ovr-flo")[0].get_text()
    #score of the second team
    team_2_score=soup.findall(class_ = "cb-ovr-flo")[1].get_text()
    #configure the team names to teams labels
    teams.config(text=f'{team_1}\t\t{team_2}')
    #configure the team scores to teams labels
    score.config(text=f'{team_1_score})\t{team_2_score}')
    # call the get_score() function
    # after every 1000 milliseconds
    # and update scores
    scores.after(1000, get_score)
    #label to dispaly ipl 2021 title
    title = Label(root,text="IPL 2021",font=('Haveltica 30 bold'))
    title.grid(row=0,pady=5)
    #labels for team names
    teams = Label(root,font=("Haveltica 20 bold"))
    teams.grid(row=1,padx=5)
    #labels for team scores
    scores = Label(row,font=('Haveltica 10 bold'))
    scores.grid(row = 2 ,padx=5)
    #call function
    get_score()
    root.mainloops()

