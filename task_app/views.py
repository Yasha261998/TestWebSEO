from annoying.decorators import render_to


@render_to('task_app/index.html')
def index(request):
    return {}
