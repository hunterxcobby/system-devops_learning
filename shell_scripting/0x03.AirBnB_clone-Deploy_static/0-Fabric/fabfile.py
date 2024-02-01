#!/usr/bin/python3

from fabric import task

@task
def hello(ctx, who="world"):
    print(f"Hello, {who}!")

@task
def folder(ctx):
    result = ctx.run("mkdir folder/")
    if result.failed:
        print("Failed to create folder")
