import pathlib
from django.http import HttpResponse

## this will leave you with the path directory of the file that you are currentl 
this_dir = pathlib.Path(__file__).resolve().parent

## this is a function that allows a user to request a page
## this function will return whatever is within the function
## the content in here has to map to a url:
    ## this was don in the url.py server
def home_page_view(request, *args, **kwargs):
    my_title = "My page"
    my_context = {
        "page_title": my_title
        }
    html_ = """
        <!DOCTYPE html>
<html>

<body>
    <h1>{page_title}</h1>
</body>

</html>
    """.format(**my_context)
    #html_file_path = this_dir / "home.html"
    #html_ = html_file_path.read_text()
    return HttpResponse(html_)
