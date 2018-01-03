from datetime import datetime

bichinhos = []


def insert(bichinho):
    bichinho['created_on'] = datetime.now()
    bichinhos.append(bichinho)
    return True
