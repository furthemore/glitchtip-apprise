import apprise

apobj = apprise.Apprise()
config = apprise.AppriseConfig()
config.add("apprise.conf")
apobj.add(config)


def main(request):
    body_text = ""
    webhook_body = request.json
    attachments = webhook_body.get("attachments")
    if attachments:
        first_attachment = attachments[0]

        title = first_attachment.get("title")
        if title:
            body_text = f'*{webhook_body["attachments"][0]["title"]}*\n'
        activitySubtitle = first_attachment.get("activitySubtitle")
        if activitySubtitle:
            body_text += f"{webhook_body['sections'][0]['activitySubtitle']}\n"

        for field in first_attachment.get("fields", []):
            body_text += f"{field['title']}: `{field['value']}`\n"

    print(f"Notify: {webhook_body['text']} - {body_text}")
    body_text += f"{webhook_body['text']}\n"

    apobj.notify(body=body_text)
    # apobj.notify(
    #    body=body_text,
    #    title=f"*{webhook_body['text']}*",
    # )
    return "OK"
