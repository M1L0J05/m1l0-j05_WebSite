import reflex as rx

config = rx.Config(
    app_name="milo_jos",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)