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
@app.route('/dictionary/characters', methods=['POST'])
def dictionary_characters():
    return 1
#정령 도감:DB에 있는 정령도감정보들
@app.route('/dictionary/sprites', methods=['POST'])
def dictionary_sprites():
    return 1
#지팡이 도감:DB에 있는 지팡이도감정보들
@app.route('/dictionary/wands', methods=['POST'])
def dictionary_wands():
    return 1
#지역 도감:DB에 있는 지역도감정보들
@app.route('/dictionary/region', methods=['POST'])
def dictionary_region():
    return 1
#몬스터 도감:DB에 있는 몬스터도감정보들
@app.route('/dictionary/monsters', methods=['POST'])
def dictionary_monsters():
    return 1
#아이템 도감:DB에 있는 아이템도감정보들
@app.route('/dictionary/items', methods=['POST'])
def dictionary_items():
    return 1
#연대기 버튼:
 
#메인 퀘스트: 메인퀘스트도감 TBL에서,가문 TBL에서 메인퀘스트
@app.route('/quest/main/mine', methods=['POST'])
def main_quest():
    return 1
#서브 퀘스트: 서브퀘스트도감 TBL에서,가문 TBL에서 서브퀘스트
@app.route('/quest/sub/mine', methods=['POST'])
def sub_quest():
    return 1




######모험버튼을 눌렀을 때(모험지도)
##chapter ID 정보 보내줌#
@app.route('user/myadventure/map', methods=['POST'])
def get_myadventure():
    return 1



########상점버튼을 눌렀을 때
####오늘쪽 UI에선 내꺼를 팔 수 있음####
##User TBL에서 가지고 있는 무기, 소비품, 기타 목록들의 정보들이 보내짐
#맨 오른쪽 UI에 무기별로, 소비품별로, 기타물품별로 띄워지는건 클라이언트에서 
@app.route('/store/myitems', methods=['POST'])
def get_user_items():
    return 1
##오른쪽 UI에서 아이템을 누르면 판매 탭이 보이고 판매를 누르면 DB아이템 목록에서 제거되고 
##그 값만큼 User TBL에 GOLD 추가
@app.route('/store/sellitems', methods=['POST'])
def sell_user_items():
    return 1
####왼쪽 UI에는 상점 아이템####
##왼쪽 UI에서 특수화폐상점 탭을 누르면: CachItemInfo 테이블에서 정보가 보내짐 
@app.route('/store/cashitems', methods=['POST'])
def get_cash_items():
    return 1
##아이템을 누르면 구매 탭이 나오고 그걸 누르면 DB내 아이템에 [아이템이름][유저ID]로 구매정보 추가, 
##아이템 가격만큼 DB 바론(Cash)에서 감소
@app.route('/store/cashitems/buy', methods=['POST'])
def buy_cash_items():
    return 1
##왼쪽 UI에서 소비품상점 탭을 누르면: NOT YET..

##왼쪽 UI에서 골드상점 탭을 누르면: StoreItemInfo 테이블에서 정보가 보내짐
@app.route('/store/golditems', methods=['POST'])
def get_gold_items():
    return 1
##아이템을 누르면 구매 탭이 나오고 그걸 누르면 DB내 아이템에 [아이템이름][유저ID]로 구매정보 추가, 
##아이템 가격만큼 DB GOLD에서 감소
@app.route('/store/golditems/buy', methods=['POST'])
def but_gold_items():
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
##    클릭된 지팡이가 디비에 selected 지팡이로 저장되어야 함.
@app.route('/user/selects/wand', methods=['POST'])
def user_selects_wand():
    return 1
##소비품을 탭 눌렀을 때: 레시피에 쓰이는 재료들이 보여짐
@app.rounte('/user/inventory/consume', methods=['POST'])
def get_user_consume():
    return 1
@app.rounte('/user/selects/consume', methods=['POST'])
def user_selects_consume():
    return 1
##기타를 탭 눌렀을 때: 나머지 아이템들이 보여짐 (어떤 아이템인지 모르지만 스킨 탈것 펫 하수인이라면 클릭된 것들은 디비에 selected로 저장.)
@app.rounte('/user/inventory/etc', methods=['POST'])
def get_user_etc():
    return 1
@app.rounte('/user/selects/etc', methods=['POST'])
def user_selects_etc():
    return 1


#######소환술버튼을 눌렀을 때
##디비에 User가 가지고 있는 정령들 정보를 클라이언트로 보냄
@app.route('/user/prites/info', methods=['POST'])
def get_user_sprites():
    return 1
#(가나다순을 누르면)가지고 있는 정령들이 가나다로 정렬
#(속성별을 누르면)가지고 있는 정령들이 속성별로 정렬
#(등급별을 누르면)가지고 있는 정령들이 등급별로 정렬
##(왼쪽UI)최대 3개 선택된 정령들이 User(가문테이블)에 selected 정령들에 저장되어야함.
@app.rounte('/user/selects/sprites', methods=['POST'])
def user_selects_sprites():
    return 1
#(왼쪽UI)선택된 정령들의 보유 스킬들이 보여짐



########캐릭터리스트를 눌렀을 때_일단 PASS....
##user가 가지고 있는 캐릭터들 다 불러옴.
##클릭한 캐릭터는 가문테이블에 업데이트




#######################################################

if __name__ == '__main__':
    app.run(debug = True)