RESULT = {}

def remove_unit_production(keyList):
    global RESULT
    for key, value in RESULT.items():
        if key in keyList:
            tempList = []
            for prod in value:
                if len(prod.split(" ")) == 2:
                    tempList.append(prod)
                else:
                    for i in RESULT[prod]:
                        if i not in tempList:
                            tempList.append(i)
            RESULT[key] = tempList

def get_set_of_production():
    global RESULT
    RESULT.clear()
    with open("modules/rules-of-cfg.txt", "r", encoding="utf-8") as txt:
        for lines in txt:
            line = lines.strip().split(" → ")
            lhs = line[0]
            rhs = line[1].split(" | ")
            if lhs in RESULT.keys():
                RESULT[lhs].extend(rhs)
            else:
                RESULT[lhs] = rhs
    # Melakukan lowercase pada string
    for key, value in RESULT.items():
        if key == "PropNoun":
            tempList = []
            for val in value:
                if val not in tempList:
                    tempList.append(val.lower())
            RESULT[key] = tempList
    phrases = ["NumP", "AdvP", "AdjP", "PP", "NP", "VP"]
    remove_unit_production(phrases)
    patterns = ["S", "P", "O", "Pel", "Ket"]
    remove_unit_production(patterns)
    tempList = []
    tempDict = {}
    counter = 1
    for key, value in RESULT.items():
        if key == "K":
            for val in value:
                if len(val.split(" ")) > 2:
                    temp = val.split(" ")
                    while len(temp) > 2:
                        check_str = temp[0] + " " + temp[1]
                        is_found = False
                        for k, v in tempDict.items():
                            if check_str == v:
                                is_found = True
                                temp.pop(0)
                                temp.pop(0)
                                temp.insert(0, k)
                                break
                        if not is_found:
                            tempDict["K" + str(counter)] = check_str
                            temp.pop(0)
                            temp.pop(0)
                            temp.insert(0, "K" + str(counter))
                            counter += 1
                    tempList.append(" ".join(temp))
                else:
                    tempList.append(val)
            RESULT[key] = tempList
    for key, value in tempDict.items():
        RESULT[key] = [value]
    return RESULT

def print_result_to_file(file_path):
    with open(file_path, "w", encoding="utf-8") as output_file:
        for key, value in RESULT.items():
            output_file.write(f"{key} → {' | '.join(value)}\n")

def get_raw_set_of_production():
    global RESULT
    RESULT.clear()
    with open("modules/rules-of-cfg.txt", "r", encoding="utf-8") as f:
        for lines in f:
            line = lines.splitlines()
            line = line[0].split(" → ")
            lhs = line[0]
            rhs = line[1].split(" | ")
            if lhs in RESULT.keys():
                RESULT[lhs].extend(rhs)
            else:
                RESULT[lhs] = rhs
    for key, value in RESULT.items():
        if key == "PropNoun":
            tempList = []
            for val in value:
                if val not in tempList:
                    tempList.append(val.lower())
            RESULT[key] = tempList
    tempList = []
    tempDict = {}
    counter = 1
    for key, value in RESULT.items():
        if key == "K":
            for val in value:
                if len(val.split(" ")) > 2:
                    temp = val.split(" ")
                    while len(temp) > 2:
                        check_str = temp[0] + " " + temp[1]
                        is_found = False
                        for k, v in tempDict.items():
                            if check_str == v:
                                is_found = True
                                temp.pop(0)
                                temp.pop(0)
                                temp.insert(0, k)
                                break
                        if not is_found:
                            tempDict["K" + str(counter)] = check_str
                            temp.pop(0)
                            temp.pop(0)
                            temp.insert(0, "K" + str(counter))
                            counter += 1
                    tempList.append(" ".join(temp))
                else:
                    tempList.append(val)
            RESULT[key] = tempList
    for key, value in tempDict.items():
        RESULT[key] = [value]
    return RESULT
