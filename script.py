from dashboard.models import Counsellor, User
from dashboard.analytics import *
from random import randint
from datetime import datetime
import time


f=open('c.csv')
for i in f.read().strip().split('\n'):
	j=i.split(',')
	user = User.objects.create_user(username=j[0], email=j[3], is_counsellor=True, password=j[0] + 'pswd')
	user.save()
	time.sleep(0.3)
	counsellor = Counsellor(
		user=user,
		email=j[3],
		phone_number=j[2],
		sat_score=randint(120,161)*10,
		act_score=randint(20,37),
		gpa=randint(20,41)/10.0,
		ethnicity=randint(0,8),
		university=j[1],
		last_login=datetime.now(),
	)
	counsellor.save()

"""
f = open('c.csv', 'a+')
store = "wadsworthcounsellor@gmail.com;sheffiecounsellor@gmail.com;fairfaxcounsellor@gmail.com;cyrilcounsellor@gmail.com;avigdorcounsellor@gmail.com;svendcounsellor@gmail.com;lindycounsellor@gmail.com;richmoundcounsellor@gmail.com;valentincounsellor@gmail.com;heribertocounsellor@gmail.com;giffycounsellor@gmail.com;rafaelllecounsellor@gmail.com;douglascounsellor@gmail.com;waldoncounsellor@gmail.com;uptoncounsellor@gmail.com;byramcounsellor@gmail.com;gilburtcounsellor@gmail.com;costacounsellor@gmail.com;armandocounsellor@gmail.com;holtcounsellor@gmail.com;bondiecounsellor@gmail.com;fonziecounsellor@gmail.com;papagenocounsellor@gmail.com;chancounsellor@gmail.com;tremainecounsellor@gmail.com;christianocounsellor@gmail.com;frasercounsellor@gmail.com;jaecounsellor@gmail.com;barnebascounsellor@gmail.com;seecounsellor@gmail.com;farleecounsellor@gmail.com;aluinocounsellor@gmail.com;neddycounsellor@gmail.com;miguelcounsellor@gmail.com;dominiquecounsellor@gmail.com;raddycounsellor@gmail.com;judoncounsellor@gmail.com;siwardcounsellor@gmail.com;kareemcounsellor@gmail.com;humphreycounsellor@gmail.com;errickcounsellor@gmail.com;tyecounsellor@gmail.com;cyruscounsellor@gmail.com;lemcounsellor@gmail.com;tanncounsellor@gmail.com;casscounsellor@gmail.com;percevalcounsellor@gmail.com;eduinocounsellor@gmail.com;gearaltcounsellor@gmail.com;rogcounsellor@gmail.com;quinlancounsellor@gmail.com;jarviscounsellor@gmail.com;broddycounsellor@gmail.com;humfriedcounsellor@gmail.com;neallcounsellor@gmail.com;artaircounsellor@gmail.com;miltycounsellor@gmail.com;alexandroscounsellor@gmail.com;koenraadcounsellor@gmail.com;peytoncounsellor@gmail.com;slycounsellor@gmail.com;tallycounsellor@gmail.com;rexcounsellor@gmail.com;kasparcounsellor@gmail.com;karlancounsellor@gmail.com;anatolcounsellor@gmail.com;heindrickcounsellor@gmail.com;emersoncounsellor@gmail.com;dewiecounsellor@gmail.com;andreycounsellor@gmail.com;fremontcounsellor@gmail.com;jabezcounsellor@gmail.com;doycounsellor@gmail.com;darcycounsellor@gmail.com;kingstoncounsellor@gmail.com;gallardcounsellor@gmail.com;oliviercounsellor@gmail.com;archiecounsellor@gmail.com;simonecounsellor@gmail.com;majecounsellor@gmail.com;rupertocounsellor@gmail.com;salvatorecounsellor@gmail.com;klementcounsellor@gmail.com;christophecounsellor@gmail.com;suttoncounsellor@gmail.com;hartwellcounsellor@gmail.com;dylancounsellor@gmail.com;tieboutcounsellor@gmail.com;artiecounsellor@gmail.com;thomacounsellor@gmail.com;earlycounsellor@gmail.com;devincounsellor@gmail.com;andriscounsellor@gmail.com;lekcounsellor@gmail.com;hillarycounsellor@gmail.com;christopercounsellor@gmail.com;lammondcounsellor@gmail.com;thomascounsellor@gmail.com;ikeycounsellor@gmail.com;saxcounsellor@gmail.com;Catlincounsellor@gmail.com;Michelinecounsellor@gmail.com;Dinacounsellor@gmail.com;Cathalcounsellor@gmail.com;Dearcounsellor@gmail.com;Romuluscounsellor@gmail.com;Saleemcounsellor@gmail.com;Wallycounsellor@gmail.com;Jo-anncounsellor@gmail.com;Armandcounsellor@gmail.com;Ariadnecounsellor@gmail.com;Siamackcounsellor@gmail.com;Gencounsellor@gmail.com;Ardiscounsellor@gmail.com;Valentinecounsellor@gmail.com;Saswatacounsellor@gmail.com;Penangcounsellor@gmail.com;Marietcounsellor@gmail.com;Rameshcounsellor@gmail.com;Maxycounsellor@gmail.com;Juniecounsellor@gmail.com;Minnecounsellor@gmail.com;Joyouscounsellor@gmail.com;Juilecounsellor@gmail.com;Kristophercounsellor@gmail.com;Erniecounsellor@gmail.com;Rollycounsellor@gmail.com;Faustinecounsellor@gmail.com;Kiemcounsellor@gmail.com;Juliettecounsellor@gmail.com;Joellecounsellor@gmail.com;Clauscounsellor@gmail.com;Maribellecounsellor@gmail.com;Idalinacounsellor@gmail.com;Ladellcounsellor@gmail.com;Jaquenettecounsellor@gmail.com;Hallycounsellor@gmail.com;Adrianecounsellor@gmail.com;Kemalcounsellor@gmail.com;Jayniecounsellor@gmail.com;Skipcounsellor@gmail.com;Shiucounsellor@gmail.com;Blinnicounsellor@gmail.com;Tuhinacounsellor@gmail.com;Roricounsellor@gmail.com;Valliercounsellor@gmail.com;Moriscounsellor@gmail.com;Izzycounsellor@gmail.com;Norinacounsellor@gmail.com;Frasercounsellor@gmail.com;Thriftcounsellor@gmail.com;Helmuthcounsellor@gmail.com;Hideocounsellor@gmail.com;Tricounsellor@gmail.com;Brencounsellor@gmail.com;Cristiancounsellor@gmail.com;Dodiecounsellor@gmail.com;Maryacounsellor@gmail.com;Nancecounsellor@gmail.com;Norviecounsellor@gmail.com;Sanjaycounsellor@gmail.com;Iviecounsellor@gmail.com;Gaylenecounsellor@gmail.com;Dionecounsellor@gmail.com;Wilhelminecounsellor@gmail.com;Rickiecounsellor@gmail.com;Tildiecounsellor@gmail.com;Henkcounsellor@gmail.com;Gilliancounsellor@gmail.com;Gracecounsellor@gmail.com;Jasvercounsellor@gmail.com;Lilincounsellor@gmail.com;Zdenkacounsellor@gmail.com;Lexiecounsellor@gmail.com;Leneecounsellor@gmail.com;Millardcounsellor@gmail.com;Otheliacounsellor@gmail.com;Merielcounsellor@gmail.com;Devcounsellor@gmail.com;Benthemcounsellor@gmail.com;Heloisecounsellor@gmail.com;Eliascounsellor@gmail.com;Madalyncounsellor@gmail.com;Concettinacounsellor@gmail.com;Lysecounsellor@gmail.com;Cheukcounsellor@gmail.com;Morgannecounsellor@gmail.com;Miwacounsellor@gmail.com;Vadicounsellor@gmail.com;Taccounsellor@gmail.com;Shircounsellor@gmail.com;Tadeuszcounsellor@gmail.com;Sashacounsellor@gmail.com;Zavencounsellor@gmail.com;Shermancounsellor@gmail.com;Rudolphcounsellor@gmail.com;Felicecounsellor@gmail.com;Raynellcounsellor@gmail.com;Danacounsellor@gmail.com;Mocounsellor@gmail.com;paolinacounsellor@gmail.com;dyannecounsellor@gmail.com;nissycounsellor@gmail.com;amaleecounsellor@gmail.com;beverleecounsellor@gmail.com;perricounsellor@gmail.com;maryellencounsellor@gmail.com;christianecounsellor@gmail.com;lynnellcounsellor@gmail.com;ernestacounsellor@gmail.com;eboneecounsellor@gmail.com;cassandrycounsellor@gmail.com;julianncounsellor@gmail.com;marycounsellor@gmail.com;chrystelcounsellor@gmail.com;minervacounsellor@gmail.com;clairecounsellor@gmail.com;nadiacounsellor@gmail.com;adriannacounsellor@gmail.com;aubriecounsellor@gmail.com;jandycounsellor@gmail.com;lenkacounsellor@gmail.com;joyancounsellor@gmail.com;xeniacounsellor@gmail.com;lulitacounsellor@gmail.com;pammicounsellor@gmail.com;blondiecounsellor@gmail.com;sabracounsellor@gmail.com;jennicounsellor@gmail.com;isadoracounsellor@gmail.com;christynacounsellor@gmail.com;dioncounsellor@gmail.com;deenacounsellor@gmail.com;rosaliecounsellor@gmail.com;minnniecounsellor@gmail.com;leshiacounsellor@gmail.com;klarikacounsellor@gmail.com;tillycounsellor@gmail.com;lyndsiecounsellor@gmail.com;noliecounsellor@gmail.com;donnajeancounsellor@gmail.com;carmellacounsellor@gmail.com;robiniacounsellor@gmail.com;letiziacounsellor@gmail.com;gerladinacounsellor@gmail.com;dehliacounsellor@gmail.com;rafaeliacounsellor@gmail.com;zanetacounsellor@gmail.com;ailiscounsellor@gmail.com"
store = store.split(";")
counter = 0
hold = ""
extt = f.read().strip().split('\n')
hold = extt[0] + '\n'
for i in extt[1:]:
	hold += i + store[counter] + '\n'
	counter += 1
f.close()
f2 = open('c.csv', 'w')
f2.write(hold)
f2.close()
"""