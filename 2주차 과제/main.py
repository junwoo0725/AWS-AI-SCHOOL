import asyncio
from typing import List

from utils import (
    print_menu,
    add_order,
    order_generator,
    async_log,
    MENU
)


async def run_kiosk() -> None:
    order_list: List[str] = []
    total_price: int = 0

    print("===== 카페 키오스크 =====")

    while True:
        print_menu()

        try:
            choice: int = int(input("번호 입력: "))

            if choice == 0:
                break

            if choice not in MENU:
                raise ValueError("메뉴에 없는 번호입니다.")

            total_price = add_order(choice, order_list, total_price)

            # 비동기 로그 기록
            await async_log(f"{MENU[choice]['name']} 주문 추가")

        except ValueError as e:
            print(f"입력 오류: {e}")

    print("\n===== 주문 내역 =====")

    if not order_list:
        print("주문한 메뉴가 없습니다.")
    else:
        for item in order_generator(order_list):
            print("-", item)

        print(f"총 결제 금액: {total_price}원")

    print("이용해주셔서 감사합니다 😊")


if __name__ == "__main__":
    asyncio.run(run_kiosk())

from typing import Dict, List, Generator
import asyncio

# 메뉴 데이터
MENU: Dict[int, Dict[str, int]] = {
    1: {"name": "아메리카노", "price": 3000},
    2: {"name": "카페라떼", "price": 3500},
    3: {"name": "카푸치노", "price": 3500},
    4: {"name": "바닐라라떼", "price": 3800},
}


def print_menu() -> None:
    print("\n메뉴를 선택하세요")
    for key, value in MENU.items():
        print(f"{key}. {value['name']} - {value['price']}원")
    print("0. 주문 완료")


def add_order(
    choice: int,
    order_list: List[str],
    total_price: int
) -> int:
    item = MENU[choice]
    order_list.append(item["name"])
    print(f"{item['name']}가 장바구니에 추가되었습니다.")
    return total_price + item["price"]


def order_generator(order_list: List[str]) -> Generator[str, None, None]:
    for item in order_list:
        yield item


async def async_log(message: str) -> None:
    await asyncio.sleep(0.2)  # 비동기 작업 시뮬레이션
    print(f"[LOG] {message}")
