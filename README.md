# Blog
This is blog app with ability to add, edit and delete posts

## Instalation
Make sure Docker is installed on your working machine. If not here is the link https://docs.docker.com/get-docker/

To launch this project first you need to clone the repository.

```bash
git clone 'repository link'
```

Open terminal and navigate to project forder, then build the docker image

```bash
docker-compose up
```

When the building will be finished, the server will be running. 
To use this blog you need at least one user, so you should create super user to login to the blog or admin pannel.
Open new terminal and run this command:

```bash
docker exec -it  'container_id' python manage.py createsuperuser
```

Here you should be good to go. Navigate to terminal where server is running and open server's url.
Enjoy.
