import tkinter as tk
from tkinter import ttk
import threading

from utils import scrape_ads

class AdsPostsWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ## Top Frame
        topFrame = tk.Frame(self, pady=10)

        # Email Row
        emailLabel = tk.Label(topFrame, text='Email')
        emailLabel.grid(row=0, sticky='E')

        emailEntry = tk.Entry(topFrame, textvariable=controller.emailVar)
        emailEntry.grid(row=0, column=1, ipadx=15, padx=5)

        # Password Row
        passLabel = tk.Label(topFrame, text='Password')
        passLabel.grid(row=1, sticky='E')

        passEntry = tk.Entry(topFrame, textvariable=controller.passVar, show='*')
        passEntry.grid(row=1, column=1, ipadx=15)

        # Telegram ID Row
        teleIdLabel = tk.Label(topFrame, text='Telegram User ID')
        teleIdLabel.grid(row=2, sticky='E')

        teleIdEntry = tk.Entry(topFrame, textvariable=controller.teleIdVar)
        teleIdEntry.grid(row=2, column=1, ipadx=15)

        # Remember Me Checkbox
        rememberMeCB = tk.Checkbutton(topFrame, text='Remember Me', variable=controller.rememberMeVar)
        rememberMeCB.grid(columnspan=2)

        # Keywords Row
        keywordsLabel = tk.Label(topFrame, text='Keywords')
        keywordsLabel.grid(row=4, sticky='E')

        keywordsEntry = tk.Entry(topFrame, textvariable=controller.keywordsVar)
        keywordsEntry.grid(row=4, column=1, ipadx=15)

        # Blacklist Keywords Row
        blacklistKeywordsLabel = tk.Label(topFrame, text='Blacklist Keywords')
        blacklistKeywordsLabel.grid(row=5, sticky='E')

        blacklistKeywordsEntry = tk.Entry(topFrame, textvariable=controller.blacklistKeywordsVar)
        blacklistKeywordsEntry.grid(row=5, column=1, ipadx=15)

        topFrame.pack()
        ## End Top Frame

        ## Lower Frame
        lowerFrame = tk.Frame(self)

        # Browse Chrome Button
        browseChromeBtn = ttk.Button(lowerFrame, text='Browse Chromedriver', command=controller.chrome_path)
        browseChromeBtn.grid(row=1, column=0)

        # Get Old Users
        getOldUsersBtn = ttk.Button(lowerFrame, text='Get Old Users', command=controller.start_get_old_users_thread)
        getOldUsersBtn.grid(row=1, column=1)

        # Scraping Button
        scrapingBtn = ttk.Button(lowerFrame, text='Start Scraping', command=self.start_scrape_ads_thread)
        scrapingBtn.grid(row=2, columnspan=2, ipadx=5, ipady=5)

        lowerFrame.pack()

    def start_scrape_ads_thread(self):
        scrapeAdsThread = threading.Thread(target=scrape_ads, args=(controller.version, controller.statusBar, controller.chromePath,
                                        controller.session_id, controller.keywordsVar, controller.blacklistKeywordsVar, controller.emailVar,
                                        controller.passVar, controller.teleIdVar, controller.oldUsersList,), daemon=True, name='scraping_ads_thread')
        scrapeAdsThread.start()