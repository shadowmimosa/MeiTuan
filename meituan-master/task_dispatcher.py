from workers import app
from redis import StrictRedis, ConnectionPool
import json
import time
pool_r = ConnectionPool(host='localhost', port=6379, db=0)
r = StrictRedis(connection_pool=pool_r)


def manage_crawl_task():
    while True:
        shop = r.lpop("shop")

        if shop:
            shop = shop.decode()
            shop = json.loads(shop)
            content = app.send_task('tasks.crawl', args=(shop,))
            # content = app.send_task('tasks.crawl', kwargs=shop)
            print(content)
        time.sleep(0.001)
        # else:
        #     print("队列为空")
if __name__ == '__main__':
    manage_crawl_task()
    # url = r.lpop("urlqueue")
    # print(url.decode())