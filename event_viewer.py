from __future__ import print_function  # These imports must stay on top of all the other ones
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def elist(events, el1):
    l = list()
    for event in events:
        et = (event['start'].get('dateTime')[5:10])
        if et == el1:
            l.append(event['summary'])
    return l

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    start_date = datetime.datetime.today().isoformat() + 'Z'
    end_date = (datetime.datetime.today() + datetime.timedelta(days=6)).isoformat() + 'Z'

    eventsResult = service.events().list(
        calendarId='primary',
        timeMin=start_date,
        timeMax=end_date,
        singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    count = 0
    for t in range(int(datetime.datetime.today().strftime("%d")),
                   int((datetime.datetime.today() + datetime.timedelta(days=7)).strftime("%d"))):
        print("-" * 50)
        if count == 0:
            el1 = (datetime.datetime.today() + datetime.timedelta(days=count)).strftime("%m-%d")
            el = elist(events, el1)
            if not el:
                print("Today  No events scheduled.")
            else:
                print("Today  ", end="")
                print(*el, sep=", ")

        else:
            el1 = (datetime.datetime.today() + datetime.timedelta(days=count)).strftime("%m-%d")
            el = elist(events, el1)
            if not el:
                print((datetime.datetime.today() + datetime.timedelta(days=count)).strftime("%a, %b %d "),
                      "No events scheduled.")
            else:
                print((datetime.datetime.today() + datetime.timedelta(days=count)).strftime("%a, %b %d  "),
                      end="")
                print(*el, sep=", ")
        count += 1
    print("-" * 50)


if __name__ == '__main__':
    main()

