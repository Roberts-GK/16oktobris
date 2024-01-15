fails=open("aste.txt", 'r', encoding='utf8')
# pārlūkot visu failu pa rindiņām! - .cikla konstrukcija
for ii in fails:
    print(ii)

fails.close()