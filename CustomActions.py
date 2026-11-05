# How Docker container action works?
# 1. GitHub Actions starts a runnner
# 2. The runner pulls or builds the docker container
# 3. The container starts wuth its required environment.
# 4. The action executes inside a container
# 5. The result is returned to the GitHub Actions workflow

# name: My Docker Action
# description: Run a custom python script

# runs: 
#     using: docker
#     image: Dockerfile

# Dockerfile
# FROM python:3.12
# COPY script.py /script.py
# ENTRYPOINT ["python", "/script.py"]

# How JavaScript action works?
# 1. GitHub Actions starts a runnner
# 2. The runner executes the JavaScript action code directly on the runner
# 3. Node.js executes the action code
# 4. The result is returned to the GitHub Actions workflow

# name: My JavaScript Action
# description: Run a custom JavaScript script

# runs: 
#     using: node24
#     main: index.js

# index.js
# console.log("Hello from my JavaScript action!");
# console.log("This action is running on Node.js version:");
