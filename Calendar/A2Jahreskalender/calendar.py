import calfunctions
from tkinter import *

#Main-File
#verwendet: schaltjahr(jahr), monatslaenge(jahr,monat), wochentag(jahr,monat,tag)
def kalender(jahr):

	#Listen für schnellen Zugriff auf Monatsname und Wochentag
	monatsname = ['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember']
	tagnamelang = ['Sonntag','Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag']
	tagname = ['So','Mo','Di','Mi','Do','Fr','Sa']	
	
	
	##Erstellung der Fenster
	
	##Fenster 1 für den Kalender
	##Fenster 2 für die Feiertage
	
	fenster=Tk()
	fenster2=Tk()
	fenster3=Tk()
	windows = [fenster, fenster2, fenster3]
	fenster.title("Kalender des Jahres "+str(jahr)+" Januar bis April")
	fenster2.title("Kalender des Jahres "+str(jahr)+" Mai bis August")
	fenster3.title("Kalender des Jahres "+str(jahr)+" September bis Dezember")	
	
	feiertage=Tk()
	feiertage.title("Feiertage des Jahres "+str(jahr))
	
	
	#============================================
     # Erzeugung Tabelle
     #============================================
	reihe=0
	
	for monat in range(1,5,1):
		#header Monatsname + Tagliste
		###print(monatsname[monat]) #default: print(monatsname[monat],end='\n')
		Label(text=monatsname[monat-1],width=15, relief=GROOVE, bg='green', fg='white').grid(row=reihe,column=0) ###beginnt bei 0, siehe Tage
		reihe+=1 ###hat null einfluss
		for tag in range(1,8,1):
			Label(text=tagname[tag%7],width=15, relief=GROOVE).grid(row=reihe, column=tag-1)
		reihe+=1 ###wochdentagsüberschriften
		monatlang=calfunctions.monatslaenge(jahr,monat)#laenge des aktuellen monates
	
		
		#============================================
		#	Einträge in Tabelle
		#============================================     
		w = calfunctions.wochentag(jahr,monat,1)
			#fügt Leerzeichen ein vor erstem Eintrag in Monat
			###BEACHTE COLUMN BEGINNEN BEI 0
		if (w!=1):
			if(w!=0):
				###print('\t'*(w-1)+'1',end='')
				#hier noch einmal die empty-labels durchgucken, es müssen mehr gedruckt werden
				for i in range(0,w+1,1):
					Label(text='',width=15, relief=GROOVE).grid(row=reihe, column=i)
				Label(text='1',width=15, relief=GROOVE).grid(row=reihe, column=w-1)
			else:
				###print('\t'*6+'1',end='\n') #gibt 6* '\t' aus
				for i in range(0,6,1):
					Label(text='',width=15, relief=GROOVE).grid(row=reihe, column=i)
				Label(text='1',width=15, relief=GROOVE).grid(row=reihe, column=6)#column6, da Sonntag
				reihe+=1
		else:
			###print(str(1),end='')
			Label(text='1',width=15, relief=GROOVE).grid(row=reihe, column=0)#w-1 = Montag ist 1
        

		#schreibt die konsekutiven Wochentage  
		zaehler = 2
		for tag in range(2,monatlang+1,1): # Frage: was ist schneller? range(1,calfunctions.monatslaenge(monat))
			w+=1
			if(w%7==0): #Sonntag
				###print('\t'+str(zaehler),end='\n')
				Label(text=str(zaehler),width=15, relief=GROOVE).grid(row=reihe, column=w%7+6)
				reihe+=1
			elif (w%7==1):#Montag
				Label(text=str(zaehler),width=15, relief=GROOVE).grid(row=reihe, column=w%7-1)
			else:
				###dürfte no Need sein, da grid Label(text='',width=15, relief=GROOVE).grid(row=reihe, column=w%7)
				Label(text=str(zaehler),width=15, relief=GROOVE).grid(row=reihe, column=w%7-1)
			zaehler+=1
		reihe+=1 ###abstand nach letztem Wochentag
	
	reihe=0
	
	for monat in range(5,9,1):
		#header Monatsname + Tagliste
		###print(monatsname[monat]) #default: print(monatsname[monat],end='\n')
		Label(fenster2, text=monatsname[monat-1],width=15, relief=GROOVE, bg='green', fg='white').grid(row=reihe,column=0) ###beginnt bei 0, siehe Tage
		reihe+=1 ###hat null einfluss
		for tag in range(1,8,1):
			Label(fenster2, text=tagname[tag%7],width=15, relief=GROOVE).grid(row=reihe, column=tag-1)
		reihe+=1 ###wochdentagsüberschriften
		monatlang=calfunctions.monatslaenge(jahr,monat)#laenge des aktuellen monates
	
		
		#============================================
		#	Einträge in Tabelle
		#============================================     
		w = calfunctions.wochentag(jahr,monat,1)
			#fügt Leerzeichen ein vor erstem Eintrag in Monat
			###BEACHTE COLUMN BEGINNEN BEI 0
		if (w!=1):
			if(w!=0):
				###print('\t'*(w-1)+'1',end='')
				#hier noch einmal die empty-labels durchgucken, es müssen mehr gedruckt werden
				for i in range(0,w+1,1):
					Label(fenster2, text='',width=15, relief=GROOVE).grid(row=reihe, column=i)
				Label(fenster2, text='1',width=15, relief=GROOVE).grid(row=reihe, column=w-1)
			else:
				###print('\t'*6+'1',end='\n') #gibt 6* '\t' aus
				for i in range(0,6,1):
					Label(fenster2, text='',width=15, relief=GROOVE).grid(row=reihe, column=i)
				Label(fenster2, text='1',width=15, relief=GROOVE).grid(row=reihe, column=6)#column6, da Sonntag
				reihe+=1
		else:
			###print(str(1),end='')
			Label(fenster2, text='1',width=15, relief=GROOVE).grid(row=reihe, column=0)#w-1 = Montag ist 1
        

		#schreibt die konsekutiven Wochentage  
		zaehler = 2
		for tag in range(2,monatlang+1,1): # Frage: was ist schneller? range(1,calfunctions.monatslaenge(monat))
			w+=1
			if(w%7==0): #Sonntag
				###print('\t'+str(zaehler),end='\n')
				Label(fenster2, text=str(zaehler),width=15, relief=GROOVE).grid(row=reihe, column=w%7+6)
				reihe+=1
			elif (w%7==1):#Montag
				Label(fenster2, text=str(zaehler),width=15, relief=GROOVE).grid(row=reihe, column=w%7-1)
			else:
				###dürfte no Need sein, da grid Label(text='',width=15, relief=GROOVE).grid(row=reihe, column=w%7)
				Label(fenster2, text=str(zaehler),width=15, relief=GROOVE).grid(row=reihe, column=w%7-1)
			zaehler+=1
		reihe+=1 ###abstand nach letztem Wochentag
    
	
	reihe=0
	
	for monat in range(9,13,1):
		#header Monatsname + Tagliste
		###print(monatsname[monat]) #default: print(monatsname[monat],end='\n')
		Label(fenster3, text=monatsname[monat-1],width=15, relief=GROOVE, bg='green', fg='white').grid(row=reihe,column=0) ###beginnt bei 0, siehe Tage
		reihe+=1 ###hat null einfluss
		for tag in range(1,8,1):
			Label(fenster3, text=tagname[tag%7],width=15, relief=GROOVE).grid(row=reihe, column=tag-1)
		reihe+=1 ###wochdentagsüberschriften
		monatlang=calfunctions.monatslaenge(jahr,monat)#laenge des aktuellen monates
	
		
		#============================================
		#	Einträge in Tabelle
		#============================================     
		w = calfunctions.wochentag(jahr,monat,1)
			#fügt Leerzeichen ein vor erstem Eintrag in Monat
			###BEACHTE COLUMN BEGINNEN BEI 0
		if (w!=1):
			if(w!=0):
				###print('\t'*(w-1)+'1',end='')
				#hier noch einmal die empty-labels durchgucken, es müssen mehr gedruckt werden
				for i in range(0,w+1,1):
					Label(fenster3, text='',width=15, relief=GROOVE).grid(row=reihe, column=i)
				Label(fenster3,text='1',width=15, relief=GROOVE).grid(row=reihe, column=w-1)
			else:
				###print('\t'*6+'1',end='\n') #gibt 6* '\t' aus
				for i in range(0,6,1):
					Label(fenster3, text='',width=15, relief=GROOVE).grid(row=reihe, column=i)
				Label(fenster3, text='1',width=15, relief=GROOVE).grid(row=reihe, column=6)#column6, da Sonntag
				reihe+=1
		else:
			###print(str(1),end='')
			Label(fenster3, text='1',width=15, relief=GROOVE).grid(row=reihe, column=0)#w-1 = Montag ist 1
        

		#schreibt die konsekutiven Wochentage  
		zaehler = 2
		for tag in range(2,monatlang+1,1): # Frage: was ist schneller? range(1,calfunctions.monatslaenge(monat))
			w+=1
			if(w%7==0): #Sonntag
				###print('\t'+str(zaehler),end='\n')
				Label(fenster3, text=str(zaehler),width=15, relief=GROOVE).grid(row=reihe, column=w%7+6)
				reihe+=1
			elif (w%7==1):#Montag
				Label(fenster3, text=str(zaehler),width=15, relief=GROOVE).grid(row=reihe, column=w%7-1)
			else:
				###dürfte no Need sein, da grid Label(text='',width=15, relief=GROOVE).grid(row=reihe, column=w%7)
				Label(fenster3, text=str(zaehler),width=15, relief=GROOVE).grid(row=reihe, column=w%7-1)
			zaehler+=1
		reihe+=1 ###abstand nach letztem Wochentag
     
	# Gibt die Feiertage aus
    
	###Überschriften
	Label(feiertage, text='Ereignis',width=20,bg='green',fg='white', relief=GROOVE).grid(row=0, column=0)
	Label(feiertage, text='Tag',width=7,bg='green',fg='white', relief=GROOVE).grid(row=0, column=1)
	Label(feiertage, text='Monat',width=15,bg='green',fg='white', relief=GROOVE).grid(row=0, column=2)
	
	feiertag = calfunctions.feiertage(jahr)
	for counter in range(0,len(feiertag),1):        
		###print(feiertag[counter][2]+':\t'+str(feiertag[counter][1])+'. '+str(monatsname[feiertag[counter][0]-1]))
		name=feiertag[counter][2]
		tag=str(feiertag[counter][1])
		monat=str(monatsname[feiertag[counter][0]-1])

        
		Label(feiertage, text=name,width=20, relief=GROOVE).grid(row=counter+2, column=0)
		Label(feiertage, text=monat,width=15, relief=GROOVE).grid(row=counter+2, column=2)
		Label(feiertage, text=tag,width=7, relief=GROOVE).grid(row=counter+2, column=1)

	feiertage.mainloop()
	fenster.mainloop()
    
def	main():
	jahr = int(input("Bitte geben Sie ein Jahr ein: "))
	kalender(jahr)
 
 
if __name__ == '__main__':
    main()

