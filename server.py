#-*- coding:utf-8 -*-
from flask import Flask, request, jsonify, render_template
from dao import database
import pymysql
import json

app = Flask(__name__)

###################################



######################
###########로그인 후 기본화면######

######도감버튼을 눌렀을 때
#캐릭터 도감:DB에 있는 캐릭터도감정보들..?
@app.route('/dictionary/characters', methods=['GET'])
def dictionary_characters():
    data = database.GetDictionaryInfo('CharacterInfo')
    res = list()
    for i in range(len(data)):
        res.append({
            "character_key" : data[i][0],
            "name" : data[i][1],
            "description": data[i][2],
            "term" : data[i][3]
        })
    return json.dumps(res,ensure_ascii=False)
#정령 도감:DB에 있는 정령도감정보들
@app.route('/dictionary/sprites', methods=['GET'])
def dictionary_sprites():
    data = database.GetDictionaryInfo('SpriteInfo')
    return 1
#지팡이 도감:DB에 있는 지팡이도감정보들
@app.route('/dictionary/wands', methods=['GET'])
def dictionary_wands():
    data = database.GetDictionaryInfo('WandInfo')
    return 1
#지역 도감:DB에 있는 지역도감정보들
@app.route('/dictionary/region', methods=['GET'])
def dictionary_region():
    return 1
#몬스터 도감:DB에 있는 몬스터도감정보들
@app.route('/dictionary/monsters', methods=['GET'])
def dictionary_monsters():
    data = database.GetDictionaryInfo('SpriteInfo')
    return 1
#아이템 도감:DB에 있는 아이템도감정보들
@app.route('/dictionary/items', methods=['GET'])
def dictionary_items():
    data = database.GetDictionaryInfo('ItemInfo')
    return 1
#연대기 버튼:
 
#메인 퀘스트: 메인퀘스트도감 TBL에서,가문 TBL에서 메인퀘스트
@app.route('/quest/main/mine', methods=['POST'])
def main_quest():
    data = database.GetDictionaryInfo('StoryInfo')
    return 1
#서브 퀘스트: 서브퀘스트도감 TBL에서,가문 TBL에서 서브퀘스트
@app.route('/quest/sub/mine', methods=['POST'])
def sub_quest():
    return 1

########캐릭터 버튼 클릭했을 때##########

@app.route('character/character/main',methods=['POST'])
def character_character_main():
    data = request.get_json()
    return 1

@app.route('character/skin/main',methods=['POST'])
def character_skin_main():
    data = request.get_json()
    return 1

@app.route('character/pet/main',methods=['POST'])
def character_pet_main():
    data = request.get_json()
    return 1

@app.route('character/ride/main',methods=['POST'])
def character_ride_main():
    data = request.get_json()
    return 1

@app.route('character/servant/main',methods=['POST'])
def character_servant_main():
    data = request.get_json()
    return 1

##끌어다놓을때

@app.route('character/character/select',methods=['POST'])
def character_character_main():
    data = request.get_json()
    return 1

@app.route('character/skin/select',methods=['POST'])
def character_skin_main():
    data = request.get_json()
    return 1

@app.route('character/pet/select',methods=['POST'])
def character_pet_main():
    data = request.get_json()
    return 1

@app.route('character/ride/select',methods=['POST'])
def character_ride_main():
    data = request.get_json()
    return 1

@app.route('character/servant/select',methods=['POST'])
def character_servant_main():
    data = request.get_json()
    return 1

#################################

######상점버튼을 눌렀을때#########
@app.route('store/main',methods=['POST'])
def store_main():
    data = request.get_json()
    return 1

@app.route('store/main/left/consume',methods=['POST'])
def store_main_left_consume():
    data = request.get_json()
    return 1

@app.route('store/main/left/gold',methods=['POST'])
def store_main_left_gold():
    data = request.get_json()
    return 1

@app.route('store/main/left/baron',methods=['POST'])
def store_main_left_baron():
    data = request.get_json()
    return 1

@app.route('store/main/right/wand',methods=['POST'])
def store_main_right_wand():
    data = request.get_json()
    return 1

@app.route('store/main/right/consume',methods=['POST'])
def store_main_right_consume():
    data = request.get_json()
    return 1

@app.route('store/main/right/etc',methods=['POST'])
def store_main_right_etc():
    data = request.get_json()
    return 1

#########판매#########

@app.route('store/sell/left/consume',methods=['POST'])
def store_sell_left_consume():
    data = request.get_json()
    return 1

@app.route('store/sell/left/gold',methods=['POST'])
def store_sell_left_gold():
    data = request.get_json()
    return 1

@app.route('store/sell/left/baron',methods=['POST'])
def store_sell_left_baron():
    data = request.get_json()
    return 1

@app.route('store/sell/right/wand',methods=['POST'])
def store_sell_right_wand():
    data = request.get_json()
    return 1

@app.route('store/sell/right/consume',methods=['POST'])
def store_sell_right_consume():
    data = request.get_json()
    return 1

@app.route('store/sell/right/etc',methods=['POST'])
def store_sell_right_etc():
    data = request.get_json()
    return 1


######모험버튼을 눌렀을 때(모험지도)
##chapter ID 정보 보내줌#
@app.route('user/myadventure/map', methods=['POST'])
def get_myadventure():
    return 1



#######가방버튼을 눌렀을 때
##인벤_선택창: User의 Selected 캐릭터, 지팡이, 스킨, 탈것, 펫, 하수인 정보 가져옴.
@app.route('/user/family/selected/info', methods=['POST'])
def get_user_family_selected():
    return 1
##지팡이 탭 눌렀을 때: 가문의 가지고 있는 지팡이들 보여줌
@app.route('/user/inventory/wand', methods=['POST'])
def get_user_wands():
    return 1
##소비품을 탭 눌렀을 때: 레시피에 쓰이는 재료들이 보여짐
@app.rounte('/user/inventory/consume', methods=['POST'])
def get_user_consume():
    return 1
##기타를 탭 눌렀을 때: 나머지 아이템들이 보여짐 (어떤 아이템인지 모르지만 스킨 탈것 펫 하수인이라면 클릭된 것들은 디비에 selected로 저장.)
@app.rounte('/user/inventory/etc', methods=['POST'])
def get_user_etc():
    return 1
##    클릭된 지팡이가 디비에 selected 지팡이로 저장되어야 함.
@app.route('/user/selects/wand', methods=['POST'])
def user_selects_wand():
    return 1


#######소환술버튼을 눌렀을 때
##디비에 User가 가지고 있는 정령들 정보를 클라이언트로 보냄
@app.route('/user/sprites/info', methods=['POST'])
def get_user_sprites():
    return 1
#(가나다순을 누르면)가지고 있는 정령들이 가나다로 정렬
#(속성별을 누르면)가지고 있는 정령들이 속성별로 정렬
#(등급별을 누르면)가지고 있는 정령들이 등급별로 정렬
##(왼쪽UI)최대 3개 선택된 정령들이 User(가문테이블)에 selected 정령들에 저장되어야함.
@app.rounte('/user/selects/sprites1', methods=['POST'])
def user_selects_sprites1():
    return 1
    @app.rounte('/user/selects/sprites2', methods=['POST'])
def user_selects_sprites2():
    return 1
    @app.rounte('/user/selects/sprites3', methods=['POST'])
def user_selects_sprites3():
    return 1
#(왼쪽UI)선택된 정령들의 보유 스킬들이 보여짐



########캐릭터리스트를 눌렀을 때_일단 PASS....
##user가 가지고 있는 캐릭터들 다 불러옴.
##클릭한 캐릭터는 가문테이블에 업데이트


#######################################################

if __name__ == '__main__':
    app.run(debug = True)