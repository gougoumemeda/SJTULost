# coding: utf-8
from django.http import HttpResponse

import lost.models as Models

def init_database(request):
    Item1 = Models.ItemType(description='钥匙')
    Item1.save()
    Item2 = Models.ItemType(description='钱包')
    Item2.save()
    Item3 = Models.ItemType(description='手机')
    Item3.save()

    user1 = Models.User(phone='18017126712', name=u'金嘉骏', student_number='5130309578')
    user1.save()
    user2 = Models.User(phone='15098888888', name=u'胡逸飞', student_number='5130309549')
    user2.save()

    place1 = Models.Place(description=u'东转篮球场')
    place1.save()
    place2 = Models.Place(description=u'二餐')
    place2.save()

    finding1 = Models.Finding(user_id=user1, description=u'我的钱包掉了,求助!', pay=3.4, state=0,
                              image='http://7xtbqj.com2.z0.glb.clouddn.com/qwt.jpg', place_detail=u'应该是掉在东转篮球场!',
                              lost_time='2016-01-24 15:00:00')
    finding1.save()
    finding1.place_ids.add(place1)
    finding1.type_id.add(Item2)
    finding2 = Models.Finding(user_id=user1, description='我的手机掉了,求助!', pay=4.9, state=0,
                              image='http://7xtbqj.com2.z0.glb.clouddn.com/qwt.jpg', place_detail='肯定掉在食堂了!',
                              lost_time='2016-01-22 09:00:00')
    finding2.save()
    finding2.place_ids.add(place2)
    finding2.type_id.add(Item3)
    finding3 = Models.Finding(user_id=user1, description=u'我的钥匙掉了,救命啊!!!!', pay=9, state=0,
                              image='http://7xtbqj.com2.z0.glb.clouddn.com/qwt.jpg', place_detail=u'可能在东转吧, 也可能在食堂!',
                              lost_time='2016-02-09 15:00:00')
    finding3.save()
    finding3.place_ids.add(place1)
    finding3.place_ids.add(place2)
    finding3.type_id.add(Item1)
    finding4 = Models.Finding(user_id=user2, description=u'钱包手机都没了,心好累', pay=15, state=0,
                              image='http://7xtbqj.com2.z0.glb.clouddn.com/5130309578.jpg', place_detail=u'可能在食堂吧!',
                              lost_time='2016-02-18 13:00:00')
    finding4.save()
    finding4.place_ids.add(place2)
    finding4.type_id.add(Item2)
    finding4.type_id.add(Item3)
    finding5 = Models.Finding(user_id=user2, description=u'新买的iphone6没了', pay=7.7, state=0,
                              image='http://7xtbqj.com2.z0.glb.clouddn.com/qwt.jpg', place_detail=u'绝对在东转!',
                              lost_time='2016-04-12 22:00:00')
    finding5.save()
    finding5.place_ids.add(place1)
    finding5.type_id.add(Item3)

    found1 = Models.Found(user_id=user1, description=u'捡到一个手机', state=0,
                          image='http://7xtbqj.com2.z0.glb.clouddn.com/qwt.jpg', place_id=place1,
                          place_detail=u'可能在东转吧',
                          found_time='2016-03-13 10:00:00')
    found1.save()
    found1.type_id.add(Item3)
    found2 = Models.Found(user_id=user2, description=u'谁的钥匙掉了?', state=0,
                          image='http://7xtbqj.com2.z0.glb.clouddn.com/5130309578.jpg', place_id=place2,
                          place_detail=u'在食堂找到的!',
                          found_time='2016-03-19 12:00:00')
    found2.save()
    found2.type_id.add(Item1)
    return HttpResponse(u'Initialization Complete!')
