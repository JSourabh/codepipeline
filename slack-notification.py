def send_message_to_slack(text):
    from urllib import request, parse
    import json

    post = {"text": "{0}".format(text)}

    try:
        json_data = json.dumps(post)
        req = request.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'})


        resp = request.urlopen(req)
    except Exception as em:
         print("EXCEPTION: " + str(em))

send_message_to_slack('Deployment has been completed.... ')
