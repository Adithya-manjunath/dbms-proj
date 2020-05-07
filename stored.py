from flask_sqlalchemy import sqlalchemy.Storedprocedure
from flask_sqlalchemy import sqlalchemy.query
from flask_sqlalchemy import sqlalchemy.trigger


class performance(Storedprocedure):

    def getperformance():
        st=Storedprocedure()
        re1=requests.get(f'https://api.opendota.com/api/players/{playerid}/rankings')
        j1=re1.json()
        print(j1)
        id=[d['hero_id'] for d in j1]
        perc=[d['percent_rank'] for d in j1]
        size=len(id)
        print(size)

        playerdict=dict(zip(id,perc))
        print(playerdict)
        odpd=collections.OrderedDict(sorted(playerdict.items()))
        print(odpd)

        perc1=list(odpd.values())
        print(perc1)
        id1=list(odpd.keys())
        print(id1)
        print(len(id1))
        k=0
        result=0
        score=0
        desc=[]

        st.begin():
            while k<size:
                result=perc1[k]
                print(result)
                if result <= 0.2:
                    desc.append("Herald")

                elif result >0.2 and result<=0.3:
                    desc.append("Guardian")


                elif result >0.3 and result<=0.4:
                    desc.append("Crusader")


                elif result >0.4 and result<=0.5:
                    desc.append("Archon")


                elif result >0.5 and result<=0.7:
                    desc.append("Legend")

                elif result>0.7 and result<=0.8:
                    desc.append("Ancient")

                elif result >0.8 and result <=0.9:
                    desc.append("Divine")

                else:
                    desc.append("Immortal")

                k=k+1


        st.end()

        user=hero.query.Storedprocedure(st)

        print(desc)
        names=[]
        k=0
        while k<size:
            nam=hero.query.filter_by(hid=id1[k]).all()
            for n in nam:
                nama=n.hero_name
            names.append(nama)
            k=k+1


        print(names)


        k=0
        while k<size:
            user=player_hero(hero_id=id1[k],score=perc1[k],player_id=playerid,Performance=desc[k],heroname=names[k])
            db.session.add(user)
            db.session.commit()
            k=k+1

class valid(trigger):

    def validate():
        t=trigger()


        user=logo.query.filter_by(id=id.data,trigger=t).first()
        t.beforeinsert()
        if user is not None:
            raise ValidationError("This id is already registered")


        aid=0
        list1=[]
        re1=requests.get(f"https://api.opendota.com/api/players/{id.data}")
        js1=re1.json()
        print(js1)
        for key,values in js1.items():
            if key=='profile':
                list1.append(values)

        print(list1)
        for i in list1:
            if i['account_id']:
                aid=i['account_id']


        print(aid)

        if id.data != aid:
            raise ValidationError("Please enter a valid PlayerID")
