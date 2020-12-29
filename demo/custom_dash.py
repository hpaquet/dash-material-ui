import dash
from demo.style import stylesheet


class CustomDash(dash.Dash):
    def interpolate_index(self, **kwargs):
        return f'''
                <!DOCTYPE html>
                <html>
                    <head>
                        {kwargs['metas']}
                        <title>{kwargs['title']}</title>
                        {kwargs['favicon']}
                        {kwargs['css']}
                        <style>{stylesheet.css()}</style>
                    </head>
                    <body>
                        {kwargs['app_entry']}
                        {kwargs['config']}
                        {kwargs['scripts']}
                        {kwargs['renderer']}
                        <div>footer</div>
                    </body>
                </html>
                '''
