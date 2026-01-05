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
