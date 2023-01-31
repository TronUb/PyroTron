from typing import Union

from pyrogram import raw



class InviteToGroupCall:
    async def invite_to_group_call(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_id: Union[int, str]
    ) -> "pyrogram.raw.base.Updates":
        """ Invite Users to Group Call
        """
        group_call = self.get_group_call(chat_id)

        if group_call is None:
            raise Exception("There is no active group call")

        if isinstance(user_id, list):
            users = [self.resolve_peer(x) for x in user_id]
        else:
            users = [self.resolve_peer(user_id)]

        call = group_call.call

        return await self.invoke(
            raw.functions.phone.InviteToGroupCall(
                call=raw.types.InputGroupCall(
                    id=call.id,
                    access_hash=call.access_hash
                ),
                users=users
            )
        )
