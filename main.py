import apprise

apobj = apprise.Apprise()
config = apprise.AppriseConfig()
config.add("apprise.conf")
apobj.add(config)


def main(request):
    webhook_body = request.json
    body_text = f'*{webhook_body["attachments"][0]["title"]}*\n'
    body_text += f"{webhook_body['sections'][0]['activitySubtitle']}\n"
    for field in webhook_body["attachments"][0]["fields"]:
        body_text += f"{field['title']}: `{field['value']}`\n"
    apobj.notify(
        body=body_text,
        title=f"*{webhook_body['text']}*",
    )
    return "OK"
