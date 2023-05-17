from apps.factory import create_app


if __name__ == "__main__":
    app = create_app()
    app.config['DEBUG'] = True

    app.run(port=5001)
