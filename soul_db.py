# soul_db.py : 60갑자(Sixty Pillars) 데이터 생성 및 해석 엔진

def get_60_pillar_data(index):
    """
    0~59 사이의 인덱스를 받아서 해당되는 60갑자의 영어 이름과 해석을 반환
    """
    
    # 1. 10천간 (Elements & Colors)
    stems = [
        {"ko": "갑", "element": "Wood", "color": "Green", "adj": "Unbending", "desc": "a towering tree with leadership"}, # 0
        {"ko": "을", "element": "Wood", "color": "Green", "adj": "Resilient", "desc": "a surviving vine with adaptability"}, # 1
        {"ko": "병", "element": "Fire", "color": "Red", "adj": "Blazing", "desc": "the mid-day sun with passion"}, # 2
        {"ko": "정", "element": "Fire", "color": "Red", "adj": "Warm", "desc": "a candlelight guiding others"}, # 3
        {"ko": "무", "element": "Earth", "color": "Yellow", "adj": "Majestic", "desc": "a huge mountain with trust"}, # 4
        {"ko": "기", "element": "Earth", "color": "Yellow", "adj": "Nurturing", "desc": "fertile soil raising life"}, # 5
        {"ko": "경", "element": "Metal", "color": "White", "adj": "Sharp", "desc": "raw iron with justice"}, # 6
        {"ko": "신", "element": "Metal", "color": "White", "adj": "Polished", "desc": "a precious gem with precision"}, # 7
        {"ko": "임", "element": "Water", "color": "Black", "adj": "Vast", "desc": "the deep ocean with wisdom"}, # 8
        {"ko": "계", "element": "Water", "color": "Black", "adj": "Mysterious", "desc": "mist and rain with intuition"}, # 9
    ]

    # 2. 12지지 (Animals)
    branches = [
        {"ko": "자", "animal": "Rat", "trait": "smart and secretive"}, # 0
        {"ko": "축", "animal": "Ox", "trait": "diligent and enduring"}, # 1
        {"ko": "인", "animal": "Tiger", "trait": "brave and adventurous"}, # 2
        {"ko": "묘", "animal": "Rabbit", "trait": "gentle and sensitive"}, # 3
        {"ko": "진", "animal": "Dragon", "trait": "ambitious and charismatic"}, # 4
        {"ko": "사", "animal": "Snake", "trait": "wise and sharp"}, # 5
        {"ko": "오", "animal": "Horse", "trait": "free and energetic"}, # 6
        {"ko": "미", "animal": "Sheep", "trait": "peaceful and artistic"}, # 7
        {"ko": "신", "animal": "Monkey", "trait": "clever and versatile"}, # 8
        {"ko": "유", "animal": "Rooster", "trait": "precise and observant"}, # 9
        {"ko": "술", "animal": "Dog", "trait": "loyal and honest"}, # 10
        {"ko": "해", "animal": "Pig", "trait": "generous and optimistic"}, # 11
    ]

    # 3. 계산 로직 (인덱스로 천간/지지 찾기)
    stem_idx = index % 10
    branch_idx = index % 12
    
    stem = stems[stem_idx]
    branch = branches[branch_idx]

    # 4. 60갑자 영어 네이밍 생성 (예: Green Wood Rat)
    english_name = f"{stem['color']} {stem['element']} {branch['animal']}"
    
    # 5. 핵심 키워드 조합
    keywords = [stem['adj'], branch['trait'].split()[0].capitalize(), "Destiny"]

    # 6. 성격 해석 문장 생성 (Template)
    description = (
        f"You possess the energy of the **{english_name}**.\n\n"
        f"Your core essence is like **{stem['desc']}**, "
        f"grounded in the spirit of a **{branch['animal']}** that is {branch['trait']}.\n\n"
        f"This combination makes you unique: you have the {stem['element']}'s desire to manifest "
        f"mixed with the {branch['animal']}'s instinct."
    )

    # 7. 특별한 일주 (백호살, 괴강살 등) - 재미를 위해 몇 개만 하드코딩 추가
    # 예: 갑자 (Green Rat)
    if index == 0: 
        description += "\n\n✨ **Special Note:** You are the start of the 60-year cycle. A born leader."
    # 예: 경진 (White Dragon - 괴강)
    if index == 16:
        description += "\n\n🔥 **Special Aura:** You have 'Kui-Gang' energy. Extremely powerful leadership and charisma."
    # 예: 병오 (Red Horse - 양인)
    if index == 42:
        description += "\n\n🔥 **Special Aura:** You are the Burning Sun at noon. Unstoppable energy."

    return {
        "name": english_name,
        "keywords": keywords,
        "desc": description,
        "element_img": stem['element'] # 이미지 매칭용
    }
