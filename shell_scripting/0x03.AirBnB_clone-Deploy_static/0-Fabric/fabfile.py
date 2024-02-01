from fabric import task

@task
def hello(ctx, who="world"):
    print(f"Hello, {who}!")

