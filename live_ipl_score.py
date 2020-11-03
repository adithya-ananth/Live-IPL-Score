from bs4 import BeautifulSoup as bs
import requests

r = requests.get('https://www.cricbuzz.com/cricket-match/live-scores')
soup = bs(r.content, features = 'html.parser')


try:
    div = soup.find("div", attrs = {"ng-show" : "active_match_type == 'league-tab'"})

    title = div.find("h2")
    print(title.text, end='\n\n')

    matches = div.find_all(class_ = "cb-mtch-lst cb-col cb-col-100 cb-tms-itm")
    for match in matches:
        team_names = match.find("h3")
        print(team_names.text[1:-2], end='\n\n')
        
        teams = match.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")
        team_scores = match.find_all("div", attrs = {"style" : "display:inline-block; width:140px"})

        for team, team_score in zip(teams, team_scores):
            print(f'{team.text}: {team_score.text}')

        live = match.find(class_ = "cb-text-live")
        print('\n' + live.text)
        
    
except AttributeError:
    print("\nNo IPL matches at the moment")




