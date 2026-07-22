# Docker for Absolute Beginners

If you have ever heard someone say *"but it works on my machine!"*, Docker is the tool that fixes exactly that problem. This guide explains Docker from scratch, with small examples you can try yourself.

## The problem Docker solves

Imagine you build an app on your laptop. It works perfectly. Then you send it to a friend, or deploy it to a server, and suddenly it breaks — a different Python version, a missing library, a different operating system.

Docker packages your app **together with everything it needs to run** (code, libraries, settings) into one box called a **container**. That box runs the same way everywhere: your laptop, your friend's PC, or a cloud server.

## The three things you must understand

Docker really comes down to three words. Let's go through them in order, because each one builds on the previous.

### 1. Dockerfile — the recipe

A **Dockerfile** is a plain text file with step-by-step instructions telling Docker how to build your app's box.

Think of it like a recipe: "start with this base, copy my files in, install these things, then run this command."

Example `Dockerfile` for a simple Node.js app:

```dockerfile
# Start from an official Node base image
FROM node:20

# Set the working folder inside the container
WORKDIR /app

# Copy dependency list first (for faster rebuilds)
COPY package.json .

# Install the dependencies
RUN npm install

# Copy the rest of the app code
COPY . .

# The command that runs when the container starts
CMD ["node", "index.js"]
```

### 2. Image — the packaged box

When you *build* a Dockerfile, you get an **image**. The image is the finished, packaged box — read-only, and ready to be shipped anywhere.

Build an image from the Dockerfile above:

```bash
docker build -t my-app .
```

- `-t my-app` gives the image a name ("tag").
- The `.` means "use the Dockerfile in the current folder".

See your images:

```bash
docker images
```

### 3. Container — the running box

A **container** is a running instance of an image. The image is the recipe's result sitting on a shelf; the container is when you actually take it off the shelf and run it.

Run a container from your image:

```bash
docker run -p 3000:3000 my-app
```

- `-p 3000:3000` connects port 3000 inside the container to port 3000 on your machine, so you can open it in the browser.

You can start **many containers from one image** — like printing many copies from the same recipe.

Useful commands:

```bash
docker ps            # list running containers
docker ps -a         # list all containers (including stopped)
docker stop <id>     # stop a container
docker rm <id>       # remove a container
```

## The mental model

```
Dockerfile  →  (docker build)  →  Image  →  (docker run)  →  Container
  recipe                          the box                    running box
```

## Running someone else's app (no Dockerfile needed)

You don't always have to build an image. You can pull ready-made ones from **Docker Hub** (a public registry of images). Example — run a database in seconds:

```bash
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=secret postgres
```

- `-d` runs it in the background (detached).
- `-e` sets an environment variable.

No installing Postgres, no config headaches. When you're done, stop and remove it, and your machine stays clean.

## Docker Compose — running many containers together

Real apps often need more than one container: for example a web app **and** a database. Writing long `docker run` commands for each gets tiring.

**Docker Compose** lets you describe all of them in one file called `docker-compose.yml`:

```yaml
services:
  web:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db

  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: secret
```

Then start everything with a single command:

```bash
docker compose up
```

And stop everything with:

```bash
docker compose down
```

## Docker vs Virtual Machines (quick note)

You might wonder how this is different from a virtual machine (VM).

- A **VM** runs a whole separate operating system — heavy, slow to start, uses lots of resources.
- A **Docker container** shares your computer's OS kernel and only packages the app — lightweight, starts in seconds.

That's why you can run many containers where you could only run a few VMs.

## Cheat sheet

| What you want to do        | Command                          |
| -------------------------- | -------------------------------- |
| Build an image             | `docker build -t my-app .`       |
| Run a container            | `docker run -p 3000:3000 my-app` |
| List running containers    | `docker ps`                      |
| Stop a container           | `docker stop <id>`               |
| Remove a container         | `docker rm <id>`                 |
| List images                | `docker images`                  |
| Start a Compose setup      | `docker compose up`              |
| Stop a Compose setup       | `docker compose down`            |

## Where to go next

- Official documentation: [docs.docker.com](https://docs.docker.com)
- Find ready-made images: [hub.docker.com](https://hub.docker.com)

That's the whole foundation. Once **Dockerfile → Image → Container** clicks, everything else in Docker is just building on top of it.
