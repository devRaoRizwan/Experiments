# Docker

Docker is an open source platform that allows you to automate the deployment and management of applications inside lightweight, isolated software containers.

## Advantages of Docker

- **Portable** — Docker containers can run on any system, ensuring consistent behaviour across different environments.
- **Isolation** — Containers are isolated from each other, preventing interference between applications and their dependencies.
- **Efficiency** — Containers are lightweight and start quickly, which optimizes resource usage.
- **Scalability** — Docker makes scaling easy by replicating and distributing containers.
- **Versioning & rollback** — Docker enables versioning and rollback of containerized applications.

## What is a Dockerfile?

A Dockerfile is a text file that contains instructions on how to build a Docker image.
It specifies the base image, the application code, dependencies, commands, and configuration.

## What is a Docker Image?

An image is a lightweight, standalone, and executable software package that includes everything needed to run the application — the code, runtime, system tools, libraries, and settings.

Docker images are created from base images and can be customized and layered with additional components.

## What is a Docker Container?

Containers are isolated environments that encapsulate an application and its dependencies, including libraries, frameworks, and other software components.
Each container runs an isolated process on the host machine and has its own filesystem, networking, and resources.

We can create multiple containers from a single Docker image.

## What is Docker Compose?

Docker Compose is a tool for defining and managing multi-container applications.
It lets you define a multi-container setup in a YAML file, specifying the containers, their configuration, and how they communicate with each other.
It simplifies running complex applications made of multiple interconnected containers.

## What is a Container Registry?

A container registry is a centralized repository for storing and sharing container images.
It lets you manage and distribute containerized applications while ensuring secure access, versioning, and image integrity.

Examples: Docker Hub, Amazon ECR, Google GCR, Azure ACR, GitLab Container Registry.

## What is a Docker Registry?

A Docker registry is a central repository that stores Docker images.
The most common one is Docker Hub, which is a public registry.
You can also set up a private registry to store private images.

## What is a Base Image?

A base image is the initial starting point for building a Docker image — it serves as a template.
It is a prebuilt and reusable image.

## Flow

```
Dockerfile  →  Docker Image  →  Container(s)
```

## Docker Containers vs Virtual Machines

Docker containers are lightweight, share the host OS kernel, start quickly, and use resources efficiently.
Virtual machines run a full guest OS on top of a hypervisor, which makes them heavier and slower to start.

## References

- Official documentation: [docs.docker.com](https://docs.docker.com)
- Public Docker registry: [hub.docker.com](https://hub.docker.com)
