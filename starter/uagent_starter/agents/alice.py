from uagents.setup import fund_agent_if_low
from uagents import Agent, Context

from messages.basic import Message


BOB_ADDRESS = "agent1qg5nnsqs4emdk93yytmmdcgfzg9uxkpd3z8qsy6knnv6n8t6f2ehscqn0e4"


alice = Agent(
    name="alice",
    port=8000,
    seed="alice secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(alice.wallet.address())


@alice.on_interval(period=2.0)
async def send_message(ctx: Context):
    await ctx.send(BOB_ADDRESS, Message(message="Hello there bob."))


@alice.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")


if __name__ == "__main__":
    alice.run()