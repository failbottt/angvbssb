import os
import re
import mistune
import datetime

class Generator:
    def __init__(self):
        self.dir = ''
        self.articles = []

    def build(self, dir):
        self.init(dir)
        self.getFiles()
        self.createHtml()
        self.updateIndexPage()
        self.copyStaticPages();
        self.copyAssets()

    def init(self, dir):
        if os.path.isdir('./build'):
            os.system('rm -rf ./build')

        if os.path.isdir('./build') == False:
            os.system('mkdir -p ./build/posts')
            os.system('mkdir ./build/assets')

        self.dir = dir

    def getFiles(self):
        self.articles = os.listdir(self.dir)

    def createHtml(self):
        template = open('./templates/page', 'r').read();
        for x in self.articles:
            tmp = template
            fd = open(self.dir + x, 'r')

            # get title meta
            content = fd.read()
            title = re.findall(r'title::\s*.*', content)
            if len(title) > 0:
                title = title[0].split('::')[1].strip()

            ## get description meta
            des = re.findall(r'description::\s*.*', content)
            if len(des) > 0:
                des = des[0].split('::')[1].strip()

            ## remove meta info so MD parser doesn't mess with it
            content = re.sub(r'title::\s*.*', '', content).strip()
            content = re.sub(r'description::\s*.*', '', content).strip()

            ## open the html file
            nf = open('./build/posts/' + x.replace('md', 'html'), 'w+')

            html = tmp.replace('{{ title }}', title)
            html = html.replace('{{ meta:description }}', des)

            # parse md to html
            html = html.replace('{{ content }}', mistune.markdown(content))

            # write to new file
            nf.write(html)

            fd.close()
            nf.close()
            
    def updateIndexPage(self):
        template = open('./templates/index', 'r').read();
        links = "<article class=\"links\">"

        for x in self.articles:
            stats = os.stat(self.dir + x)
            date = datetime.datetime.fromtimestamp(stats.st_birthtime).strftime('%Y-%m-%d')
            fd = open(self.dir + x, 'r')

            # get title
            content = fd.read()
            title = re.findall(r'title::\s*.*', content)
            if len(title) > 0:
                title = title[0].split('::')[1].strip()

            # add link to index page
            html = """
                    <div>
                        <span>%s</span>: 
                        <a href='/posts/%s'>%s</a>
                    </div>
            """ % (date, x.replace('md', 'html'), title)
                    
            links = links + html

        links = links + "    </article>"

        nf = open('./build/index.html', 'w+')
        html = template.replace("<article class=\"links\"></article>", links)
        nf.write(html)
        nf.close()

    def copyAssets(self):
        os.system('cp ./src/assets/* ./build/assets')

    def copyStaticPages(self):
        os.system('cp ./src/static/* ./build')
