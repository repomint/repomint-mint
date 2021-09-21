from repomint_mint import create_app


PORT = 5001


if __name__ == "__main__":
    create_app().run(port=PORT)
