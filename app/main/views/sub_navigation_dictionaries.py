def features_nav():
    return [
        {
            "name": "Features",
            "link": "main.features",
            "sub_navigation_items": [
                {
                    "name": "Emails",
                    "link": "main.features_email",
                },
                {
                    "name": "Text messages",
                    "link": "main.features_sms",
                },
                {
                    "name": "Letters",
                    "link": "main.features_letters",
                },
            ]
        },
        {
            "name": "Roadmap",
            "link": "main.roadmap",
        },
        {
            "name": "Security",
            "link": "main.security",
        },
        {
            "name": "Terms of use",
            "link": "main.terms",
        },
    ]


def pricing_nav():
    return [
        {
            "name": "Pricing",
            "link": "main.pricing",
        },
        {
            "name": "How to pay",
            "link": "main.how_to_pay",
        },
    ]


def using_notify_nav():
    return [
        {
            "name": "Get started",
            "link": "main.get_started",
        },
        {
            "name": "Trial mode",
            "link": "main.trial_mode_new",
        },
        {
            "name": "Delivery status",
            "link": "main.message_status",
        },
        {
            "name": "Guidance",
            "link": "main.guidance_index",
            "sub_navigation_items": [
                {
                    "name": "Create and send messages",
                    "link": "main.create_and_send_messages",
                },
                {
                    "name": "Edit and format messages",
                    "link": "main.edit_and_format_messages",
                },
                {
                    "name": "Branding and customisation",
                    "link": "main.branding_and_customisation",
                },
                {
                    "name": "Send files by email",
                    "link": "main.send_files_by_email",
                },
                {
                    "name": "Upload your own letters",
                    "link": "main.upload_a_letter",
                },
            ]
        },
        {
            "name": "API documentation",
            "link": "main.documentation",
        },
    ]
