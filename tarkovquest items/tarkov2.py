import json

# 파일 경로 설정
inventory_file = 'inventory.json'

# 상인별 아이템 목록
default_quest_items = {
    "프라퍼": {
        "ak60발탄창": 3,
        "하프마스크": 7,
        "스케브단검": 5,
        "ak74n": 1,
        "m4a1": 1,
        "pm": 2,
        "탱크베터리": 1,
        "OFZ": 5,
        "베어독택": 20,
    },
    "스키어": {
        "3m": 1,
        "토즈": 1,
        "usb": 2,
        "2m마스크": 4,
        "체혈세트": 3,
        "광신도칼": 12,
    },
    "피스키퍼": {
        "wd-40": 1,
        "클린": 2,
        "옥스": 2,
        "모르핀": 4,
        "알칼리": 2,
        "호스": 4,
        "프로판": 2,
        "군용라디오": 6,
        "벌텍스": 7,
        "3btg": 1,
        "l1": 1,
        "p22": 1,
        "ahf1-m": 1,
        "멜도닌": 1,
        "옥돌": 1,
        "뮬": 1,
        "rfid": 5,
        "mfd": 4,  # 군용 플래시 드라이버
        "vpx": 5,
        "베어독택50이상": 20,
        "유섹독택50이상": 20,
        "방해독택": 20,
    },
    "테라피스트": {
        "살레와": 3,
        "가스분석기": 3,
        "모르핀": 4,
        "투숀카소": 15,
        "자동차베터리": 4,
        "플러그": 8,
        "검안경": 4,
        "레덱스": 3,
        "제새동기": 5,
        "약더미": 20,
        "비타민": 10,
    },
    "메카닉": {
        "파워코드": 2,
        "t플러그": 4,
        "pcb": 5,
        "글카": 3,
        "cpu팬": 15,
        "cpu": 3,
        "충전지": 3,
        "g폰": 7,
        "말보루": 5,
        "스트라이크": 5,
        "윌스턴": 5,
        "rfid": 1,
        "vpx": 1,
        "와이어": 5,
        "캡": 5,
        "ec": 4,
        "가스분석기": 4,
        "sj1": 15,
        "sj6": 5,
        "sj9": 1,
        "픽셀글라스": 2,
        "청색테이프": 1,
        "mcb": 2,
        "LCD": 1,
    },
    "레그맨": {
        "우샨카": 2,
        "카우보이모자": 2,
        "스키마스크": 1,
        "블랙락": 2,
        "wtrig": 2,
        "연료첨가제": 4,
        "아라미드": 5,
        "립스톱": 10,
        "코듀라": 10,
        "플리스": 10,
        "파라코드": 3,
        "kek": 5,  # kek 테이프
        "보드카": 10,
        "위스키": 10,
        "맥주": 20,
        "필그림": 1,
        "사자상": 2,
        "꽃병": 2,
        "고양이": 1,
        "말": 2,
        "주전자": 3,
        "롤러": 1,
        "달걀": 1,
        "까마귀": 2,
        "앵무새": 1,
        "정재수": 3,
        "6b13 50%": 1,  
        "6b13 100%": 1,
    },
    "예거": {
        "이스크라": 3,
        "누들": 2,
        "투숀카큰거": 2,
        "황금tt": 1,
        "킬라뚝": 1,
        "샷따키": 1,
        "타길라모자": 1,
        "엑세스키카드": 2,
        "cms": 1,
        "소세지": 1,
    },
    "팬스": {
        "부시": 1,
        "도끼": 1,
        "책": 1,
        "기름": 1,
        "뱃지": 1,
        "수염기름": 1,
        "황금폰": 1,
        "마요": 1,
        "콧수염": 1,
        "커피콩": 1,
        "시그니쳐차": 1,
        "스모크발라클라바": 1,
        "렛콜라": 1,
        "달걀": 1,
        "앵무새": 1,
        "붉은수염": 1,
        "베이크북": 1,
        "지게차키": 1,
        "닭": 1,
        "룻로드": 1,
        "역병의사마스크": 1,
        "까마귀": 1,
        "스프렛": 1,
        "코큰비니": 1,
        "슈라우드": 1,
        "베리타스": 1,
        "엡실론": 1,
        "wz지갑": 1,
        "쥐약": 1,
        "버디베어": 1,
        "긴기": 1,
        "DRD": 1,
        "글로리우스마스크": 1,
    },
}

# 인벤토리 파일에서 데이터 로드
def load_inventory():
    try:
        with open(inventory_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return default_quest_items
    except json.JSONDecodeError:
        print("error_code:나는 HTML 프로그레머다!!")
        return default_quest_items

def reset_inventory():
    with open(inventory_file, 'w') as file:
        json.dump(default_quest_items, file, ensure_ascii=False, indent=4)
    print("필요 아이템 갯수가 초기화 되었습니다. 설마... 자체 초기화...?")

# 인벤토리 파일에 데이터 저장
def save_inventory(inventory):
    try:
        with open(inventory_file, 'w') as file:
            json.dump(inventory, file, ensure_ascii=False, indent=4)
    except IOError:
        print("파일 저장 오류 삐빅 HTML은 프로그래밍 언어가 아닙니다.")

# 인벤토리 데이터 로드
inventory = load_inventory()

def print_inventory(category):
    items = inventory.get(category, {})
    print(f"\n{category}의 현재 필요한 퀘스트 아이템 수량:")
    for item, count in items.items():
        print(f"{item}: {count}개")

print_inventory("프라퍼")  # 기본 상인으로 프라퍼를 설정

# 제출된 품목과 수량을 기록
submitted_items = {}

# 사용자로부터 품목과 수량을 입력받아 차감
while True:
    category = input("\n상인 이름을 입력하세요 (예: '프라퍼', '테라피스트') 또는 '종료'를 입력하세요: ")
    
    if category == "종료":
        break
    
    if category not in inventory:
        print("현재 퀘스트에 필요하신 상인 이름이 아니에요!")
        continue
    
    item_name = input("\n품목 이름을 입력하세요: ")
    
    if item_name == "종료":
        break
    
    items = inventory.get(category, {})
    
    if item_name not in items:
        print("현재 퀘스트에 필요하신 아이템이 아니에요!")
        continue
    
    try:
        quantity = int(input(f"{item_name}의 수량을 입력해주세요: "))
    except ValueError:
        print("숫자만 입력 가능합니다.")
        continue
    
    if quantity <= 0:
        print("수량은 1 이상이어야 합니다.")
        continue
    
    if items[item_name] >= quantity:
        items[item_name] -= quantity
        
        # 제출된 품목과 수량 기록하기
        if item_name in submitted_items:
            submitted_items[item_name] += quantity
        else:
            submitted_items[item_name] = quantity
        print(f"{item_name}의 수량이 {quantity}개 차감되었습니다.")
    else:
        print(f"{item_name}의 재고가 부족합니다. 현재 수량: {items[item_name]}개")
    
    # 현재 필요한 퀘스트 아이템 수량 출력
    print_inventory(category)

# 인벤토리 아이템 저장
save_inventory(inventory)

# 종료 시 제출된 아이템과 수량 출력
print("\n제출된 품목과 수량은:")
for item, quantity in submitted_items.items():
    print(f"{item}: {quantity}개")

print("오늘 하루도 고생하셨어요!")

# 본 코드는 아직 시연 단계이며 여러분들의 피드백을 받아 점차 개선해 나갈 것입니다. 많은 피드백 부탁드립니다!
# 개선할 점은 디코 DM으로 해주시거나 댓글 남겨주세요!!
