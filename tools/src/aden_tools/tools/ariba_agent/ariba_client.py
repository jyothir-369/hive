
import httpx
from .auth import OAuth2Client


class AribaClient:
    BASE_URL = "https://api.ariba.com/v2/opportunities"

    def __init__(self):
        self.auth = OAuth2Client(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_SECRET",
            token_url="https://api.ariba.com/oauth/token",
        )

    async def search_async(self, query: dict):
        token = await self.auth.get_token_async()

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.BASE_URL,
                json=query,
                headers=headers,
                timeout=10,
            )

        return response.json().get("opportunities", [])
