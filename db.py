db code
import psycopg2

db.connect()

print("OK")


n = int(input())

for i in range(n):
    print(i, end='')

print("hello, world!")
