#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

info ={
    '河北省':{
        '石家庄市':["长安区","桥东区","桥西区","新华区","井陉矿区"]
        ,'唐山市':["路南区","路北区","古冶区","开平区","丰南区","丰润区"]
        ,'秦皇岛市':["海港区","山海关区","北戴河区","青龙满族自治县","昌黎县"]
        ,'邯郸市':["邯山区","丛台区","复兴区","峰峰矿区","邯郸县"]
    }
    ,'山西省':{
        '太原市':["小店区","迎泽区","杏花岭区","尖草坪区"]
        ,'大同市':["城区","矿区","南郊区","新荣区"]
        ,'阳泉市':["城区","矿区","郊区","平定县"]
        ,'长治市':["城区","郊区","长治县","襄垣县","屯留县"]
    }
    ,'山东省':{
        '济南市':["历下区","市中区","槐荫区","天桥区","历城区"]
        ,'青岛市':["市南区","市北区","四方区","黄岛区"]
        ,'淄博市':["淄川区","张店区","博山区"]
        ,'枣庄市':["市中区","薛城区","峄城区","台儿庄区"]
    }
    ,'河南省':{
        '郑州市':["中原区","二七区","管城回族区","金水区"]
        ,'开封市':["龙亭区","鼓楼区","南关区","郊区","杞县","通许县"]
    }

}

tag =False
while not tag:
    for k in info:
        print(k)
    select1 = input('第一层>>').strip()
    if select1 in info:
        while not tag:
            for k2 in info[select1]:
                print(k2)
            select2 = input('第二层>>').strip()
            if select2 in info[select1]:
                while not tag:
                    for k3 in info[select1][select2]:
                        print(k3)
                    select3 = input('第三层>>').strip()
                    if select3 in info[select1][select2]:
                        print(select1,select2,select3)
                        tag = True
                    elif select3 == 'b':
                        break
                    elif select3 == 'q':
                        print('game over')
                        tag = True
            elif select2 =='b':
                break
            elif select2 =='q':
                print('game over')
                tag =True
    elif select1 == 'b' or select1 =='q':
        print('game over')
        break













