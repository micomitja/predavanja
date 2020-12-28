from collections import defaultdict


def razdeli_besede(slovar):
    po_zacetnicah = defaultdict(set)
    for beseda in slovar:
        po_zacetnicah[beseda[0]].add(beseda)
    return po_zacetnicah


def najboljsa_naslednja(beseda, moznosti, po_crkah):
    naj_naprej = ""
    naj_pogostost = -1
    for naprej in moznosti:
        pogostost = len(po_crkah[naprej[-1]])
        if pogostost > naj_pogostost:
            naj_pogostost = pogostost
            naj_naprej = naprej
    return naj_naprej


from random import random

def najboljsa_naslednja(beseda, moznosti, po_crkah):
    if not moznosti:
        return None

    pogostosti = []
    for naprej in moznosti:
        pogostosti.append((len(po_crkah[naprej[-1]]), naprej))
    pogostosti.sort(reverse=True)
    i = 0
    while i + 1 < len(pogostosti) and (
            pogostosti[i + 1] == pogostosti[i] and random() > 0.2
            or random() > 0.7):
        i += 1
    return pogostosti[i][1]


def sestavi_zaporedje(slovar):
    po_crkah = razdeli_besede(slovar)
    naslednja = najboljsa_naslednja("", slovar, po_crkah)
    veriga = []
    while naslednja:
        po_crkah[naslednja[0]].remove(naslednja)
        veriga.append(naslednja)
        naslednja = najboljsa_naslednja(naslednja, po_crkah[naslednja[-1]], po_crkah)
    return veriga



def najdaljsa_veriga(slovar):
    verige = []
    slovar = set(slovar)
    for prva in slovar:
        verige += nadaljevanja(prva, slovar)
    return verige


def nadaljevanja(beseda, slovar):
    n = [[beseda]]
    for naprej in slovar:
        if naprej[0] == beseda[-1]:
            for podverige in nadaljevanja(naprej, slovar - {beseda}):
                n.append([beseda] + podverige)
    return n


from functools import reduce

def najdaljsa_veriga(slovar):
    return max(reduce(list.__add__, (nadaljevanja(prva, set(slovar)) for prva in slovar), []), key=len)

def nadaljevanja(beseda, slovar):
    return [[beseda] + pod for naprej in slovar if naprej[0] == beseda[-1] for pod in nadaljevanja(naprej, slovar - {beseda})] or [[beseda]]




slovar = ["ABRAHAM", "MELODIJA", "ASTEROID", "DREVO", "MEČ", "OBLAK",
            "KLEPTOMAN", "KAČA", ]

print(najdaljsa_veriga(slovar))


nouns = ['PEOPLE', 'HISTORY', 'WAY', 'ART', 'WORLD', 'INFORMATION', 'MAP',
            'TWO', 'FAMILY', 'GOVERNMENT', 'HEALTH', 'SYSTEM', 'COMPUTER',
            'MEAT', 'YEAR', 'THANKS', 'MUSIC', 'PERSON', 'READING', 'METHOD',
            'DATA', 'FOOD', 'UNDERSTANDING', 'THEORY', 'LAW', 'BIRD',
            'LITERATURE', 'PROBLEM', 'SOFTWARE', 'CONTROL', 'KNOWLEDGE',
            'POWER', 'ABILITY', 'ECONOMICS', 'LOVE', 'INTERNET', 'TELEVISION',
            'SCIENCE', 'LIBRARY', 'NATURE', 'FACT', 'PRODUCT', 'IDEA',
            'TEMPERATURE', 'INVESTMENT', 'AREA', 'SOCIETY', 'ACTIVITY',
            'STORY', 'INDUSTRY', 'MEDIA', 'THING', 'OVEN', 'COMMUNITY',
            'DEFINITION', 'SAFETY', 'QUALITY', 'DEVELOPMENT', 'LANGUAGE',
            'MANAGEMENT', 'PLAYER', 'VARIETY', 'VIDEO', 'WEEK', 'SECURITY',
            'COUNTRY', 'EXAM', 'MOVIE', 'ORGANIZATION', 'EQUIPMENT', 'PHYSICS',
            'ANALYSIS', 'POLICY', 'SERIES', 'THOUGHT', 'BASIS', 'BOYFRIEND',
            'DIRECTION', 'STRATEGY', 'TECHNOLOGY', 'ARMY', 'CAMERA', 'FREEDOM',
            'PAPER', 'ENVIRONMENT', 'CHILD', 'INSTANCE', 'MONTH', 'TRUTH',
            'MARKETING', 'UNIVERSITY', 'WRITING', 'ARTICLE', 'DEPARTMENT',
            'DIFFERENCE', 'GOAL', 'NEWS', 'AUDIENCE', 'FISHING', 'GROWTH',
            'INCOME', 'MARRIAGE', 'USER', 'COMBINATION', 'FAILURE', 'MEANING',
            'MEDICINE', 'PHILOSOPHY', 'TEACHER', 'COMMUNICATION', 'NIGHT',
            'CHEMISTRY', 'DISEASE', 'DISK', 'ENERGY', 'NATION', 'ROAD', 'ROLE',
            'SOUP', 'ADVERTISING', 'LOCATION', 'SUCCESS', 'ADDITION',
            'APARTMENT', 'EDUCATION', 'MATH', 'MOMENT', 'PAINTING', 'POLITICS',
            'ATTENTION', 'DECISION', 'EVENT', 'PROPERTY', 'SHOPPING',
            'STUDENT', 'WOOD', 'COMPETITION', 'DISTRIBUTION', 'ENTERTAINMENT',
            'OFFICE', 'POPULATION', 'PRESIDENT', 'UNIT', 'CATEGORY',
            'CIGARETTE', 'CONTEXT', 'INTRODUCTION', 'OPPORTUNITY',
            'PERFORMANCE', 'DRIVER', 'FLIGHT', 'LENGTH', 'MAGAZINE',
            'NEWSPAPER', 'RELATIONSHIP', 'TEACHING', 'CELL', 'DEALER',
            'FINDING', 'LAKE', 'MEMBER', 'MESSAGE', 'PHONE', 'SCENE',
            'APPEARANCE', 'ASSOCIATION', 'CONCEPT', 'CUSTOMER', 'DEATH',
            'DISCUSSION', 'HOUSING', 'INFLATION', 'INSURANCE', 'MOOD', 'WOMAN',
            'ADVICE', 'BLOOD', 'EFFORT', 'EXPRESSION', 'IMPORTANCE', 'OPINION',
            'PAYMENT', 'REALITY', 'RESPONSIBILITY', 'SITUATION', 'SKILL',
            'STATEMENT', 'WEALTH', 'APPLICATION', 'CITY', 'COUNTY', 'DEPTH',
            'ESTATE', 'FOUNDATION', 'GRANDMOTHER', 'HEART', 'PERSPECTIVE',
            'PHOTO', 'RECIPE', 'STUDIO', 'TOPIC', 'COLLECTION', 'DEPRESSION',
            'IMAGINATION', 'PASSION', 'PERCENTAGE', 'RESOURCE', 'SETTING',
            'AD', 'AGENCY', 'COLLEGE', 'CONNECTION', 'CRITICISM', 'DEBT',
            'DESCRIPTION', 'MEMORY', 'PATIENCE', 'SECRETARY', 'SOLUTION',
            'ADMINISTRATION', 'ASPECT', 'ATTITUDE', 'DIRECTOR', 'PERSONALITY',
            'PSYCHOLOGY', 'RECOMMENDATION', 'RESPONSE', 'SELECTION', 'STORAGE',
            'VERSION', 'ALCOHOL', 'ARGUMENT', 'COMPLAINT', 'CONTRACT',
            'EMPHASIS', 'HIGHWAY', 'LOSS', 'MEMBERSHIP', 'POSSESSION',
            'PREPARATION', 'STEAK', 'UNION', 'AGREEMENT', 'CANCER', 'CURRENCY',
            'EMPLOYMENT', 'ENGINEERING', 'ENTRY', 'INTERACTION', 'MIXTURE',
            'PREFERENCE', 'REGION', 'REPUBLIC', 'TRADITION', 'VIRUS', 'ACTOR',
            'CLASSROOM', 'DELIVERY', 'DEVICE', 'DIFFICULTY', 'DRAMA',
            'ELECTION', 'ENGINE', 'FOOTBALL', 'GUIDANCE', 'HOTEL', 'OWNER',
            'PRIORITY', 'PROTECTION', 'SUGGESTION', 'TENSION', 'VARIATION',
            'ANXIETY', 'ATMOSPHERE', 'AWARENESS', 'BATH', 'BREAD', 'CANDIDATE',
            'CLIMATE', 'COMPARISON', 'CONFUSION', 'CONSTRUCTION', 'ELEVATOR',
            'EMOTION', 'EMPLOYEE', 'EMPLOYER', 'GUEST', 'HEIGHT', 'LEADERSHIP',
            'MALL', 'MANAGER', 'OPERATION', 'RECORDING', 'SAMPLE',
            'TRANSPORTATION', 'CHARITY', 'COUSIN', 'DISASTER', 'EDITOR',
            'EFFICIENCY', 'EXCITEMENT', 'EXTENT', 'FEEDBACK', 'GUITAR',
            'HOMEWORK', 'LEADER', 'MOM', 'OUTCOME', 'PERMISSION',
            'PRESENTATION', 'PROMOTION', 'REFLECTION', 'REFRIGERATOR',
            'RESOLUTION', 'REVENUE', 'SESSION', 'SINGER', 'TENNIS', 'BASKET',
            'BONUS', 'CABINET', 'CHILDHOOD', 'CHURCH', 'CLOTHES', 'COFFEE',
            'DINNER', 'DRAWING', 'HAIR', 'HEARING', 'INITIATIVE', 'JUDGMENT',
            'LAB', 'MEASUREMENT', 'MODE', 'MUD', 'ORANGE', 'POETRY', 'POLICE',
            'POSSIBILITY', 'PROCEDURE', 'QUEEN', 'RATIO', 'RELATION',
            'RESTAURANT', 'SATISFACTION', 'SECTOR', 'SIGNATURE',
            'SIGNIFICANCE', 'SONG', 'TOOTH', 'TOWN', 'VEHICLE', 'VOLUME',
            'WIFE', 'ACCIDENT', 'AIRPORT', 'APPOINTMENT', 'ARRIVAL',
            'ASSUMPTION', 'BASEBALL', 'CHAPTER', 'COMMITTEE', 'CONVERSATION',
            'DATABASE', 'ENTHUSIASM', 'ERROR', 'EXPLANATION', 'FARMER', 'GATE',
            'GIRL', 'HALL', 'HISTORIAN', 'HOSPITAL', 'INJURY', 'INSTRUCTION',
            'MAINTENANCE', 'MANUFACTURER', 'MEAL', 'PERCEPTION', 'PIE', 'POEM',
            'PRESENCE', 'PROPOSAL', 'RECEPTION', 'REPLACEMENT', 'REVOLUTION',
            'RIVER', 'SON', 'SPEECH', 'TEA', 'VILLAGE', 'WARNING', 'WINNER',
            'WORKER', 'WRITER', 'ASSISTANCE', 'BREATH', 'BUYER', 'CHEST',
            'CHOCOLATE', 'CONCLUSION', 'CONTRIBUTION', 'COOKIE', 'COURAGE',
            'DAD', 'DESK', 'DRAWER', 'ESTABLISHMENT', 'EXAMINATION', 'GARBAGE',
            'GROCERY', 'HONEY', 'IMPRESSION', 'IMPROVEMENT', 'INDEPENDENCE',
            'INSECT', 'INSPECTION', 'INSPECTOR', 'KING', 'LADDER', 'MENU',
            'PENALTY', 'PIANO', 'POTATO', 'PROFESSION', 'PROFESSOR',
            'QUANTITY', 'REACTION', 'REQUIREMENT', 'SALAD', 'SISTER',
            'SUPERMARKET', 'TONGUE', 'WEAKNESS', 'WEDDING', 'AFFAIR',
            'AMBITION', 'ANALYST', 'APPLE', 'ASSIGNMENT', 'ASSISTANT',
            'BATHROOM', 'BEDROOM', 'BEER', 'BIRTHDAY', 'CELEBRATION',
            'CHAMPIONSHIP', 'CHEEK', 'CLIENT', 'CONSEQUENCE', 'DEPARTURE',
            'DIAMOND', 'DIRT', 'EAR', 'FORTUNE', 'FRIENDSHIP', 'FUNERAL',
            'GENE', 'GIRLFRIEND', 'HAT', 'INDICATION', 'INTENTION', 'LADY',
            'MIDNIGHT', 'NEGOTIATION', 'OBLIGATION', 'PASSENGER', 'PIZZA',
            'PLATFORM', 'POET', 'POLLUTION', 'RECOGNITION', 'REPUTATION',
            'SHIRT', 'SIR', 'SPEAKER', 'STRANGER', 'SURGERY', 'SYMPATHY',
            'TALE', 'THROAT', 'TRAINER', 'UNCLE', 'YOUTH', 'TIME', 'WORK',
            'FILM', 'WATER', 'MONEY', 'EXAMPLE', 'WHILE', 'BUSINESS', 'STUDY',
            'GAME', 'LIFE', 'FORM', 'AIR', 'DAY', 'PLACE', 'NUMBER', 'PART',
            'FIELD', 'FISH', 'BACK', 'PROCESS', 'HEAT', 'HAND', 'EXPERIENCE',
            'JOB', 'BOOK', 'END', 'POINT', 'TYPE', 'HOME', 'ECONOMY', 'VALUE',
            'BODY', 'MARKET', 'GUIDE', 'INTEREST', 'STATE', 'RADIO', 'COURSE',
            'COMPANY', 'PRICE', 'SIZE', 'CARD', 'LIST', 'MIND', 'TRADE',
            'LINE', 'CARE', 'GROUP', 'RISK', 'WORD', 'FAT', 'FORCE', 'KEY',
            'LIGHT', 'TRAINING', 'NAME', 'SCHOOL', 'TOP', 'AMOUNT', 'LEVEL',
            'ORDER', 'PRACTICE', 'RESEARCH', 'SENSE', 'SERVICE', 'PIECE',
            'WEB', 'BOSS', 'SPORT', 'FUN', 'HOUSE', 'PAGE', 'TERM', 'TEST',
            'ANSWER', 'SOUND', 'FOCUS', 'MATTER', 'KIND', 'SOIL', 'BOARD',
            'OIL', 'PICTURE', 'ACCESS', 'GARDEN', 'RANGE', 'RATE', 'REASON',
            'FUTURE', 'SITE', 'DEMAND', 'EXERCISE', 'IMAGE', 'CASE', 'CAUSE',
            'COAST', 'ACTION', 'AGE', 'BAD', 'BOAT', 'RECORD', 'RESULT',
            'SECTION', 'BUILDING', 'MOUSE', 'CASH', 'CLASS', 'NOTHING',
            'PERIOD', 'PLAN', 'STORE', 'SIDE', 'SUBJECT', 'SPACE',
            'RULE', 'STOCK', 'WEATHER', 'CHANCE', 'FIGURE', 'MAN', 'MODEL',
            'SOURCE', 'BEGINNING', 'EARTH', 'PROGRAM', 'CHICKEN', 'DESIGN',
            'FEATURE', 'HEAD', 'MATERIAL', 'PURPOSE', 'QUESTION', 'ROCK',
            'SALT', 'ACT', 'BIRTH', 'CAR', 'DOG', 'OBJECT', 'SCALE', 'SUN',
            'NOTE', 'PROFIT', 'RENT', 'SPEED', 'STYLE', 'WAR', 'BANK', 'CRAFT',
            'HALF', 'INSIDE', 'OUTSIDE', 'STANDARD', 'BUS', 'EXCHANGE', 'EYE',
            'FIRE', 'POSITION', 'PRESSURE', 'STRESS', 'ADVANTAGE', 'BENEFIT',
            'FRAME', 'ISSUE', 'STEP', 'CYCLE', 'FACE', 'ITEM', 'METAL',
            'PAINT', 'REVIEW', 'ROOM', 'SCREEN', 'STRUCTURE', 'VIEW',
            'ACCOUNT', 'BALL', 'DISCIPLINE', 'MEDIUM', 'SHARE', 'BALANCE',
            'BIT', 'BLACK', 'BOTTOM', 'CHOICE', 'GIFT', 'IMPACT', 'MACHINE',
            'SHAPE', 'TOOL', 'WIND', 'ADDRESS', 'AVERAGE', 'CAREER', 'CULTURE',
            'MORNING', 'POT', 'SIGN', 'TABLE', 'TASK', 'CONDITION', 'CONTACT',
            'CREDIT', 'EGG', 'HOPE', 'ICE', 'NETWORK', 'NORTH', 'SQUARE',
            'ATTEMPT', 'DATE', 'EFFECT', 'LINK', 'POST', 'STAR', 'VOICE',
            'CAPITAL', 'CHALLENGE', 'FRIEND', 'SELF', 'SHOT', 'BRUSH',
            'COUPLE', 'DEBATE', 'EXIT', 'FRONT', 'FUNCTION', 'LACK', 'LIVING',
            'PLANT', 'PLASTIC', 'SPOT', 'SUMMER', 'TASTE', 'THEME', 'TRACK',
            'WING', 'BRAIN', 'BUTTON', 'CLICK', 'DESIRE', 'FOOT', 'GAS',
            'INFLUENCE', 'NOTICE', 'RAIN', 'WALL', 'BASE', 'DAMAGE',
            'DISTANCE', 'FEELING', 'PAIR', 'SAVINGS', 'STAFF', 'SUGAR',
            'TARGET', 'TEXT', 'ANIMAL', 'AUTHOR', 'BUDGET', 'DISCOUNT', 'FILE',
            'GROUND', 'LESSON', 'MINUTE', 'OFFICER', 'PHASE', 'REFERENCE',
            'REGISTER', 'SKY', 'STAGE', 'STICK', 'TITLE', 'TROUBLE', 'BOWL',
            'BRIDGE', 'CAMPAIGN', 'CHARACTER', 'CLUB', 'EDGE', 'EVIDENCE',
            'FAN', 'LETTER', 'LOCK', 'MAXIMUM', 'NOVEL', 'OPTION', 'PACK',
            'PARK', 'PLENTY', 'QUARTER', 'SKIN', 'SORT', 'WEIGHT', 'BABY',
            'BACKGROUND', 'CARRY', 'DISH', 'FACTOR', 'FRUIT', 'GLASS', 'JOINT',
            'MASTER', 'MUSCLE', 'RED', 'STRENGTH', 'TRAFFIC', 'TRIP',
            'VEGETABLE', 'APPEAL', 'CHART', 'GEAR', 'IDEAL', 'KITCHEN', 'LAND',
            'LOG', 'MOTHER', 'NET', 'PARTY', 'PRINCIPLE', 'RELATIVE', 'SALE',
            'SEASON', 'SIGNAL', 'SPIRIT', 'STREET', 'TREE', 'WAVE', 'BELT',
            'BENCH', 'COMMISSION', 'COPY', 'DROP', 'MINIMUM', 'PATH',
            'PROGRESS', 'PROJECT', 'SEA', 'SOUTH', 'STATUS', 'STUFF', 'TICKET',
            'TOUR', 'ANGLE', 'BLUE', 'BREAKFAST', 'CONFIDENCE', 'DAUGHTER',
            'DEGREE', 'DOCTOR', 'DOT', 'DREAM', 'DUTY', 'ESSAY', 'FATHER',
            'FEE', 'FINANCE', 'HOUR', 'JUICE', 'LIMIT', 'LUCK', 'MILK',
            'MOUTH', 'PEACE', 'PIPE', 'SEAT', 'STABLE', 'STORM', 'SUBSTANCE',
            'TEAM', 'TRICK', 'AFTERNOON', 'BAT', 'BEACH', 'BLANK', 'CATCH',
            'CHAIN', 'CONSIDERATION', 'CREAM', 'CREW', 'DETAIL', 'GOLD',
            'INTERVIEW', 'KID', 'MARK', 'MATCH', 'MISSION', 'PAIN', 'PLEASURE',
            'SCORE', 'SCREW', 'SHOP', 'SHOWER', 'SUIT', 'TONE',
            'WINDOW', 'AGENT', 'BAND', 'BLOCK', 'BONE', 'CALENDAR', 'CAP',
            'COAT', 'CONTEST', 'CORNER', 'COURT', 'CUP', 'DISTRICT', 'DOOR',
            'EAST', 'FINGER', 'GARAGE', 'GUARANTEE', 'HOLE', 'HOOK',
            'IMPLEMENT', 'LAYER', 'LECTURE', 'LIE', 'MANNER', 'MEETING',
            'NOSE', 'PARKING', 'PARTNER', 'PROFILE', 'RESPECT', 'RICE',
            'ROUTINE', 'SCHEDULE', 'SWIMMING', 'TELEPHONE', 'TIP', 'WINTER',
            'AIRLINE', 'BAG', 'BATTLE', 'BED', 'BILL', 'BOTHER', 'CAKE',
            'CODE', 'CURVE', 'DESIGNER', 'DIMENSION', 'DRESS', 'EASE',
            'EMERGENCY', 'EVENING', 'EXTENSION', 'FARM', 'FIGHT', 'GAP',
            'GRADE', 'HOLIDAY', 'HORROR', 'HORSE', 'HOST', 'HUSBAND', 'LOAN',
            'MISTAKE', 'MOUNTAIN', 'NAIL', 'NOISE', 'OCCASION', 'PACKAGE',
            'PATIENT', 'PAUSE', 'PHRASE', 'PROOF', 'RACE', 'RELIEF', 'SAND',
            'SENTENCE', 'SHOULDER', 'SMOKE', 'STOMACH', 'STRING', 'TOURIST',
            'TOWEL', 'VACATION', 'WEST', 'WHEEL', 'WINE', 'ARM', 'ASIDE',
            'ASSOCIATE', 'BET', 'BLOW', 'BORDER', 'BRANCH', 'BREAST',
            'BROTHER', 'BUDDY', 'BUNCH', 'CHIP', 'COACH', 'CROSS', 'DOCUMENT',
            'DRAFT', 'DUST', 'EXPERT', 'FLOOR', 'GOD', 'GOLF', 'HABIT', 'IRON',
            'JUDGE', 'KNIFE', 'LANDSCAPE', 'LEAGUE', 'MAIL', 'MESS', 'NATIVE',
            'OPENING', 'PARENT', 'PATTERN', 'PIN', 'POOL', 'POUND', 'REQUEST',
            'SALARY', 'SHAME', 'SHELTER', 'SHOE', 'SILVER', 'TACKLE', 'TANK',
            'TRUST', 'ASSIST', 'BAKE', 'BAR', 'BELL', 'BIKE', 'BLAME', 'BOY',
            'BRICK', 'CHAIR', 'CLOSET', 'CLUE', 'COLLAR', 'COMMENT',
            'CONFERENCE', 'DEVIL', 'DIET', 'FEAR', 'FUEL', 'GLOVE', 'JACKET',
            'LUNCH', 'MONITOR', 'MORTGAGE', 'NURSE', 'PACE', 'PANIC', 'PEAK',
            'PLANE', 'REWARD', 'ROW', 'SANDWICH', 'SHOCK', 'SPITE', 'SPRAY',
            'SURPRISE', 'TILL', 'TRANSITION', 'WEEKEND', 'WELCOME', 'YARD',
            'ALARM', 'BEND', 'BICYCLE', 'BITE', 'BLIND', 'BOTTLE', 'CABLE',
            'CANDLE', 'CLERK', 'CLOUD', 'CONCERT', 'COUNTER', 'FLOWER',
            'GRANDFATHER', 'HARM', 'KNEE', 'LAWYER', 'LEATHER', 'LOAD',
            'MIRROR', 'NECK', 'PENSION', 'PLATE', 'PURPLE', 'RUIN', 'SHIP',
            'SKIRT', 'SLICE', 'SNOW', 'SPECIALIST', 'STROKE', 'SWITCH',
            'TRASH', 'TUNE', 'ZONE', 'ANGER', 'AWARD', 'BID', 'BITTER', 'BOOT',
            'BUG', 'CAMP', 'CANDY', 'CARPET', 'CAT', 'CHAMPION', 'CHANNEL',
            'CLOCK', 'COMFORT', 'COW', 'CRACK', 'ENGINEER', 'ENTRANCE',
            'FAULT', 'GRASS', 'GUY', 'HELL', 'HIGHLIGHT', 'INCIDENT', 'ISLAND',
            'JOKE', 'JURY', 'LEG', 'LIP', 'MATE', 'MOTOR', 'NERVE', 'PASSAGE',
            'PEN', 'PRIDE', 'PRIEST', 'PRIZE', 'PROMISE', 'RESIDENT', 'RESORT',
            'RING', 'ROOF', 'ROPE', 'SAIL', 'SCHEME', 'SCRIPT', 'SOCK',
            'STATION', 'TOE', 'TOWER', 'TRUCK', 'WITNESS', 'A', 'YOU', 'IT',
            'CAN', 'WILL', 'IF', 'ONE', 'MANY', 'MOST', 'OTHER', 'USE', 'MAKE',
            'GOOD', 'LOOK', 'HELP', 'GO', 'GREAT', 'BEING', 'FEW', 'MIGHT',
            'STILL', 'PUBLIC', 'READ', 'KEEP', 'START', 'GIVE', 'HUMAN',
            'LOCAL', 'GENERAL', 'SHE', 'SPECIFIC', 'LONG', 'PLAY', 'FEEL',
            'HIGH', 'TONIGHT', 'PUT', 'COMMON', 'SET', 'CHANGE', 'SIMPLE',
            'PAST', 'BIG', 'POSSIBLE', 'PARTICULAR', 'TODAY', 'MAJOR',
            'PERSONAL', 'CURRENT', 'NATIONAL', 'CUT', 'NATURAL', 'PHYSICAL',
            'SHOW', 'TRY', 'CHECK', 'SECOND', 'CALL', 'MOVE', 'PAY', 'LET',
            'INCREASE', 'SINGLE', 'INDIVIDUAL', 'TURN', 'ASK', 'BUY', 'GUARD',
            'HOLD', 'MAIN', 'OFFER', 'POTENTIAL', 'PROFESSIONAL',
            'INTERNATIONAL', 'TRAVEL', 'COOK', 'ALTERNATIVE', 'FOLLOWING',
            'SPECIAL', 'WORKING', 'WHOLE', 'DANCE', 'EXCUSE', 'COLD',
            'COMMERCIAL', 'LOW', 'PURCHASE', 'DEAL', 'PRIMARY', 'WORTH',
            'FALL', 'NECESSARY', 'POSITIVE', 'PRODUCE', 'SEARCH', 'PRESENT',
            'SPEND', 'TALK', 'CREATIVE', 'TELL', 'COST', 'DRIVE', 'GREEN',
            'SUPPORT', 'GLAD', 'REMOVE', 'RETURN', 'RUN', 'DUE',
            'EFFECTIVE', 'MIDDLE', 'REGULAR', 'RESERVE', 'INDEPENDENT',
            'LEAVE', 'ORIGINAL', 'REACH', 'REST', 'SERVE', 'WATCH',
            'BEAUTIFUL', 'CHARGE', 'ACTIVE', 'BREAK', 'NEGATIVE', 'SAFE',
            'STAY', 'VISIT', 'VISUAL', 'AFFECT', 'COVER', 'REPORT', 'RISE',
            'WALK', 'WHITE', 'BEYOND', 'JUNIOR', 'PICK', 'UNIQUE', 'ANYTHING',
            'CLASSIC', 'FINAL', 'LIFT', 'PRIVATE', 'STOP', 'TEACH',
            'WESTERN', 'CONCERN', 'FAMILIAR', 'FLY', 'OFFICIAL', 'BROAD',
            'COMFORTABLE', 'GAIN', 'MAYBE', 'RICH', 'SAVE', 'STAND', 'YOUNG',
            'FAIL', 'HEAVY', 'HELLO', 'LEAD', 'LISTEN', 'VALUABLE', 'WORRY',
            'HANDLE', 'LEADING', 'MEET', 'RELEASE', 'SELL', 'FINISH', 'NORMAL',
            'PRESS', 'RIDE', 'SECRET', 'SPREAD', 'SPRING', 'TOUGH', 'WAIT',
            'BROWN', 'DEEP', 'DISPLAY', 'FLOW', 'HIT', 'OBJECTIVE', 'SHOOT',
            'TOUCH', 'CANCEL', 'CHEMICAL', 'CRY', 'DUMP', 'EXTREME', 'PUSH',
            'CONFLICT', 'EAT', 'FILL', 'FORMAL', 'JUMP', 'KICK', 'OPPOSITE',
            'PASS', 'PITCH', 'REMOTE', 'TOTAL', 'TREAT', 'VAST', 'ABUSE',
            'BEAT', 'BURN', 'DEPOSIT', 'PRINT', 'RAISE', 'SLEEP', 'SOMEWHERE',
            'ADVANCE', 'ANYWHERE', 'CONSIST', 'DARK', 'DOUBLE', 'DRAW',
            'EQUAL', 'HIRE', 'INTERNAL', 'JOIN', 'KILL', 'SENSITIVE',
            'TAP', 'WIN', 'ATTACK', 'CLAIM', 'CONSTANT', 'DRAG', 'DRINK',
            'GUESS', 'MINOR', 'PULL', 'RAW', 'SOFT', 'SOLID', 'WEAR', 'WEIRD',
            'WONDER', 'ANNUAL', 'COUNT', 'DEAD', 'DOUBT', 'FEED', 'FOREVER',
            'IMPRESS', 'NOBODY', 'REPEAT', 'ROUND', 'SING', 'SLIDE', 'STRIP',
            'WHEREAS', 'WISH', 'COMBINE', 'COMMAND', 'DIG', 'DIVIDE',
            'EQUIVALENT', 'HANG', 'HUNT', 'INITIAL', 'MARCH', 'MENTION',
            'SMELL', 'SPIRITUAL', 'SURVEY', 'TIE', 'ADULT', 'BRIEF', 'CRAZY',
            'ESCAPE', 'GATHER', 'HATE', 'PRIOR', 'REPAIR', 'ROUGH', 'SAD',
            'SCRATCH', 'SICK', 'STRIKE', 'EMPLOY', 'EXTERNAL', 'HURT',
            'ILLEGAL', 'LAUGH', 'LAY', 'MOBILE', 'NASTY', 'ORDINARY',
            'RESPOND', 'ROYAL', 'SENIOR', 'SPLIT', 'STRAIN', 'STRUGGLE',
            'SWIM', 'TRAIN', 'UPPER', 'WASH', 'YELLOW', 'CONVERT', 'CRASH',
            'DEPENDENT', 'FOLD', 'FUNNY', 'GRAB', 'HIDE', 'MISS', 'PERMIT',
            'QUOTE', 'RECOVER', 'RESOLVE', 'ROLL', 'SINK', 'SLIP', 'SPARE',
            'SUSPECT', 'SWEET', 'SWING', 'TWIST', 'UPSTAIRS', 'USUAL',
            'ABROAD', 'BRAVE', 'CALM', 'CONCENTRATE', 'ESTIMATE', 'GRAND',
            'MALE', 'MINE', 'PROMPT', 'QUIET', 'REFUSE', 'REGRET', 'REVEAL',
            'RUSH', 'SHAKE', 'SHIFT', 'SHINE', 'STEAL', 'SUCK', 'SURROUND',
            'ANYBODY', 'BEAR', 'BRILLIANT', 'DARE', 'DEAR', 'DELAY', 'DRUNK',
            'FEMALE', 'HURRY', 'INEVITABLE', 'INVITE', 'KISS', 'NEAT', 'POP',
            'PUNCH', 'QUIT', 'REPLY', 'REPRESENTATIVE', 'RESIST', 'RIP', 'RUB',
            'SILLY', 'SMILE', 'SPELL', 'STRETCH', 'STUPID', 'TEAR',
            'TEMPORARY', 'TOMORROW', 'WAKE', 'WRAP', 'YESTERDAY']

print(len(sestavi_zaporedje(nouns)))

# print(najdaljsa_veriga(nouns))