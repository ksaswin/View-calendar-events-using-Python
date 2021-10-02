### Using python to list your weekly events listed in Google calendar.

This program finds events in your Google calendar.


Login to your google account and go to [Google Cloud platform](https://console.developers.google.com/).<br>
Create a new project there and Enable Google Calendar API.<br>
Once you enable that, within credentials you can find your OAuth Client ID and secret.<br>
Download them as json and rename your file as **_credentials.json_**.<br>
Please note that you save this file in the same directory.<br><br>

```
pip install -r requirements.txt
```
If you are on a windows machine:
```
python -m pip install -r requirements.txt
```
<br>
The first time you run the code you maybe prompted to authorize your application.<br>
Upon successful authorisation, you will find a new file named **_token.pickle_** saved in your directory.<br>
Please make sure that you don't share or upload the credentials.json or the token.pickle files on the internet.
