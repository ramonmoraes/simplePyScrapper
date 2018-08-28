from server import app

@app.shell_context_processor
def make_shell_context():
    return dict(app=app)

if __name__ == '__main__':
  app.run()

