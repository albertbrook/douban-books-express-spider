class CreatePage(object):
    page = None

    @classmethod
    def open(cls, file_name):
        cls.page = open("%s.html" % file_name, "w", encoding="utf-8")
        html_str = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <style type="text/css">
                    body, ul, li, img, a, h4{
                        margin: 0;
                        padding: 0;
                        border: 0;
                    }
                    body {
                        font: 14px/18px "宋体";
                        color: #333;
                    }
                    a {
                        color: black;
                    }
                    .list-express > li {
                        width: 750px;
                        margin: 10px 0;
                        list-style: none;
                        background-color: #f9f9f9;
                    }
                    .cover {
                        width: 20%;
                        float: left;
                    }
                    .info {
                        width: 70%;
                        padding: 0 5%;
                        float: left;
                    }
                    .info li {
                        margin: 10px 0;
                        list-style: none;
                    }
                </style>
            </head>
            <body>
            <ul class="list-express">
        """
        cls.page.write(html_str)

    @classmethod
    def write(cls, img_src, **info):
        if info["resume"][-3:] == "...":
            info["resume"] = info["resume"][:-3] + "<a href='%s' target='_blank'>...</a>" % info["link"]
        html_str = """
                <li>
                    <div class="cover"><a href="{0}" target="_blank"><img src="{1}" width="100%"></a></div>
                    <div class="info">
                        <ul>
                            <li><h4><a href="{0}" target="_blank">{2}</a></h4></li>
                            <li>{3} / {4} / {5}</li>
                            <li>{6}</li>
                        </ul>
                    </div>
                    <div style="clear: both;"></div>
                </li>
        """.format(info["link"], img_src, info["title"], info["author"],
                   info["year"], info["publisher"], info["resume"])
        cls.page.write(html_str)

    @classmethod
    def close(cls):
        html_str = """
            </ul>
            </body>
            </html>
        """
        cls.page.write(html_str)
        cls.page.close()
