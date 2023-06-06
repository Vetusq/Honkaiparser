
with open("НАкитайском.txt", "r", encoding="utf-8") as file, open("Промежуток.txt", "w", encoding="utf-8") as file2:
    for line in file:
        index = line.find("{")
        for i in range(index, len(line)):
            line = line.replace("男", "male")
            line = line.replace("女", "female")
            line = line.replace("五星", "legend")
            line = line.replace("瓦尔特" , "Welt")
            line = line.replace("姬子" , "Himeko")
            line = line.replace("布洛妮哑" , "Bronya")
            line = line.replace("希儿" , "Seele")
            line = line.replace("克拉拉" , "Clara")
            line = line.replace("景元" , "Jing Yuan")
            line = line.replace("彦卿" , "Yanqing")
            line = line.replace("白露" , "Bailu")
            line = line.replace("杰帕德" , "Gepard")
            line = line.replace("停云" , "Tingyun")
            line = line.replace("银河铁之夜" , "Night on the Milky Way")
            line = line.replace("于夜色中" , "In the Night")
            line = line.replace("无可取代的东西" , "Something Irreplaceable")
            line = line.replace("但战斗还未结束" , "But the Battle Isn't Over")
            line = line.replace("以世界之名" , "In the Name of the World")
            line = line.replace("制胜的瞬间" , "Moment of Victory")
            line = line.replace("拂晓之前" , "Before Dawn")
            line = line.replace("如泥酣眠" , "Sleep Like the Dead")
            line = line.replace("时节不居" , "Time Waits for No One")
            line = line.replace("记一位星神的陨落" , "On the Fall of an Aeon")
            line = line.replace("星海巡航" , "Cruising in the Stellar Sea")
            line = line.replace("记忆的质料" , "Texture of Memories")
            line = line.replace("银河铁道之夜", "Night on the Milky Way")
        line += ""
        file2.write(line)
with open("Промежуток.txt", "r", encoding="utf-8") as file2, open("Готовые данные.txt", "w", encoding="utf-8") as file3:
    for line in file2:
        index = line.find(":")
        if index != -1:
            if "6" in line[index:index+7]:
                line = line.replace(line[index:index+10], "--NA--")
            elif "7" in line[index:index+7]:
                line = line.replace(line[index:index+10], "--EU--")
        line += ""
        file3.write(line)