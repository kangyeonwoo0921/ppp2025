import asyncio
import telegram

async def send_daily_message(): #실행시킬 함수명 임의지정
    token = "7985392578:AAFRd_Z6-QBbsSe7uUAJBuU_6pvLbO_Y8L0" 
    chat_id = 7836352783
    bot = telegram.Bot(token = token)

    message = "강연우천재재"
    await bot.send_message(chat_id,message)

async def main():
    while True:
        await send_daily_message()
        await asyncio.sleep(86400) # 24시간 대기

if __name__ == "__main__":
    asyncio.run(main())
