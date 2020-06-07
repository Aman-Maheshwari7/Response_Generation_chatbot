


def response_generation("""input from backend"""):
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="username",
        passwd="password"
        )

    
    mycursor = mydb.cursor()
    """Access Database"""
    """string type S return"""
    return S