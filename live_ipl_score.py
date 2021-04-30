from bs4 import BeautifulSoup as bs
import requests
import sys
import time

while True:
    r = requests.get('https://www.cricbuzz.com/cricket-match/live-scores')
    soup = bs(r.content, features = 'html.parser')

    try:
        div = soup.find("div", attrs = {"ng-show" : "active_match_type == 'league-tab'"})
        
        title = div.find("h2").text

        if title != "INDIAN PREMIER LEAGUE 2021":
            print("\nNo IPL matches at the moment")
            sys.exit()
            
        print(f'\n{title}', end='\n\n')

        matches = div.find_all(class_ = "cb-mtch-lst cb-col cb-col-100 cb-tms-itm")
        for match in matches:
            team_names = match.find("h3")
            print(team_names.text[1:-2], end='\n\n')
                
            teams = match.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")
            team_scores = match.find_all("div", attrs = {"style" : "display:inline-block; width:140px"})

            for team, team_score in zip(teams, team_scores):
                print(f'{team.text}: {team_score.text}')

            try:
                live = match.find(class_ = "cb-text-live")
                print('\n' + live.text)
            except AttributeError:
                completed = match.find(class_ = "cb-text-complete")
                print('\n' + completed.text)

            if len(matches) > 1:
                break
    
    except AttributeError:
        print("\nNo IPL matches at the moment")

    time.sleep(45)
