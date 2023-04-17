# GenrePredictionServer

The GenrePrediction server is a webserver that accepts requests containing a .wav audio clip, and responds with a prediction of the genre of music contained within the clip in the form of JSON. 

Following is an example JSON response that demonstrates the possible genres and the shape of the response:

[
    {"certainty":0.1,"genre":"blues"},
    {"certainty":0.05,"genre":"classical"},
    {"certainty":0.97,"genre":"country"},
    {"certainty":0.0,"genre":"disco"},
    {"certainty":0.0,"genre":"hiphop"},
    {"certainty":0.02,"genre":"jazz"},
    {"certainty":0.0,"genre":"metal"},
    {"certainty":0.0,"genre":"pop"},
    {"certainty":0.0,"genre":"reggae"},
    {"certainty":0.0,"genre":"rock"}
]


**Note!** <br>
It is recommended to use at least 1.5 seconds of audio to obtain a more accurate prediction. 

## Running

Before running, please install dependencies using the following command:
>pip install -r requirements.txt

Then, to run the server, simply use the following command:
>python main.py