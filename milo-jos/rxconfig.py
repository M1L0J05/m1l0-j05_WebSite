import reflex as rx

config = rx.Config(
    app_name="milo_jos",
    cors_allowed_origins=[
        'http://localhost:8000',
        'https://api.milo-jos.es',
    ]
)