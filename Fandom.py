#!/usr/bin/env python
# coding: utf-8

# In[168]:


#import tkinter as tk
from tkinter import *
import requests

window = Tk()
window.title("Welcome to Fandom Project")
window.geometry('400x400')
txt = Entry(window,width=25)
txt.grid(row=0, column=0)
lbl = Label(window, text="")
lbl.grid(row=1, column=0)
lbl2 = Label(window, text="")
lbl2.grid(row=2, column=0)
lbl3 = Label(window, text="")
lbl3.grid(row=3, column=0)
lbl4 = Label(window, text="")
lbl4.grid(row=4, column=0)
lbl5 = Label(window, text="")
lbl5.grid(row=5, column=0)
message = Message(window, text = "") 
message.grid(row=6, column=0)

def clicked():
    
    user_input = txt.get()
    query = '''
    query ($id: Int, $search: String) { # Define which variables will be used in the query (id)
      Media (id: $id, search: $search, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
        id
        title {
          romaji
          english
          native
        }
        status
        genres
        averageScore
        description
        trailer{
            site
            thumbnail
        }
      }
    }
    '''
    # Define our query variables and values that will be used in the query request
    variables = {
        'search': user_input
    }
    url = 'https://graphql.anilist.co'
    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    y = response.json()
    genres =""
    for i in range(len(y['data']['Media']['genres'])):
        genres = genres + y['data']['Media']['genres'][i] + ', '
    x = y['data']['Media']['description']
    description = re.sub("<br><br>\n", "", x)

    lbl.configure(text='English: '+y['data']['Media']['title']['english'])
    lbl2.configure(text='Native: '+y['data']['Media']['title']['native'])
    lbl3.configure(text='Status: '+y['data']['Media']['status'])
    lbl4.configure(text='Genres: '+genres)
    lbl5.configure(text='AvgScore: '+str(y['data']['Media']['averageScore']))
    message.configure(text='Description: '+description)

btn = Button(window, text="Search", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()

