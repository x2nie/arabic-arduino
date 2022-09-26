# ref: https://www.unicode.org/charts/PDF/U1FB00.pdf
# ref: https://www.unicode.org/charts/PDF/U2580.pdf
import enum


char_2x3 = [
[0, ' ', 32, 'SPACE'],
[1, '🬁', 129793, 'BLOCK SEXTANT-2'],
[2, '🬀', 129792, 'BLOCK SEXTANT-1'],
[3, '🬂', 129794, 'BLOCK SEXTANT-12'],
[4, '🬇', 129799, 'BLOCK SEXTANT-4'],
[5, '🬉', 129801, 'BLOCK SEXTANT-24'],
[6, '🬈', 129800, 'BLOCK SEXTANT-14'],
[7, '🬊', 129802, 'BLOCK SEXTANT-124'],
[8, '🬃', 129795, 'BLOCK SEXTANT-3'],
[9, '🬅', 129797, 'BLOCK SEXTANT-23'],
[10, '🬄', 129796, 'BLOCK SEXTANT-13'],
[11, '🬆', 129798, 'BLOCK SEXTANT-123'],
[12, '🬋', 129803, 'BLOCK SEXTANT-34'],
[13, '🬍', 129805, 'BLOCK SEXTANT-234'],
[14, '🬌', 129804, 'BLOCK SEXTANT-134'],
[15, '🬎', 129806, 'BLOCK SEXTANT-1234'],
[16, '🬞', 129822, 'BLOCK SEXTANT-6'],
[17, '🬠', 129824, 'BLOCK SEXTANT-26'],
[18, '🬟', 129823, 'BLOCK SEXTANT-16'],
[19, '🬡', 129825, 'BLOCK SEXTANT-126'],
[20, '🬦', 129830, 'BLOCK SEXTANT-46'],
[00, '▐', 9616,   'RIGHT HALF BLOCK'],
[22, '🬧', 129831, 'BLOCK SEXTANT-146'],
[23, '🬨', 129832, 'BLOCK SEXTANT-1246'],
[24, '🬢', 129826, 'BLOCK SEXTANT-36'],
[25, '🬤', 129828, 'BLOCK SEXTANT-236'],
[26, '🬣', 129827, 'BLOCK SEXTANT-136'],
[27, '🬥', 129829, 'BLOCK SEXTANT-1236'],
[28, '🬩', 129833, 'BLOCK SEXTANT-346'],
[29, '🬫', 129835, 'BLOCK SEXTANT-2346'],
[29, '🬻', 129851, 'BLOCK SEXTANT-2346'],
[30, '🬪', 129834, 'BLOCK SEXTANT-1346'],
[31, '🬬', 129836, 'BLOCK SEXTANT-12346'],
[32, '🬏', 129807, 'BLOCK SEXTANT-5'],
[33, '🬑', 129809, 'BLOCK SEXTANT-25'],
[34, '🬐', 129808, 'BLOCK SEXTANT-15'],
[35, '🬒', 129810, 'BLOCK SEXTANT-125'],
[36, '🬖', 129814, 'BLOCK SEXTANT-45'],
[37, '🬘', 129816, 'BLOCK SEXTANT-245'],
[38, '🬗', 129815, 'BLOCK SEXTANT-145'],
[39, '🬙', 129817, 'BLOCK SEXTANT-1245'],
[40, '🬓', 129811, 'BLOCK SEXTANT-35'],
[41, '🬔', 129812, 'BLOCK SEXTANT-235'],
[00, '▌', 9612,   'LEFT HALF BLOCK'],
[43, '🬕', 129813, 'BLOCK SEXTANT-1235'],
[44, '🬚', 129818, 'BLOCK SEXTANT-345'],
[45, '🬜', 129820, 'BLOCK SEXTANT-2345'],
[46, '🬛', 129819, 'BLOCK SEXTANT-1345'],
[47, '🬝', 129821, 'BLOCK SEXTANT-12345'],
[48, '🬭', 129837, 'BLOCK SEXTANT-56'],
[49, '🬯', 129839, 'BLOCK SEXTANT-256'],
[50, '🬮', 129838, 'BLOCK SEXTANT-156'],
[51, '🬰', 129840, 'BLOCK SEXTANT-1256'],
[52, '🬵', 129845, 'BLOCK SEXTANT-456'],
[53, '🬷', 129847, 'BLOCK SEXTANT-2456'],
[54, '🬶', 129846, 'BLOCK SEXTANT-1456'],
[55, '🬸', 129848, 'BLOCK SEXTANT-12456'],
[56, '🬱', 129841, 'BLOCK SEXTANT-356'],
[57, '🬳', 129843, 'BLOCK SEXTANT-2356'],
[58, '🬲', 129842, 'BLOCK SEXTANT-1356'],
[59, '🬴', 129844, 'BLOCK SEXTANT-12356'],
[60, '🬹', 129849, 'BLOCK SEXTANT-3456'],
[62, '🬺', 129850, 'BLOCK SEXTANT-13456'],
[63, '█', 9608,   'FULL BLOCK'],
]

if __name__ == '__main__':
    for i,line in enumerate(char_2x3):
        name = line[3]
        if '-' in name:
            name = name[name.index('-')+1:]
            # print(name)
            num = 0
            for n in name:
                bit = '214365'.index(n)
                num += (1 << bit)
            line[0] = num
    char_2x3.sort()
    for line in char_2x3:
        print(line)