import apprise

apobj = apprise.Apprise()
config = apprise.AppriseConfig()
config.add("apprise.conf")
apobj.add(config)


def main(request):
    webhook_body = request.json
    body_text = f"*{webhook_body['text']}*\n"
    attachments = webhook_body.get("attachments")
    if attachments:
        first_attachment = attachments[0]

        title = first_attachment.get("title")
        title_link = first_attachment.get("title_link")
        if title:
            if title_link:
                body_text += f'[{title}]({title_link})\n'
            else:
                body_text += f'*{title}*\n'

        activitySubtitle = first_attachment.get("activitySubtitle")
        if activitySubtitle:
            body_text += f"{webhook_body['sections'][0]['activitySubtitle']}\n"

        for field in first_attachment.get("fields", []):
            body_text += f"{field['title']}: `{field['value']}`\n"

    sections = webhook_body.get("sections", [])
    for section in sections:
        body_text += f"{section['activitySubtitle']}\n"

    print(f"Notify: {webhook_body['text']} - {body_text}")

    apobj.notify(body=body_text)
    return "OK"
