"""
L1 CLI Vault example challenge.

Intentional behavior: only admin can read vault secret when maintenance mode is active.
Unintended flow: state confusion + missing precondition can let a normal user pivot identity.
"""

from dataclasses import dataclass


FLAG = "FLAG{vault_flow_chain_7421}"


@dataclass
class User:
    name: str
    role: str


USERS = {
    "alice": User("alice", "user"),
    "bob": User("bob", "user"),
    "ops": User("ops", "admin"),
}


state = {
    "current_user": USERS["alice"],
    "pending_user": None,
    "maintenance_mode": False,
    "audit": [],
}


def log(event: str) -> None:
    state["audit"].append(event)


def whoami() -> str:
    return f"{state['current_user'].name} ({state['current_user'].role})"


def set_timezone(value: str) -> str:
    # Bug: special timezone string toggles maintenance mode for any logged-in user.
    if value.upper() == "UTC+OPS":
        state["maintenance_mode"] = True
        log("maintenance_enabled_via_timezone")
        return "timezone updated"
    return "timezone updated"


def open_support_ticket(target_user: str) -> str:
    if target_user not in USERS:
        return "unknown user"
    # Intended for support workflows, but lacks role validation.
    state["pending_user"] = target_user
    log(f"ticket_open_for_{target_user}")
    return "ticket opened"


def assume_pending_identity() -> str:
    # Bug: no authorization check before identity switch.
    pending = state["pending_user"]
    if not pending:
        return "no pending ticket"
    state["current_user"] = USERS[pending]
    log(f"identity_assumed_{pending}")
    return f"assumed identity {pending}"


def read_vault() -> str:
    user = state["current_user"]
    if user.role != "admin":
        return "access denied: admin required"
    if not state["maintenance_mode"]:
        return "access denied: maintenance mode required"
    return FLAG


def help_text() -> str:
    return (
        "commands:\n"
        "  whoami\n"
        "  tz <value>\n"
        "  ticket <username>\n"
        "  assume\n"
        "  read\n"
        "  quit\n"
    )


def run_cli() -> None:
    print("Vault CLI")
    print(help_text())
    while True:
        raw = input("> ").strip()
        if not raw:
            continue
        parts = raw.split()
        cmd = parts[0]

        if cmd == "quit":
            print("bye")
            return
        if cmd == "whoami":
            print(whoami())
        elif cmd == "tz" and len(parts) == 2:
            print(set_timezone(parts[1]))
        elif cmd == "ticket" and len(parts) == 2:
            print(open_support_ticket(parts[1]))
        elif cmd == "assume":
            print(assume_pending_identity())
        elif cmd == "read":
            print(read_vault())
        else:
            print("unknown command")


if __name__ == "__main__":
    run_cli()
