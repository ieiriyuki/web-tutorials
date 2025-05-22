import asyncio
import csv
from datetime import datetime, timedelta, timezone
from random import randint
import aiohttp


async def post_to_localhost(id=0, amount=200, request_id=0):
    url = "http://app:8000/"
    await asyncio.sleep(randint(0, 3))
    started_at = datetime.now(tz=timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S")

    data_dict = {
        "id": id,
        "amount": amount,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data_dict) as response:
            response_data = await response.json()

    responded_at = datetime.now(tz=timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S")
    result = {
        "request_id": request_id,
        "started_at": started_at,
        "responded_at": responded_at,
        "id": id,
        "amount": amount,
        "result": response_data.get("result"),
        "current_credit": response_data.get("current_credit"),
        "total_credit": response_data.get("total_credit"),
    }
    return result


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        num_id = 8
        for _id in range(num_id):
            for num in range(8):
                request_id = num + _id * num_id
                tasks.append(tg.create_task(post_to_localhost(id=_id, amount=200, request_id=request_id)))

    results = [task.result() for task in tasks]
    sorted_results = sorted(
        sorted(results, key=lambda x: x["responded_at"]),
        key=lambda x: x["id"]
    )
    return sorted_results


if __name__ == "__main__":
    result = asyncio.run(main())
    with open("./data/result.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["request_id", "started_at", "responded_at", "id", "amount", "result", "current_credit", "total_credit"])
        writer.writeheader()
        for row in result:
            writer.writerow(row)
