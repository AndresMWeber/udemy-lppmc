



# ip = input("Hi, please type in your IP adress")
#
# seg1 = ""
# seg2 = ""
# seg3 = ""
# seg4 = ""
# answer = ""
#
#
# for i in range (0, len(ip)):
#     if ip[i] in "0123456789":
#         continue
#     answer = answer + ip[i]
# print("the ip number contains {} segments" .format(len(answer)+1))
#
#
#
#
# for i in range (0, len(ip)):
#     if ip[i] in ("."):
#         break
#     seg1 = seg1 + ip[i]
# print("Det första segmentet är {} siffror långt" .format(len(seg1)))
#
#
#
#
#
# for i in range (len(seg1) + 1, len(ip)):
#     if ip[i] in ("."):
#         break
#     seg2 = seg2 + ip[i]
# print("Det andra segmentet är {} siffror långt" .format(len(seg2)))
#
#
#
#
#
# for i in range (len(seg1 + seg2) + 2, len(ip)):
#     if ip[i] in ("."):
#         break
#     seg3 = seg3 + ip[i]
# print("Det tredje segmentet är {} siffror långt" .format(len(seg3)))
#
#
#
#
# for i in range (len(seg1 + seg2 + seg3) + 3, len(ip)):
#     if ip[i] in ("."):
#         break
#     seg4 = seg4 + ip[i]
# print("Det fjärde segmentet är {} siffror långt" .format(len(seg4)))



ipAddress = "192.168.0.1"

if ipAddress[-1] != ".":
    ipAddress += "."

segment = 1
segment_lenght = 0


for character in ipAddress:
        if character == ".":
            print("the {0} segment contains {1} characters" .format(segment, segment_lenght))

            segment += 1
            segment_lenght = 0
        else:
            segment_lenght += 1







