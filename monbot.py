#!/usr/bin/env python3
#coding:utf8
######################################### PARAMETRES A PERSONALISER ################
bot   = "KICHOU" # nom de votre bot
jouea = "Python discord" # activité du bot
token = "mettre ici le tocken de votre bot" #token du boot
####################################################################################

import discord #attention a ne pas nomer ce fichier discord.py
import time

class MyClient(discord.Client):

    jeux='off'

    async def on_ready(self):
        await client.change_presence(status=discord.Status.online, activity=discord.Game('{}'.format(jouea)))
        print('BOT : {} actif joue à {} ----------------------> OK'.format(bot,jouea))

    # a travailler (édition de messages)
    async def on_message_edit(self,before, after):
        print('edit:')
        print(before.content)
        print(after.content)


    async def on_message(self, message):
        if 1 == 1 :#tous les channels
        #if (str(message.channel)=='général') or (str(message.channel)=='test'): #seulement ces channels
            print('{} canal: {} de: {} message: {}'.format(bot,message.channel,message.author,message.content))
            print('ID message: {}'.format(message.id))
            print('')

            if (1==1):
                if str(message.content).lower().find('°') >= 0 :
                    await message.delete(delay=10)
        if message.author == self.user:
            if str(message.content).lower().find('°') >= 0 :
                await message.delete(delay=10)
            return

        #COMMANDES simple en début de ligne #######################################################
        if message.content.startswith('>hello') or message.content.startswith('>Hello'):
            await message.channel.send('H e l l o, comment vas-tu {} ?'.format(message.author.name))

        if message.content.startswith('>aide') or message.content.startswith('>aide'):
            await message.channel.send('Liste des commandes : >hello, >miaou, 2')

        # VARIABLES globales et commande d'activation du jeux


        if message.content.startswith('jeux on'):
            MyClient.jeux = 'on'
            await message.channel.send('Activation du jeux, état = {}'.format(MyClient.jeux))
            return

        if message.content.startswith('jeux off'):
            MyClient.jeux = 'off'
            await message.channel.send('Désactivation du jeux, état = {}'.format(MyClient.jeux)) 
            return

        if message.content.startswith('jeux'):
            await message.channel.send('jeux = {}'.format(MyClient.jeux))            

        # JEUX ni oui ni nom ###################################
        if MyClient.jeux == 'on':       
            if str(message.content).lower().find('oui') > -1:
                await message.channel.send('Ta perdu {} Tu a dit OUI !'.format(message.author.name))
            if str(message.content).lower().find('non') > -1:
                await message.channel.send('Ta perdu {} Tu a dit NON !'.format(message.author.name))
                
        #COMMANDES CLEAR ####################################################################
        cmd=('clear')
        if message.content.startswith(cmd):
            nb = int(message.content[len(cmd):len(cmd)+10])+1
            print(nb)
            await message.channel.purge(limit=nb)
            await message.channel.send('{} Message(s) supprimé {} !'.format(nb-1,message.author.name))

        #COMMANDES nbm compte les message dans un channel ###################################
        if message.content.startswith('nbm'):
            await message.channel.send('ta demande est en cours {}, ça peut être long !'.format(message.author.name))
            counter = 0
            async for message in message.channel.history(limit=50000):
                if 1 == 1:
                    counter += 1
            await message.channel.send('{} Messages  !'.format(counter))
            #print(counter)

        #COMMANDE AVEC EFFACE COMMANDE #######################################################
        if message.content.startswith('>miaou'):
            await message.channel.purge(limit=1)
            #await message.delete(delay=5)
            await message.channel.send('https://tenor.com/view/test-neko-test-neko-keyboard-test-neko-meow-meow-gif-14509709 °')

        #DETECION MOT mouse bonjour hello avion apero sieste level bière café givre café :coffee: pelle poubelle @kichou 
        if str(message.content).lower().find('mousse ') > -1:
            await message.channel.send('Qui Fait de la mousse ?')

        if str(message.content).lower().find('bonjour') >= 0 and str(message.content).find('@') == -1 :
            await message.channel.send('Bonjour, comment vas-tu {} ?'.format(message.author.name))
            print(str(message.content).find('@'))
            
        if str(message.content).lower().find('hello') >= 0 and str(message.content).find('@') == -1 :
            await message.channel.send('Hello, {} Comment ça va ?'.format(message.author.name))
            print(str(message.content).find('@'))

        if str(message.content).lower().find('avion') >= 0 :
            await message.channel.send('https://www.inc-conso.fr/sites/default/files/styles/picture_article/public/avion-2_252.png?itok=7v3a8NxD °')

        if str(message.content).lower().find('apero') >= 0 :
            await message.channel.send('https://tenor.com/view/baby-yoda-yoda-child-the-child-mandalorian-gif-16440753 °')

        if str(message.content).lower().find('sieste') >= 0 :
            await message.channel.send('https://tenor.com/view/chillin-cat-nap-tom-sleeping-gif-14821084 °')

        if str(message.content).lower().find('level') >= 0 :
            await message.channel.send('https://tenor.com/view/play-hard-gamer-play-hard-level-gif-8993741 °')

        if str(message.content).lower().find('bière') >= 0 :
            await message.channel.send('https://tenor.com/view/scholleveld-sonneveld-gif-18747738 °')

        if str(message.content).lower().find('givre') > -1:
            await message.channel.send('Du givre ou ça dans quel coin ?')

        if str(message.content).lower().find('café') > -1:
            await message.channel.send('Moi aussi je veux bien un petit ☕ {} !'.format(message.author.name))

        if str(message.content).lower().find('☕') > -1:
            await message.channel.send('Moi aussi je veux bien un petit ☕ {} !'.format(message.author.name))

        if str(message.content).lower().find('pelle') > -1:
           await message.channel.send('https://tenor.com/view/coup-de-pelle-shovel-hit-shovel-whack-gif-12859565 °')

        if str(message.content).lower().find('poubelle') > -1:
           await message.channel.send('<:poubjaune:712187805643833424> °')

        if str(message.content).lower().find('<@!773136088582717441>') > -1: #@kichou a personaliseravec identifiant du bot
           await message.channel.send('Oui {} je suis la !'.format(message.author.name) )

        if str(message.content).lower().find('miaou') > -1:
           await message.channel.send('https://tenor.com/view/test-neko-test-neko-keyboard-test-neko-meow-meow-gif-14509709 °')

        if str(message.content).lower().find('mdr') > -1:
           await message.channel.send('https://tenor.com/view/hahaha-laugh-lol-tom-and-jerry-gif-8702712 °')


        if str(message.content).lower().find('heure') > -1: #
           await message.channel.send('Oui {} je suis la ! il est {}'.format(message.author.name,time.asctime()) )


client = MyClient()
client.run(token)




