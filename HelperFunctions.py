from API.helldivers_2_client.models import Assignment2

def format_major_order(MO: Assignment2) -> str:
    return f'Brief: {MO.briefing}\nDescription: {MO.description}\nExpiration: {MO.expiration.strftime("%H:%M:%S %d-%b-%Y")}\nProgress: {MO.progress}'

def check_new_order(MO: Assignment2, currentMOID: int) -> bool:
    if currentMOID != MO.id:
        # Wrtie new mo id
        with open('majorOrder.txt', 'w') as f:
            f.write(str(MO.id))
        
        currentMOID = MO.id
        return True
    else:
        return False