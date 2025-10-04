from Controllers.base_operations import get_app

if __name__ == '__main__':
    app = get_app()
    app.run(debug=True)