import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite_project.settings')

import django
django.setup()

from webapp.models import Project

def populate():
    add_project(name="Pokemon 3D", img_small_name="pkmnrevo_small", img_large_name="pkmnrevo_large", subheading="(work in progress)", description="Well what can I say? This is my latest baby. The steep D3D learning curve coupled with the countless times I've been looking for a bug learning C++, have qualified this project as the longest one in my list. And still it's far from alpha. Walking around the town and speaking to the residents is currently possible while I'm hopelessly trying to find some time off from uni work to enrich this project.", details="To be filled", download_link="https://www.dropbox.com/s/kqla5y2rae5e0vl/pkmnrevo.rar?dl=0", github_link="https://github.com/AlexKoukoulas2074245K/Code-PR")

    add_project(name="Arkanoid 3D", img_small_name="arkanoid_small", img_large_name="arkanoid_large", subheading="", description="This is my take on the classic. I was looking for a nice idea to kick off my first C++, D3D11 project, and I realised that I haven't seen any 3D Arkanoid clones around. So I swiftly got down to it and after spending 40-50 minutes poking around things in Blender I had my models and textures ready! Initially I thought it would be cool to have a gradual camera rotation on the y axis (z front-back, x left-right) but it turned out to be too disorienting. It looks pretty but it's only 2 levels long. Hmm I should probably spend some time making another level or two.", details="To be filled", download_link="https://www.dropbox.com/s/iuinld1ch0dgxuj/arkanoid.rar?dl=0", github_link="https://github.com/AlexKoukoulas2074245K/Arkanoid")

    add_project(name="ScrabbleGL", img_small_name="scrabble_small", img_large_name="scrabble_large", subheading="(with smart AI!)", description="This was a project I made with java and lwjgl trying to earn my wings in OpenGL which I found really hard at first (if only I knew back then how much 'fun' I'll have with d3d later). It includes a competent AI trying to form some of the longest and weirdest sounding and looking words I've ever seen taken straight from unix words. It also has some sweet transitions and animations for almost all objects in the game!", details="To be filled", download_link="https://www.dropbox.com/s/gkvb28n78n53fvm/scrabble.rar?dl=0", github_link="https://github.com/AlexKoukoulas2074245K/MyScrabble")

    add_project(name="Poke Yellow Clone", img_small_name="pokeyellow_small", img_large_name="pokeyellow_large", subheading="(Nice clone of the original)", description="Oh man this one was one of a kind. Well to be honest this was a no brainer back when I was learning java and its convenient JPanels and graphics. My favourite childhood game which LOOKED pretty easy to recreate. Simple graphics simple movement no crazy 3D stuff yet. I think it will suffice to say I was gobsmacked by how astonishingly complicated the game was (especially the battle logic) to get it even remotely close to the original. Half a year later I had managed to make a functional clone of the game up until Mt. Moon (for the initiated ones). And the rest is history as I moved on to other projects..", details="To be filled", download_link="https://www.dropbox.com/s/bcx530n8n7y3sj1/pokyellow.rar?dl=0", github_link="https://github.com/AlexKoukoulas2074245K/Pokemon-Yellow-Clone")

    add_project(name="Defence of the Moderns", img_small_name="dotm_small", img_large_name="dotm_large", subheading="", description="This is my latest project and one I've wanted to do for a long time. Since my first attempt at a 2d tower defence game in java, I've always wanted to do one in 3D. While assets are always a pain, its way more manageable than obviously and RPG for example. I'm quite happy with the engine and how the game is turning out to feel like. Its still in pre-alpha but the engine and ai can be seen in action.", details="To be filled", download_link="https://www.dropbox.com/s/rbckw9jcq3zzm2o/Defence%20of%20the%20Moderns.rar?dl=0", github_link="https://github.com/AlexKoukoulas2074245K/Defence_of_the_Moderns")
    
def add_project(name, img_small_name, img_large_name, subheading, description, details, download_link="", github_link="", views=0):
        
    project = Project.objects.get_or_create(name=name, img_small_name=img_small_name, img_large_name=img_large_name, subheading=subheading, description=description, details=details, download_link=download_link, github_link=github_link, views=views)[0]
    project.save()
    return project
    
if __name__ == '__main__':
    print "Starting population script..."
    populate()
