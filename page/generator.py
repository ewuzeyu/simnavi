import yaml

with open('config.yml','r',encoding='utf-8') as f:
    result = yaml.load(f.read(),Loader=yaml.FullLoader)


first_content = '''<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="global.css">
        <meta charset="utf-8">
        <title>
            导航页
        </title>
    </head>

    <body>
        <div class="leftnavi">
            <div class="logo col">
                本←导航页→新
            </div>
'''
colcontent = '''
            <a class="col" href="#%s">
                %s
            </a>
'''
middlecon = '''
        </div>
        
        <div class="maincon">
'''
bigcolcon = '''
            <div class="con2col">
                <h4 id="%s">
                    %s
                </h4>
                <div class="con2card">
'''
cardcon = '''
                    <div class="card">
                        <div class="cardcon">
                            <div class="webti">
                                %s
                            </div>
                            <div class="webdes">
                                %s
                            </div>
                        </div>
                        <a href="%s" target="_self" class="coverbtn cbl"></a>
                        <a href="%s" target="_blank" class="coverbtn cbr"></a>
                    </div>
'''
bigcolend = '''                </div>
            </div>'''
allend = '''        </div>
    </body>
</html>'''





with open('index.html','a',encoding='utf-8') as f:
    f.write(first_content)
    for i in result['col']:
        f.write(colcontent%(i,i))

    f.write(middlecon)

    for i in result['col']:
        f.write(bigcolcon%(i,i))
        for j in result[i]:
            if j['desc'] == None:
                f.write(cardcon%(j['name'],j['name'],j['url'],j['url']))
            else:
                f.write(cardcon%(j['name'],j['desc'],j['url'],j['url']))
        f.write(bigcolend)
    
    f.write(allend)
