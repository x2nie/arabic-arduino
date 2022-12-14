# from arabicArduino import LCD,Console, gundul
from arabicArduino.utils import * #gundul, spell, apply_ligatures
from arabicArduino.lcd_console import Console

def spells(arabic:str):
    # a = gundul(arabic)
    a = arabic
    print(a)
    print('-'*10)
    # spell(a)
    # print('-'*10)
    a = apply_ligatures(a)

    print('~'*10)
    print(a)

    print('='*10)
    spell(a)

    planes:List[List[int]] = transformA2PlanesRTL(a)        #? not unique, might containing SPACE

    CGROM = empty_CGROM()
    # #? make unique:
    # chars:List[int] = []
    # txt = []                #? chr 0..7
    # for p in planes:
    #     if p in chars:
    #         txt.append(chars.index(p))
    #     elif p == ' ':
    #         txt.append(0x20)
    #     else:
    #         chars.append(p)
    #         txt.append(chars.index(p))
    for p in planes:
        print(repr(p))
    planes.reverse()
    # print_2x2(planes)
    print()

    print_LR_2x3(planes)


def spells2(arabic:str):
    a = gundul(arabic)
    print(a)
    print('-'*10)
    a = apply_ligatures(a)

    print('~'*10)
    print(a)

    print('='*10)
    spell(a)

    planes:List[List[int]] = transformA2PlanesRTL(a)        #? not unique, might containing SPACE
    for p in planes:
        print(repr(p))

    CGROM = empty_CGROM()
    # #? make unique:
    strA = build_CGROM(planes, CGROM)
    print('strA', '~'*10)
    print(strA)
    print('CGROM', '~'*10)
    print(CGROM)

    lcd = Console()
    for i,cc in enumerate(CGROM):
        if cc['active']:
            lcd.ccg(i, cc['plane'])

    print('writeArabic:',strA)
    lcd.writeArabic(strA)
    # planes.reverse()
    # print_2x2(planes)


# spells('بِسْمِ اللّٰهِ ')
# spells(' اللهم صَلِّ عَلى مُحَمَّدٍ')
# spells(' صلى الله عليه وسلم‎ ')
# spells(' صلى الله‎ ')

# spells(' صلى الله عَلى مُحَمَّدٍ‎ ')
# ░░░░██░░██  ██████░░░░  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ██░░░░░░██  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  
# ░░░░██░░██  ██░░██░░░░  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ████░░░░██  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  
# ░░░░██████  ██████░░░░  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  ░░░░░░░░██  ░░██░░░░░░  
# ░░░░██░░░░  ██░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░██  ░░░░██████  ░░░░░░░░░░  ░░░░░░░░██  ██░░██░░██  ░░░░░░░░░░  ░░░░░░░░██  ░░████████  
# ░░░░██████  ██████░░░░  ░░░░░░░░░░  ██████░░██  ░░░░██░░░░  ░░░░░░░░░░  ░░░░██████  ██░░██░░██  ░░░░░░░░░░  ██████░░██  ░░██░░░░██  
# ░░░░██░░██  ░░░░██░░░░  ░░░░░░░░░░  ██░░██████  ██████████  ░░░░░░░░░░  ░░░░██░░██  ██░░██░░██  ░░░░░░░░░░  ██░░██████  ██████████  
# ░░░░██████  ██████░░░░  ░░░░░░░░░░  ██░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░██████  ██████░░██  ░░░░░░░░░░  ██░░░░░░░░  ░░░░░░░░░░  
# ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ██████████  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ██████████  ░░░░░░░░░░  


# spells2(' صلى الله عَلى مُحَمَّدٍ‎ ')
# spells2(' اللهم صَلِّ عَلى مُحَمَّدٍ')
# writeArabic: [0, 1, 2, 3, 4, 32, 5, 6, 32, 7, 'not-enough-for:0', 32, 'not-enough-for:1', 'not-enough-for:2']
#     ░░░░░░░░░░     ░░░░░░░░██ ░░░░░░░░░░     ░░░░░░░░░░ ░░░░░░░░░░ ░░░░██░░░░ ░░░░██░░░░ ░░░░██░░░░ 
#     ░░░░░░░░░░     ░░░░░░░░██ ░░░░░░░░░░     ░░░░░░░░░░ ░░░░░░░░░░ ░░░░██░░░░ ░░░░██░░░░ ░░░░██░░░░ 
#     ░░░░░░░░░░     ░░░░░░░░██ ░░██░░░░░░     ░░░░░░░░░░ ░░░░░░░░░░ ░░░░██░░░░ ░░░░██░░░░ ░░░░██░░░░ 
#     ░░░░██████     ░░░░░░░░██ ░░████████     ██████░░░░ ░░██████░░ ░░░░██░░░░ ░░░░██░░░░ ░░░░██░░░░ 
#     ░░░░██░░░░     ░░██░░░░██ ░░██░░░░██     ██░░██░░░░ ░░██░░██░░ ░░░░██░░░░ ░░░░██░░░░ ░░░░██░░░░ 
#     ██████████     ░░██░░░░██ ██████████     ██████████ ██████████ ██████████ ██████░░░░ ░░░░██░░░░ 
#     ░░░░░░░░░░     ░░████████ ░░░░░░░░░░     ██░░░░░░░░ ░░██░░██░░ ░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ 
#     ░░░░░░░░░░     ░░░░░░░░░░ ░░░░░░░░░░     ██░░░░░░░░ ░░██████░░ ░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ 

# # spells2(' صلى الله عليه وسلم‎ ')
# spells(' صلى الله عَلى مُحَمَّدٍ‎ ')
# spells('بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيْمِ')
# spells('اَلْحَمْدُ لِلّٰهِ رَبِّ الْعٰلَمِيْنَ')
# spells(' الرَّحْمٰنِ الرَّحِيْمِ')
# spells('مٰلِكِ يَوْمِ الدِّيْنِ')
# spells('اِيَّاكَ نَعْبُدُ وَاِيَّاكَ نَسْتَعِيْنُ')
# spells('اِهْدِنَا الصِّرَاطَ الْمُسْتَقِيْمَ')
# spells('صِرَاطَ الَّذِيْنَ اَنْعَمْتَ عَلَيْهِمْ')
# spells(' غَيْرِ الْمَغْضُوْبِ عَلَيْهِمْ')
# spells(' وَلَا الضَّآلِّيْنَ')
# # spells2(' وَلَا الضَّآلِّيْنَ')

# spells('الٓمّٓ')
# spells('ذٰلِكَ الْكِتٰبُ لَا رَيْبَ ۛ فِيْهِ ۛ هُدًى لِّلْمُتَّقِيْنَ')

# # الَّذِيْنَ يُؤْمِنُوْنَ بِالْغَيْبِ وَيُقِيْمُوْنَ الصَّلٰوةَ وَمِمَّا رَزَقْنٰهُمْ يُنْفِقُوْنَ
# # spells('')
# spells('الَّذِيْنَ يُؤْمِنُوْنَ بِالْغَيْبِ')
# spells('وَيُقِيْمُوْنَ الصَّلٰوةَ')
# spells('وَمِمَّا رَزَقْنٰهُمْ يُنْفِقُوْنَ')

# # وَالَّذِيْنَ يُؤْمِنُوْنَ بِمَآ اُنْزِلَ اِلَيْكَ وَمَآ اُنْزِلَ مِنْ قَبْلِكَ وَبِالْاٰخِرَةِ هُمْ يُوْقِنُوْنَ
# # spells('')
# spells('وَالَّذِيْنَ يُؤْمِنُوْنَ بِمَآ اُنْزِلَ اِلَيْكَ ')
# spells('وَمَآ اُنْزِلَ مِنْ قَبْلِكَ')
# spells(' وَبِالْاٰخِرَةِ هُمْ يُوْقِنُوْنَ')

# # spells(' صلى الله عَلى مُحَمَّدٍ‎ ')
# # spells(' هُدًى لِّلْمُتَّقِيْنَ')

# # اُولٰٓئِكَ عَلٰى هُدًى مِّنْ رَّبِّهِمْ ۙ وَاُولٰٓئِكَ هُمُ الْمُفْلِحُوْنَ
# # spells('')
# spells('اُولٰٓئِكَ عَلٰى هُدًى مِّنْ رَّبِّهِمْ ۙ')
# spells('وَاُولٰٓئِكَ هُمُ الْمُفْلِحُوْنَ')


# # اِنَّ الَّذِيْنَ كَفَرُوْا سَوَآءٌ عَلَيْهِمْ ءَاَنْذَرْتَهُمْ اَمْ لَمْ تُنْذِرْهُمْ لَا يُؤْمِنُوْنَ
# spells(' اِنَّ الَّذِيْنَ كَفَرُوْا سَوَآءٌ عَلَيْهِمْ')
# spells('ءَاَنْذَرْتَهُمْ اَمْ لَمْ تُنْذِرْهُمْ لَا يُؤْمِنُوْنَ')

# # خَتَمَ اللّٰهُ عَلٰى قُلُوْبِهِمْ وَعَلٰى سَمْعِهِمْ ۗ وَعَلٰٓى اَبْصَارِهِمْ غِشَاوَةٌ وَّلَهُمْ عَذَابٌ عَظِيْمٌ
# # spells('')
# spells(' خَتَمَ اللّٰهُ عَلٰى قُلُوْبِهِمْ وَعَلٰى سَمْعِهِمْ ۗ')
# spells('وَعَلٰٓى اَبْصَارِهِمْ غِشَاوَةٌ')
# spells(' وَّلَهُمْ عَذَابٌ عَظِيْمٌ')

# # وَمِنَ النَّاسِ مَنْ يَّقُولُ اٰمَنَّا بِاللّٰهِ وَبِالْيَوْمِ الْاٰخِرِ وَمَا هُمْ بِمُؤْمِنِيْنَۘ
# # spells('  النَّاسِ  ')
# spells(' وَمِنَ النَّاسِ مَنْ يَّقُولُ اٰمَنَّا بِاللّٰهِ ')
# spells(' وَبِالْيَوْمِ الْاٰخِرِ وَمَا هُمْ بِمُؤْمِنِيْنَۘ')
# # spells('')

# # يُخٰدِعُوْنَ اللّٰهَ وَالَّذِيْنَ اٰمَنُوا ۚ وَمَا يَخْدَعُوْنَ اِلَّآ اَنْفُسَهُمْ وَمَا يَشْعُرُوْنَۗ
# # spells('')
# spells('يُخٰدِعُوْنَ اللّٰهَ وَالَّذِيْنَ اٰمَنُوا ۚ')
# spells(' وَمَا يَخْدَعُوْنَ اِلَّآ اَنْفُسَهُمْ وَمَا يَشْعُرُوْنَۗ')


# # فِيْ قُلُوْبِهِمْ مَّرَضٌ ۙ فَزَادَهُمُ اللّٰهُ مَرَضًا ۚ وَلَهُمْ عَذَابٌ اَلِيْمٌۙ بِۘمَا كَانُوْا يَكْذِبُوْنَ
# # spells('')
# spells('فِيْ قُلُوْبِهِمْ مَّرَضٌ ۙ فَزَادَهُمُ اللّٰهُ مَرَضًا ۚ')
# spells(' وَلَهُمْ عَذَابٌ اَلِيْمٌۙ بِۘمَا كَانُوْا يَكْذِبُوْنَ')

# # وَإِذَا قِيلَ لَهُمْ لَا تُفْسِدُوا فِي الْأَرْضِ قَالُوا إِنَّمَا نَحْنُ مُصْلِحُونَ
# # spells(' الْأَرْضِ')
# # spells('')
# spells('وَإِذَا قِيلَ لَهُمْ لَا تُفْسِدُوا فِي الْأَرْضِ')
# spells('قَالُوا إِنَّمَا نَحْنُ مُصْلِحُونَ')

# # أَلَا إِنَّهُمْ هُمُ الْمُفْسِدُونَ وَلَٰكِنْ لَا يَشْعُرُونَ
# # spells('')
# spells('أَلَا إِنَّهُمْ هُمُ الْمُفْسِدُونَ وَلَٰكِنْ لَا يَشْعُرُونَ')

# # وَإِذَا قِيلَ لَهُمْ آمِنُوا كَمَا آمَنَ النَّاسُ قَالُوا أَنُؤْمِنُ كَمَا آمَنَ السُّفَهَاءُ ۗ أَلَا إِنَّهُمْ هُمُ السُّفَهَاءُ وَلَٰكِنْ لَا يَعْلَمُونَ
# # spells('')
# spells('وَإِذَا قِيلَ لَهُمْ آمِنُوا كَمَا آمَنَ النَّاسُ')
# spells('قَالُوا أَنُؤْمِنُ كَمَا آمَنَ السُّفَهَاءُ ۗ ')
# spells(' أَلَا إِنَّهُمْ هُمُ السُّفَهَاءُ وَلَٰكِنْ لَا يَعْلَمُونَ')

# # qulhu
# spells(' بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيْمِ ')
# spells('  قُلْ هُوَ اللَّهُ أَحَدٌ ')
# spells(' اللَّهُ الصَّمَدُ ')
# spells(' لَمْ يَلِدْ وَلَمْ يُولَدْ ')
# spells(' وَلَمْ يَكُنْ لَهُ كُفُوًا أَحَدٌ ')

# # annas
# spells(' بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيْمِ')
# spells(' قُلْ أَعُوذُ بِرَبِّ النَّاسِ ')
# spells(' مَلِكِ النَّاسِ ')
# spells(' إِلَٰهِ النَّاسِ ')
# spells(' مِنْ شَرِّ الْوَسْوَاسِ الْخَنَّاسِ  ')
# spells(' الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ ')
# spells(' مِنَ الْجِنَّةِ وَالنَّاسِ ')

# #alaq
# spells('بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيْمِ ')
# spells(' اقْرَأْ بِاسْمِ رَبِّكَ الَّذِي خَلَقَ ')

# spells(' خَلَقَ الْإِنْسَانَ مِنْ عَلَقٍ ')
# spells(' اقْرَأْ وَرَبُّكَ الْأَكْرَمُ ')
# spells(' الَّذِي عَلَّمَ بِالْقَلَمِ  ')
# spells(' عَلَّمَ الْإِنْسَانَ مَا لَمْ يَعْلَمْ ')
# spells(' كَلَّا إِنَّ الْإِنْسَانَ لَيَطْغَىٰ ')
# spells(' أَنْ رَآهُ اسْتَغْنَىٰ ')
# spells(' إِنَّ إِلَىٰ رَبِّكَ الرُّجْعَىٰ  ')
# spells(' أَرَأَيْتَ الَّذِي يَنْهَىٰ ')
# spells(' عَبْدًا إِذَا صَلَّىٰ ')
# spells(' أَرَأَيْتَ إِنْ كَانَ عَلَى الْهُدَىٰ ')
# spells(' أَوْ أَمَرَ بِالتَّقْوَىٰ ')
# spells(' أَرَأَيْتَ إِنْ كَذَّبَ وَتَوَلَّىٰ ')
# spells(' أَلَمْ يَعْلَمْ بِأَنَّ اللَّهَ يَرَىٰ  ')
# spells(' كَلَّا لَئِنْ لَمْ يَنْتَهِ لَنَسْفَعًا بِالنَّاصِيَةِ ')
# spells(' نَاصِيَةٍ كَاذِبَةٍ خَاطِئَةٍ ')
# spells(' فَلْيَدْعُ نَادِيَهُ ')
# spells(' سَنَدْعُ الزَّبَانِيَةَ ')
# spells(' كَلَّا لَا تُطِعْهُ وَاسْجُدْ وَاقْتَرِبْ ۩ ')

# #a'la
# spells(' بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيْمِ  ')
# spells(' سَبِّحِ اسْمَ رَبِّكَ الْأَعْلَى ')
# spells(' الَّذِي خَلَقَ فَسَوَّىٰ  ')
# spells(' وَالَّذِي قَدَّرَ فَهَدَىٰ ')
# spells(' وَالَّذِي أَخْرَجَ الْمَرْعَىٰ ')
# spells(' فَجَعَلَهُ غُثَاءً أَحْوَىٰ ')
# spells(' سَنُقْرِئُكَ فَلَا تَنْسَىٰ ')
# spells(' إِلَّا مَا شَاءَ اللَّهُ ۚ إِنَّهُ يَعْلَمُ الْجَهْرَ وَمَا يَخْفَىٰ ')
# spells(' وَنُيَسِّرُكَ لِلْيُسْرَىٰ ')
# spells(' فَذَكِّرْ إِنْ نَفَعَتِ الذِّكْرَىٰ ')
# spells(' سَيَذَّكَّرُ مَنْ يَخْشَىٰ ')
# spells(' وَيَتَجَنَّبُهَا الْأَشْقَى ')
# spells(' الَّذِي يَصْلَى النَّارَ الْكُبْرَىٰ ')
# spells(' ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ  ')
# spells(' قَدْ أَفْلَحَ مَنْ تَزَكَّىٰ ')
# spells(' وَذَكَرَ اسْمَ رَبِّهِ فَصَلَّىٰ ')
# spells(' بَلْ تُؤْثِرُونَ الْحَيَاةَ الدُّنْيَا ')
# spells(' وَالْآخِرَةُ خَيْرٌ وَأَبْقَىٰ ')
# spells(' إِنَّ هَٰذَا لَفِي الصُّحُفِ الْأُولَىٰ ')

# # spells(' إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ ')
# spells('  إِنَّ   هَٰذَا   لَفِى   ٱلصُّحُفِ   ٱلْأُولَىٰ ')
# # spell('  إِنَّ   هَٰذَا   لَفِى   ٱلصُّحُفِ   ٱلْأُولَىٰ ')

spells('BASMALAH')